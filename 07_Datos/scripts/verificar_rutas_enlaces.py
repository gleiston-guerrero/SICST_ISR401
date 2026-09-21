#!/usr/bin/env python3
"""
D5 — Verificador conservador de rutas/enlaces locales del repositorio SICST (V3).

Objetivo:
- comprobar enlaces Markdown/HTML y referencias LaTeX;
- comprobar rutas inequívocas escritas entre backticks;
- NO confundir DOI, versiones, nombres sueltos de archivos ni ejemplos con rutas reales.

Uso desde la raíz del repositorio:
    python3 07_Datos/scripts/verificar_rutas_enlaces.py

Genera:
    07_Datos/resultados/verificacion_rutas_enlaces.csv
    07_Datos/resultados/verificacion_rutas_enlaces.md

Código de salida:
    0 = 0 referencias locales faltantes dentro del alcance del verificador
    1 = existen referencias locales faltantes confirmadas
"""

from __future__ import annotations

import csv
import html
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

TEXT_EXTENSIONS = {
    ".md", ".markdown", ".tex", ".html", ".htm", ".css", ".js", ".mjs",
    ".cjs", ".json", ".yaml", ".yml", ".txt", ".csv", ".bib"
}

SKIP_DIRS = {
    ".git", ".github", ".idea", ".vscode", "__pycache__", "node_modules",
    ".venv", "venv", "dist", "build"
}

EXTERNAL_PREFIXES = (
    "http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#", "//"
)

COMMON_FILE_EXTENSIONS = {
    ".md", ".pdf", ".tex", ".bib", ".csv", ".xlsx", ".xls", ".docx",
    ".doc", ".txt", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
    ".mp3", ".mp4", ".wav", ".7z", ".zip", ".json", ".py", ".html",
    ".css", ".js", ".drawio", ".sha256"
}

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.I)
VERSION_RE = re.compile(r"^v?\d+(?:\.\d+){1,3}(?:[-_][A-Za-z0-9.-]+)?$", re.I)
COMMAND_RE = re.compile(
    r"^(?:git|python3?|py|pip3?|npm|npx|pdflatex|xelatex|ffprobe|ffmpeg|sha256sum)\s+",
    re.I,
)

MD_LINK_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
MD_REF_RE = re.compile(r'^\s*\[[^\]]+\]:\s*(\S+)', re.M)
HTML_LINK_RE = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.I)
CSS_URL_RE = re.compile(r'url\(\s*["\']?([^)"\']+)["\']?\s*\)', re.I)
LATEX_RE = re.compile(
    r'\\(?:includegraphics(?:\[[^\]]*\])?|input|include|bibliography|addbibresource)\{([^}]+)\}'
)
BACKTICK_RE = re.compile(r'`([^`\n]+)`')


def repo_root_from_script() -> Path:
    here = Path(__file__).resolve()
    candidate = here.parents[2]
    if (candidate / ".git").exists() or (candidate / "07_Datos").exists():
        return candidate
    cwd = Path.cwd().resolve()
    if (cwd / ".git").exists() or (cwd / "07_Datos").exists():
        return cwd
    return candidate


def clean_target(raw: str) -> str:
    s = html.unescape(raw.strip())
    # Quitar título Markdown opcional al final: archivo "título"
    s = re.sub(r'\s+["\'][^"\']*["\']\s*$', "", s)
    s = s.strip("<>").strip()
    s = unquote(s)
    s = s.split("#", 1)[0].split("?", 1)[0].strip()
    return s


def top_level_names(root: Path) -> set[str]:
    names = set()
    for p in root.iterdir():
        if p.name == ".git":
            continue
        names.add(p.name)
    return names


def is_external_or_nonpath(value: str) -> bool:
    if not value:
        return True
    low = value.lower()
    if low.startswith(EXTERNAL_PREFIXES):
        return True
    if DOI_RE.match(value):
        return True
    if VERSION_RE.match(value):
        return True
    if COMMAND_RE.match(value):
        return True
    if value.startswith("\\\\"):
        return True
    if re.match(r"^[A-Za-z]:[\\/]", value):
        return True
    if any(token in value for token in ("<", ">", "${", "$(", "{usuario}", "{archivo}")):
        return True
    if "*" in value:
        return True
    if "\n" in value or len(value) > 300:
        return True
    return False


