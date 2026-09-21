#!/usr/bin/env python3
"""
D5 — Verificador de rutas/enlaces locales del repositorio SICST.

Uso desde la raíz del repositorio:
    python 07_Datos/scripts/verificar_rutas_enlaces.py

Genera:
    07_Datos/resultados/verificacion_rutas_enlaces.csv
    07_Datos/resultados/verificacion_rutas_enlaces.md

Código de salida:
    0 = no se detectaron referencias locales faltantes
    1 = se detectaron referencias locales faltantes
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

IGNORE_PREFIXES = (
    "http://", "https://", "mailto:", "tel:", "data:", "javascript:",
    "#", "//"
)

PLACEHOLDER_HINTS = (
    "<", ">", "{", "}", "*", "$(", "${", "PENDIENTE", "EJEMPLO",
    "ruta/", "path/", "archivo.ext", "example/"
)

COMMON_FILE_EXTENSIONS = {
    ".md", ".pdf", ".tex", ".bib", ".csv", ".xlsx", ".xls", ".docx",
    ".doc", ".txt", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
    ".mp3", ".mp4", ".wav", ".7z", ".zip", ".json", ".py", ".html",
    ".css", ".js", ".drawio", ".sha256"
}

MD_LINK_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
HTML_LINK_RE = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.I)
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
    if (cwd / "07_Datos").exists():
        return cwd
    return candidate

def clean_target(raw: str) -> str:
    s = html.unescape(raw.strip())
    if " " in s and not s.startswith("<"):
        s = re.sub(r'\s+["\'][^"\']*["\']\s*$', "", s)
    s = s.strip("<>").strip()
    s = unquote(s)
    s = s.split("#", 1)[0].split("?", 1)[0].strip()
    return s

def looks_local_path(value: str) -> bool:
    if not value:
        return False
    low = value.lower()
    if low.startswith(IGNORE_PREFIXES):
        return False
    if value.startswith("\\\\"):
        return False
    if re.match(r"^[A-Za-z]:[\\/]", value):
        return False
    if any(h in value for h in PLACEHOLDER_HINTS):
        return False
    if "\n" in value or len(value) > 260:
        return False
    if value.startswith(("git ", "python ", "py ", "pip ", "npm ", "npx ",
                         "pdflatex ", "ffprobe ", "ffmpeg ")):
        return False

    suffix = Path(value).suffix.lower()
    if "/" in value or "\\" in value:
        return True
    if suffix in COMMON_FILE_EXTENSIONS:
        return True
    return False

def candidate_paths(root: Path, source: Path, raw_target: str, kind: str):
    t = clean_target(raw_target)
    if not looks_local_path(t):
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

    valid_candidates = [p for p in candidates if is_within_repo(root, p)]
    if not valid_candidates:
        return {
            "archivo_origen": source.relative_to(root).as_posix(),
            "tipo": kind,
            "referencia": cleaned,
            "estado": "FUERA_REPO",
            "resuelto_como": ""
        }

    for p in valid_candidates:
        if p.exists():
            return {
                "archivo_origen": source.relative_to(root).as_posix(),
                "tipo": kind,
                "referencia": cleaned,
                "estado": "OK",
                "resuelto_como": p.relative_to(root).as_posix()
            }

    return {
        "archivo_origen": source.relative_to(root).as_posix(),
        "tipo": kind,
        "referencia": cleaned,
        "estado": "FALTANTE",
        "resuelto_como": ""
    }

def extract_refs(text: str):
    refs = []
    for m in MD_LINK_RE.finditer(text):
        refs.append(("markdown", m.group(1)))
    for m in HTML_LINK_RE.finditer(text):
        refs.append(("html", m.group(1)))
    for m in LATEX_RE.finditer(text):
        refs.append(("latex", m.group(1)))
    for m in BACKTICK_RE.finditer(text):
        refs.append(("backtick", m.group(1)))
    return refs

def main() -> int:
    root = repo_root_from_script()
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
        for kind, target in extract_refs(text):
            key = (kind, target)
            if key in seen_in_file:
                continue
            seen_in_file.add(key)
            result = check_one(root, path, target, kind)
            if result:
                rows.append(result)

    dedup = []
    seen = set()
    for r in rows:
        key = (r["archivo_origen"], r["tipo"], r["referencia"], r["estado"])
        if key not in seen:
            seen.add(key)
            dedup.append(r)
    rows = dedup

    missing = [r for r in rows if r["estado"] in {"FALTANTE", "FUERA_REPO"}]
    ok = [r for r in rows if r["estado"] == "OK"]

    csv_path = results_dir / "verificacion_rutas_enlaces.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["archivo_origen", "tipo", "referencia", "estado", "resuelto_como"]
        )
        writer.writeheader()
        writer.writerows(rows)

    md_path = results_dir / "verificacion_rutas_enlaces.md"
    with md_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# Verificación de rutas y enlaces locales — D5\n\n")
        f.write(f"- Archivos de texto revisados: **{scanned_files}**\n")
        f.write(f"- Referencias locales detectadas: **{len(rows)}**\n")
        f.write(f"- Referencias válidas: **{len(ok)}**\n")
        f.write(f"- Referencias faltantes / fuera del repositorio: **{len(missing)}**\n\n")

        if missing:
            f.write("## Referencias pendientes\n\n")
            f.write("| Archivo origen | Tipo | Referencia | Estado |\n")
            f.write("|---|---|---|---|\n")
            for r in missing:
                src = r["archivo_origen"].replace("|", "\\|")
                ref = r["referencia"].replace("|", "\\|")
                f.write(f"| `{src}` | {r['tipo']} | `{ref}` | **{r['estado']}** |\n")
            f.write("\n> D5 no puede cerrarse todavía. Deben corregirse estas referencias y volver a ejecutar el verificador.\n")
        else:
            f.write("## Resultado\n\n")
            f.write("**0 referencias locales faltantes detectadas por el verificador.**\n\n")
            f.write("D5 puede documentarse como verificado para el alcance de este script.\n")

        f.write("\n## Alcance\n\n")
        f.write(
            "El verificador revisa enlaces Markdown, atributos `href/src` de HTML, "
            "referencias LaTeX (`includegraphics`, `input`, `include`, `bibliography`, "
            "`addbibresource`) y rutas locales escritas entre backticks. "
            "Ignora URLs externas, anclas, comandos y marcadores evidentes.\n"
        )

    print("=" * 72)
    print("D5 — VERIFICACIÓN DE RUTAS/ENLACES")
    print("=" * 72)
    print(f"Raíz: {root}")
    print(f"Archivos revisados: {scanned_files}")
    print(f"Referencias locales: {len(rows)}")
    print(f"OK: {len(ok)}")
    print(f"FALTANTES/FUERA_REPO: {len(missing)}")
    print(f"CSV: {csv_path.relative_to(root)}")
    print(f"Reporte: {md_path.relative_to(root)}")

    if missing:
        print("\nPRIMERAS REFERENCIAS PENDIENTES:")
        for r in missing[:20]:
            print(f"- {r['archivo_origen']} -> {r['referencia']} [{r['estado']}]")
        return 1

    print("\nRESULTADO: 0 referencias faltantes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
