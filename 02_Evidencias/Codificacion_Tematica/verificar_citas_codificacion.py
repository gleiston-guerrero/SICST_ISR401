import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BASE = ROOT / "02_Evidencias" / "Codificacion_Tematica"

MATRIZ = BASE / "matriz_codificacion_SICST.csv"
CITAS = BASE / "citas_codificacion.csv"


def leer_csv(ruta):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f)
        return list(lector), lector.fieldnames or []


def linea_de_posicion(texto, posicion):
    return texto.count("\n", 0, posicion) + 1


def parsear_linea(valor):
    valor = valor.strip()

    if re.fullmatch(r"\d+", valor):
        n = int(valor)
        return n, n

    m = re.fullmatch(r"(\d+)-(\d+)", valor)

    if not m:
        return None

    inicio = int(m.group(1))
    fin = int(m.group(2))

    if inicio > fin:
        return None

    return inicio, fin


errores = []

# ------------------------------------------------------------
# 1. Leer matriz
# ------------------------------------------------------------

matriz, columnas_matriz = leer_csv(MATRIZ)

if "codigo" not in columnas_matriz:
    print("ERROR: la matriz no contiene columna 'codigo'.")
    sys.exit(1)

subtemas = [
    c for c in columnas_matriz
    if c != "codigo"
]

positivos = set()

for fila in matriz:
    participante = fila["codigo"].strip()

    for subtema in subtemas:
        valor = fila[subtema].strip()

        if valor not in {"0", "1"}:
            errores.append(
                f"Matriz: valor inválido {participante} "
                f"{subtema}={valor}"
            )

        if valor == "1":
            positivos.add(
                (participante, subtema)
            )

# ------------------------------------------------------------
# 2. Leer citas
# ------------------------------------------------------------

citas, columnas_citas = leer_csv(CITAS)

columnas_requeridas = {
    "codigo_participante",
    "codigo_subtema",
    "subtema",
    "valor",
    "cita_literal",
    "archivo_fuente",
    "linea",
    "criterio",
}

faltan_columnas = (
    columnas_requeridas - set(columnas_citas)
)

if faltan_columnas:
    errores.append(
        "Faltan columnas en citas_codificacion.csv: "
        + ", ".join(sorted(faltan_columnas))
    )

claves_citas = []
claves_unicas = set()

for numero_fila, fila in enumerate(
    citas,
    start=2
):
    participante = (
        fila["codigo_participante"].strip()
    )

    subtema = (
        fila["codigo_subtema"].strip()
    )

    clave = (participante, subtema)

    claves_citas.append(clave)

    if clave in claves_unicas:
        errores.append(
            f"Fila {numero_fila}: cita duplicada "
            f"para {participante} {subtema}"
        )

    claves_unicas.add(clave)

    if fila["valor"].strip() != "1":
        errores.append(
            f"Fila {numero_fila}: valor distinto de 1 "
            f"para {participante} {subtema}"
        )

# ------------------------------------------------------------
# 3. Cobertura matriz ↔ citas
# ------------------------------------------------------------

faltantes = sorted(
    positivos - claves_unicas
)

sobrantes = sorted(
    claves_unicas - positivos
)

for clave in faltantes:
    errores.append(
        f"Falta cita para positivo de matriz: "
        f"{clave[0]} {clave[1]}"
    )

for clave in sobrantes:
    errores.append(
        f"Existe cita sin positivo en matriz: "
        f"{clave[0]} {clave[1]}"
    )

# ------------------------------------------------------------
# 4. Verificación literal y de líneas
# ------------------------------------------------------------

citas_verificadas = 0

for numero_fila, fila in enumerate(
    citas,
    start=2
):
    participante = (
        fila["codigo_participante"].strip()
    )

    subtema = (
        fila["codigo_subtema"].strip()
    )

    cita = fila["cita_literal"]

    fuente = (
        fila["archivo_fuente"].strip()
    )

    ubicacion = (
        fila["linea"].strip()
    )

    ruta = ROOT / fuente

    if not ruta.exists():
        errores.append(
            f"Fila {numero_fila}: archivo inexistente "
            f"{fuente}"
        )
        continue

    if not cita:
        errores.append(
            f"Fila {numero_fila}: cita vacía "
            f"{participante} {subtema}"
        )
        continue

    rango_guardado = parsear_linea(
        ubicacion
    )

    if rango_guardado is None:
        errores.append(
            f"Fila {numero_fila}: ubicación de línea "
            f"inválida '{ubicacion}'"
        )
        continue

    texto = ruta.read_text(
        encoding="utf-8-sig",
        errors="replace"
    )

    posiciones = []

    inicio_busqueda = 0

    while True:
        pos = texto.find(
            cita,
            inicio_busqueda
        )

        if pos < 0:
            break

        posiciones.append(pos)

        inicio_busqueda = pos + 1

    if not posiciones:
        errores.append(
            f"Fila {numero_fila}: cita NO literal "
            f"{participante} {subtema}"
        )
        continue

    ubicacion_correcta = False

    for pos in posiciones:
        linea_inicio = linea_de_posicion(
            texto,
            pos
        )

        linea_fin = linea_de_posicion(
            texto,
            pos + len(cita) - 1
        )

        if (
            linea_inicio,
            linea_fin
        ) == rango_guardado:
            ubicacion_correcta = True
            break

    if not ubicacion_correcta:
        errores.append(
            f"Fila {numero_fila}: línea incorrecta "
            f"{participante} {subtema} "
            f"(registrada {ubicacion})"
        )
        continue

    citas_verificadas += 1

# ------------------------------------------------------------
# 5. Resultado
# ------------------------------------------------------------

print("=" * 72)
print("VERIFICACIÓN AUTOMÁTICA C1")
print("=" * 72)

print(
    f"Filas de matriz            : {len(matriz)}"
)

print(
    f"Subtemas                   : {len(subtemas)}"
)

print(
    f"Positivos en matriz        : {len(positivos)}"
)

print(
    f"Citas registradas          : {len(citas)}"
)

print(
    f"Citas literales verificadas: {citas_verificadas}"
)

print(
    f"Positivos sin cita         : {len(faltantes)}"
)

print(
    f"Citas sobrantes            : {len(sobrantes)}"
)

print(
    f"Fallos totales             : {len(errores)}"
)

print("=" * 72)

if errores:
    print()
    print("DETALLE DE FALLOS:")
    print()

    for error in errores:
        print("-", error)

    print()
    print("RESULTADO C1: FALLÓ")
    sys.exit(1)

print("RESULTADO C1: OK — 0 FALLOS")
sys.exit(0)