def is_strict_backtick_path(value: str, root_names: set[str]) -> bool:
    """
    Solo considera ruta una mención entre backticks cuando es inequívoca.
    Se ignoran nombres sueltos como `index.html`, `diccionario_datos.csv`
    o `resultados/` porque pueden ser menciones contextuales y no enlaces.
    """
    if is_external_or_nonpath(value):
        return False

    v = value.replace("\\", "/").strip()
    if v.startswith("./") or v.startswith("../"):
        return True

    # Ruta explícita que comienza por un elemento real del nivel raíz.
    if "/" in v:
        first = v.split("/", 1)[0]
        if first in root_names:
            return True

    return False


def candidate_paths(root: Path, source: Path, raw_target: str, kind: str):
    t = clean_target(raw_target)
    if is_external_or_nonpath(t):
        return t, []

    t = t.replace("\\", "/")
    while t.startswith("./"):
        t = t[2:]

    candidates = [
        (source.parent / t).resolve(),
        (root / t.lstrip("/")).resolve(),
    ]

    if kind == "latex":
        p = Path(t)
        if not p.suffix:
            # \bibliography{referencias} normalmente implica .bib;
            # input/include normalmente .tex; includegraphics varias extensiones.
            for ext in (".tex", ".bib", ".png", ".jpg", ".jpeg", ".pdf", ".svg"):
                candidates.append((source.parent / (t + ext)).resolve())
                candidates.append((root / (t.lstrip("/") + ext)).resolve())

    seen = set()
    unique = []
    for c in candidates:
        key = os.path.normcase(str(c))
        if key not in seen:
            seen.add(key)
            unique.append(c)
    return t, unique


def is_within_repo(root: Path, p: Path) -> bool:
    try:
        p.relative_to(root)
        return True
    except ValueError:
        return False


def check_one(root: Path, source: Path, target: str, kind: str):
    cleaned, candidates = candidate_paths(root, source, target, kind)
    if not candidates:
        return None

    valid = [p for p in candidates if is_within_repo(root, p)]
    if not valid:
        return {
            "archivo_origen": source.relative_to(root).as_posix(),
            "tipo": kind,
            "referencia": cleaned,
            "estado": "FUERA_REPO",
            "resuelto_como": "",
        }

    for p in valid:
        if p.exists():
            return {
                "archivo_origen": source.relative_to(root).as_posix(),
                "tipo": kind,
                "referencia": cleaned,
                "estado": "OK",
                "resuelto_como": p.relative_to(root).as_posix(),
            }

    return {
        "archivo_origen": source.relative_to(root).as_posix(),
        "tipo": kind,
        "referencia": cleaned,
        "estado": "FALTANTE",
        "resuelto_como": "",
    }


def extract_refs(text: str, root_names: set[str], source_suffix: str):
    refs = []

    for m in MD_LINK_RE.finditer(text):
        refs.append(("markdown", m.group(1)))

    for m in MD_REF_RE.finditer(text):
        refs.append(("markdown_ref", m.group(1)))

    for m in HTML_LINK_RE.finditer(text):
        refs.append(("html", m.group(1)))

    # Solo interpretar url(...) como referencia CSS dentro de archivos .css.
    # En JavaScript existen expresiones como createObjectURL(blob) y
    # revokeObjectURL(url), que no son enlaces a archivos locales.
    if source_suffix.lower() == ".css":
        for m in CSS_URL_RE.finditer(text):
            refs.append(("css", m.group(1)))

    for m in LATEX_RE.finditer(text):
        refs.append(("latex", m.group(1)))

    for m in BACKTICK_RE.finditer(text):
        value = clean_target(m.group(1))
        if is_strict_backtick_path(value, root_names):
            refs.append(("backtick_ruta", value))

    return refs


def main() -> int:
    root = repo_root_from_script()
    root_names = top_level_names(root)

    results_dir = root / "07_Datos" / "resultados"
    results_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    scanned_files = 0

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        rel_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = path.read_text(encoding="utf-8-sig")
            except Exception:
                continue
        except Exception:
            continue

        scanned_files += 1
        seen_in_file = set()

        for kind, target in extract_refs(text, root_names, path.suffix):
            key = (kind, target)
            if key in seen_in_file:
                continue
            seen_in_file.add(key)

            result = check_one(root, path, target, kind)
            if result:
                rows.append(result)

    # Deduplicación final.
    dedup = []
    seen = set()
    for row in rows:
        key = (
            row["archivo_origen"],
            row["tipo"],
            row["referencia"],
            row["estado"],
            row["resuelto_como"],
        )
        if key not in seen:
            seen.add(key)
            dedup.append(row)
    rows = dedup

    missing = [r for r in rows if r["estado"] in {"FALTANTE", "FUERA_REPO"}]
    ok = [r for r in rows if r["estado"] == "OK"]

    csv_path = results_dir / "verificacion_rutas_enlaces.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "archivo_origen",
                "tipo",
                "referencia",
                "estado",
                "resuelto_como",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    md_path = results_dir / "verificacion_rutas_enlaces.md"
    with md_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# Verificación de rutas y enlaces locales — D5\n\n")
        f.write(f"- Archivos de texto revisados: **{scanned_files}**\n")
        f.write(f"- Referencias locales inequívocas detectadas: **{len(rows)}**\n")
        f.write(f"- Referencias válidas: **{len(ok)}**\n")
        f.write(f"- Referencias faltantes / fuera del repositorio: **{len(missing)}**\n\n")

        if missing:
            f.write("## Referencias pendientes\n\n")
            f.write("| Archivo origen | Tipo | Referencia | Estado |\n")
            f.write("|---|---|---|---|\n")
            for r in missing:
                src = r["archivo_origen"].replace("|", "\\|")
                ref = r["referencia"].replace("|", "\\|")
                f.write(
                    f"| `{src}` | {r['tipo']} | `{ref}` | **{r['estado']}** |\n"
                )
            f.write(
                "\n> D5 no se cierra todavía. Deben revisarse estas referencias "
                "y volver a ejecutar el verificador.\n"
            )
        else:
            f.write("## Resultado\n\n")
            f.write(
                "**0 referencias locales faltantes detectadas dentro del alcance "
                "del verificador.**\n\n"
            )

        f.write("\n## Alcance del verificador\n\n")
        f.write(
            "Se comprueban enlaces Markdown, referencias Markdown, atributos "
            "`href/src` de HTML, `url()` de CSS, referencias LaTeX "
            "(`includegraphics`, `input`, `include`, `bibliography`, "
            "`addbibresource`) y rutas inequívocas entre backticks que comienzan "
            "por una carpeta/archivo real del nivel raíz o por `./`/`../`.\n\n"
        )
        f.write(
            "No se contabilizan como rutas los DOI, URLs externas, versiones, "
            "comandos, comodines ni nombres sueltos como `index.html` o "
            "`diccionario_datos.csv`, porque pueden ser menciones contextuales "
            "y no enlaces navegables.\n"
        )

    print("=" * 72)
    print("D5 — VERIFICACIÓN CONSERVADORA DE RUTAS/ENLACES — V3")
    print("=" * 72)
    print(f"Raíz: {root}")
    print(f"Archivos revisados: {scanned_files}")
    print(f"Referencias inequívocas: {len(rows)}")
    print(f"OK: {len(ok)}")
    print(f"FALTANTES/FUERA_REPO: {len(missing)}")
    print(f"CSV: {csv_path.relative_to(root)}")
    print(f"Reporte: {md_path.relative_to(root)}")

    if missing:
        print("\nPRIMERAS REFERENCIAS PENDIENTES:")
        for r in missing[:30]:
            print(
                f"- {r['archivo_origen']} -> {r['referencia']} "
                f"[{r['estado']}] ({r['tipo']})"
            )
        return 1

    print("\nRESULTADO: 0 referencias faltantes dentro del alcance definido.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
