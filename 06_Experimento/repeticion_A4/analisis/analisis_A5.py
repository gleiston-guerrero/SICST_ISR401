from pathlib import Path
import csv
import math
import os
import unicodedata
import warnings

import numpy as np
from openpyxl import load_workbook
from scipy.optimize import minimize_scalar
from scipy.stats import norm, multivariate_normal


# ============================================================
# CONFIGURACIÓN
# ============================================================

DIMENSIONES = [
    "Completitud",
    "Ausencia de ambigüedad",
    "Verificabilidad",
    "Corrección respecto a la fuente",
    "Consistencia interna",
]

SEMILLA = 20260918

# Número de remuestreos para IC 95 % del alfa ordinal.
# Por defecto se utilizan 1000 remuestreos.
# Puede modificarse temporalmente, por ejemplo:
# A5_BOOTSTRAP=2000 python analisis_A5.py
N_BOOTSTRAP = int(os.environ.get("A5_BOOTSTRAP", "1000"))

# Efecto mínimo detectable aproximado declarado
# para el análisis con 11 pares temáticos estrictos.
MDE_DZ_11_PARES = 0.94

CARPETA_SCRIPT = Path(__file__).resolve().parent
CARPETA_A4 = CARPETA_SCRIPT.parent
CARPETA_EVALUACIONES = CARPETA_A4 / "evaluaciones_completadas"

ARCHIVOS = [
    CARPETA_EVALUACIONES / "SICST_A4_Evaluador_01_COMPLETADO.xlsx",
    CARPETA_EVALUACIONES / "SICST_A4_Evaluador_02_COMPLETADO.xlsx",
    CARPETA_EVALUACIONES / "SICST_A4_Evaluador_03_COMPLETADO.xlsx",
]

SALIDA_CSV = CARPETA_SCRIPT / "resultados_fiabilidad_A5.csv"
SALIDA_MD = CARPETA_SCRIPT / "resultado_A5.md"


# ============================================================
# UTILIDADES
# ============================================================

def normalizar_texto(valor):
    if valor is None:
        return ""

    texto = str(valor).strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )

    return " ".join(texto.split())


def es_puntuacion(valor):
    if isinstance(valor, bool):
        return False

    try:
        numero = int(valor)
        return float(valor) == numero and 1 <= numero <= 5
    except (TypeError, ValueError):
        return False


# ============================================================
# LECTURA DE LOS EXCEL
# ============================================================

def leer_evaluacion(ruta):
    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo requerido: {ruta}"
        )

    wb = load_workbook(
        ruta,
        data_only=True,
        read_only=False
    )

    if "Evaluacion" not in wb.sheetnames:
        raise ValueError(
            f"{ruta.name}: no existe la hoja 'Evaluacion'."
        )

    ws = wb["Evaluacion"]

    claves = {
        normalizar_texto(d): d
        for d in DIMENSIONES
    }

    fila_cabecera = None
    columnas = {}

    # Localizar automáticamente la fila de encabezados.
    for fila in range(1, min(ws.max_row, 15) + 1):
        encontrados = {}

        for col in range(1, ws.max_column + 1):
            texto = normalizar_texto(
                ws.cell(fila, col).value
            )

            for clave, nombre in claves.items():
                if texto == clave:
                    encontrados[nombre] = col

        if len(encontrados) == len(DIMENSIONES):
            fila_cabecera = fila
            columnas = encontrados
            break

    if fila_cabecera is None:
        raise ValueError(
            f"{ruta.name}: no se pudieron localizar "
            "las cinco dimensiones."
        )

    filas_puntuaciones = []

    # Buscar las filas que realmente tienen
    # las cinco puntuaciones válidas de 1 a 5.
    for fila in range(fila_cabecera + 1, ws.max_row + 1):

        valores = [
            ws.cell(
                fila,
                columnas[dimension]
            ).value
            for dimension in DIMENSIONES
        ]

        if all(es_puntuacion(v) for v in valores):
            filas_puntuaciones.append(
                [int(v) for v in valores]
            )

        if len(filas_puntuaciones) == 66:
            break

    if len(filas_puntuaciones) != 66:
        raise ValueError(
            f"{ruta.name}: se esperaban 66 requisitos "
            f"completos, pero se encontraron "
            f"{len(filas_puntuaciones)}."
        )

    return np.asarray(
        filas_puntuaciones,
        dtype=float
    )


# ============================================================
# ICC(2,1) E ICC(2,k)
# Two-way random effects - absolute agreement
# ============================================================

def calcular_icc(matriz):
    """
    matriz:
        filas = requisitos
        columnas = evaluadores

    ICC(2,1):
        acuerdo absoluto, efectos aleatorios,
        evaluador individual.

    ICC(2,k):
        acuerdo absoluto, efectos aleatorios,
        promedio de k evaluadores.
    """

    y = np.asarray(matriz, dtype=float)

    n, k = y.shape

    if n < 2 or k < 2:
        return np.nan, np.nan

    media_general = np.mean(y)
    medias_filas = np.mean(y, axis=1)
    medias_columnas = np.mean(y, axis=0)

    ss_filas = (
        k
        * np.sum(
            (medias_filas - media_general) ** 2
        )
    )

    ss_columnas = (
        n
        * np.sum(
            (medias_columnas - media_general) ** 2
        )
    )

    residuos = (
        y
        - medias_filas[:, None]
        - medias_columnas[None, :]
        + media_general
    )

    ss_error = np.sum(residuos ** 2)

    ms_filas = ss_filas / (n - 1)
    ms_columnas = ss_columnas / (k - 1)
    ms_error = ss_error / (
        (n - 1) * (k - 1)
    )

    denominador_21 = (
        ms_filas
        + (k - 1) * ms_error
        + (
            k
            * (ms_columnas - ms_error)
            / n
        )
    )

    denominador_2k = (
        ms_filas
        + (
            (ms_columnas - ms_error)
            / n
        )
    )

    icc_21 = (
        (ms_filas - ms_error)
        / denominador_21
        if not math.isclose(denominador_21, 0)
        else np.nan
    )

    icc_2k = (
        (ms_filas - ms_error)
        / denominador_2k
        if not math.isclose(denominador_2k, 0)
        else np.nan
    )

    return float(icc_21), float(icc_2k)


# ============================================================
# KAPPA DE FLEISS
# ============================================================

def fleiss_kappa(matriz):
    """
    Cada fila es un requisito.
    Cada columna es un evaluador.
    Categorías posibles: 1, 2, 3, 4 y 5.
    """

    ratings = np.asarray(
        matriz,
        dtype=int
    )

    n_items, n_raters = ratings.shape

    conteos = np.zeros(
        (n_items, 5),
        dtype=float
    )

    for i in range(n_items):
        for valor in ratings[i]:
            conteos[i, valor - 1] += 1

    p_categoria = (
        conteos.sum(axis=0)
        / (n_items * n_raters)
    )

    p_e = np.sum(
        p_categoria ** 2
    )

    p_item = (
        np.sum(
            conteos ** 2,
            axis=1
        )
        - n_raters
    ) / (
        n_raters
        * (n_raters - 1)
    )

    p_barra = np.mean(
        p_item
    )

    if math.isclose(1 - p_e, 0):
        return np.nan

    return float(
        (p_barra - p_e)
        / (1 - p_e)
    )


# ============================================================
# CORRELACIÓN POLICÓRICA
# ============================================================

def limites_latentes(valores):
    valores = np.asarray(
        valores,
        dtype=int
    )

    n = len(valores)

    acumuladas = []

    for categoria in range(1, 5):
        p = (
            np.sum(valores <= categoria)
            / n
        )

        p = np.clip(
            p,
            1e-6,
            1 - 1e-6
        )

        acumuladas.append(
            norm.ppf(p)
        )

    return np.asarray(
        [-np.inf]
        + acumuladas
        + [np.inf],
        dtype=float
    )


def tabla_contingencia(x, y):
    tabla = np.zeros(
        (5, 5),
        dtype=float
    )

    for a, b in zip(x, y):
        tabla[
            int(a) - 1,
            int(b) - 1
        ] += 1

    return tabla


def matriz_cdf(lim_x, lim_y, rho):
    """
    Calcula F(x,y) para todas las combinaciones
    de límites usando una distribución normal
    bivariada.
    """

    salida = np.zeros(
        (
            len(lim_x),
            len(lim_y)
        ),
        dtype=float
    )

    puntos = []
    posiciones = []

    for i, x in enumerate(lim_x):
        for j, y in enumerate(lim_y):

            if np.isneginf(x) or np.isneginf(y):
                salida[i, j] = 0.0

            elif np.isposinf(x) and np.isposinf(y):
                salida[i, j] = 1.0

            elif np.isposinf(x):
                salida[i, j] = norm.cdf(y)

            elif np.isposinf(y):
                salida[i, j] = norm.cdf(x)

            else:
                puntos.append([x, y])
                posiciones.append((i, j))

    if puntos:
        valores = multivariate_normal.cdf(
            np.asarray(puntos),
            mean=[0.0, 0.0],
            cov=[
                [1.0, rho],
                [rho, 1.0],
            ],
        )

        valores = np.atleast_1d(
            valores
        )

        for pos, valor in zip(
            posiciones,
            valores
        ):
            salida[pos] = float(valor)

    return salida


def probabilidades_celdas(lim_x, lim_y, rho):
    f = matriz_cdf(
        lim_x,
        lim_y,
        rho
    )

    probs = np.zeros(
        (5, 5),
        dtype=float
    )

    for i in range(5):
        for j in range(5):
            probs[i, j] = (
                f[i + 1, j + 1]
                - f[i, j + 1]
                - f[i + 1, j]
                + f[i, j]
            )

    return np.clip(
        probs,
        1e-12,
        1.0
    )


def correlacion_policorica(x, y):
    x = np.asarray(
        x,
        dtype=int
    )

    y = np.asarray(
        y,
        dtype=int
    )

    if len(np.unique(x)) < 2:
        return np.nan

    if len(np.unique(y)) < 2:
        return np.nan

    lim_x = limites_latentes(x)
    lim_y = limites_latentes(y)

    tabla = tabla_contingencia(
        x,
        y
    )

    def negativo_log_verosimilitud(rho):
        probs = probabilidades_celdas(
            lim_x,
            lim_y,
            rho
        )

        return -float(
            np.sum(
                tabla
                * np.log(probs)
            )
        )

    resultado = minimize_scalar(
        negativo_log_verosimilitud,
        bounds=(-0.98, 0.98),
        method="bounded",
        options={
            "xatol": 1e-4
        },
    )

    if not resultado.success:
        return np.nan

    return float(
        resultado.x
    )


# ============================================================
# ALFA ORDINAL
# ============================================================

def alfa_ordinal(matriz):
    """
    Alfa ordinal estandarizado calculado
    a partir de la matriz de correlaciones
    policóricas entre evaluadores.
    """

    x = np.asarray(
        matriz,
        dtype=int
    )

    k = x.shape[1]

    if k < 2:
        return np.nan

    r = np.eye(
        k,
        dtype=float
    )

    for i in range(k):
        for j in range(i + 1, k):

            rho = correlacion_policorica(
                x[:, i],
                x[:, j]
            )

            if not np.isfinite(rho):
                return np.nan

            r[i, j] = rho
            r[j, i] = rho

    suma = np.sum(r)

    if math.isclose(
        suma,
        0
    ):
        return np.nan

    alpha = (
        k / (k - 1)
    ) * (
        1
        - (k / suma)
    )

    return float(alpha)


def intervalo_bootstrap_alfa(
    matriz,
    n_bootstrap=N_BOOTSTRAP,
    semilla=SEMILLA,
):
    """
    Intervalo de confianza percentil del 95 %
    para alfa ordinal mediante remuestreo
    bootstrap de los requisitos.
    """

    rng = np.random.default_rng(
        semilla
    )

    x = np.asarray(
        matriz,
        dtype=int
    )

    n = x.shape[0]

    valores = []

    for _ in range(n_bootstrap):

        indices = rng.integers(
            0,
            n,
            size=n
        )

        muestra = x[
            indices,
            :
        ]

        try:
            alpha = alfa_ordinal(
                muestra
            )

            if np.isfinite(alpha):
                valores.append(alpha)

        except Exception:
            continue

    if len(valores) < 20:
        return (
            np.nan,
            np.nan,
            len(valores)
        )

    inferior, superior = np.percentile(
        valores,
        [2.5, 97.5]
    )

    return (
        float(inferior),
        float(superior),
        len(valores),
    )


# ============================================================
# FORMATO
# ============================================================

def fmt(valor):
    if not np.isfinite(valor):
        return "NA"

    return f"{valor:.3f}"


# ============================================================
# ANÁLISIS PRINCIPAL
# ============================================================

def main():
    warnings.filterwarnings(
        "ignore"
    )

    print(
        "Leyendo evaluaciones..."
    )

    evaluaciones = []

    for archivo in ARCHIVOS:
        matriz = leer_evaluacion(
            archivo
        )

        evaluaciones.append(
            matriz
        )

        print(
            f"OK: {archivo.name} "
            f"({matriz.shape[0]} requisitos)"
        )

    # Forma:
    # evaluador × requisito × dimensión
    evaluaciones = np.stack(
        evaluaciones,
        axis=0
    )

    resultados = []

    print()
    print(
        "Calculando fiabilidad..."
    )

    for indice, dimension in enumerate(
        DIMENSIONES
    ):

        # Forma:
        # requisitos × evaluadores
        matriz = evaluaciones[
            :,
            :,
            indice
        ].T

        icc_21, icc_2k = calcular_icc(
            matriz
        )

        kappa = fleiss_kappa(
            matriz
        )

        print(
            f"{dimension}: "
            "calculando alfa ordinal..."
        )

        alpha = alfa_ordinal(
            matriz
        )

        (
            ci_low,
            ci_high,
            boot_validos,
        ) = intervalo_bootstrap_alfa(
            matriz,
            n_bootstrap=N_BOOTSTRAP,
            semilla=(
                SEMILLA
                + indice
            ),
        )

        resultados.append({
            "dimension": dimension,
            "n_requisitos": 66,
            "n_evaluadores": 3,
            "ICC_2_1": icc_21,
            "ICC_2_k": icc_2k,
            "alfa_ordinal": alpha,
            "alfa_ordinal_IC95_inf": ci_low,
            "alfa_ordinal_IC95_sup": ci_high,
            "bootstrap_validos": boot_validos,
            "fleiss_kappa": kappa,
            "MDE_dz_11_pares_aprox": MDE_DZ_11_PARES,
            "alcance": "exploratorio",
        })

    # ========================================================
    # CSV
    # ========================================================

    campos = list(
        resultados[0].keys()
    )

    with open(
        SALIDA_CSV,
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as f:

        escritor = csv.DictWriter(
            f,
            fieldnames=campos
        )

        escritor.writeheader()

        for fila in resultados:
            fila_salida = {}

            for clave, valor in fila.items():

                if isinstance(
                    valor,
                    (float, np.floating)
                ):
                    fila_salida[clave] = (
                        ""
                        if not np.isfinite(valor)
                        else f"{valor:.6f}"
                    )

                else:
                    fila_salida[clave] = valor

            escritor.writerow(
                fila_salida
            )

    # ========================================================
    # INFORME MARKDOWN
    # ========================================================

    lineas = [
        "# Resultado A5 — fiabilidad y potencia exploratoria",
        "",
        "## Datos analizados",
        "",
        "- 66 requisitos funcionales.",
        "- 3 evaluadores nuevos.",
        "- 5 dimensiones puntuadas de 1 a 5.",
        "- 330 puntuaciones por evaluador.",
        "- 990 puntuaciones en total.",
        "",
        "## Métodos",
        "",
        "- ICC(2,1): modelo de dos vías, efectos aleatorios, acuerdo absoluto, evaluador individual.",
        "- ICC(2,k): modelo de dos vías, efectos aleatorios, acuerdo absoluto, promedio de los 3 evaluadores.",
        "- Alfa ordinal: calculado a partir de correlaciones policóricas entre evaluadores.",
        f"- IC 95 % del alfa ordinal: bootstrap con hasta {N_BOOTSTRAP} remuestreos por dimensión.",
        "- Kappa de Fleiss: acuerdo entre los 3 evaluadores sobre las cinco categorías de puntuación.",
        "",
        "## Resultados",
        "",
        "| Dimensión | ICC(2,1) | ICC(2,k) | Alfa ordinal | IC95% alfa | Fleiss κ |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for r in resultados:
        lineas.append(
            f"| {r['dimension']} "
            f"| {fmt(r['ICC_2_1'])} "
            f"| {fmt(r['ICC_2_k'])} "
            f"| {fmt(r['alfa_ordinal'])} "
            f"| [{fmt(r['alfa_ordinal_IC95_inf'])}, "
            f"{fmt(r['alfa_ordinal_IC95_sup'])}] "
            f"| {fmt(r['fleiss_kappa'])} |"
        )

    # ========================================================
    # INTERPRETACIÓN
    # ========================================================

    lineas.extend([
        "",
        "## Interpretación de la fiabilidad",
        "",
        "Los coeficientes obtenidos son cercanos a cero o negativos "
        "en la mayoría de las dimensiones. Esto indica que, en esta "
        "muestra, el grado de acuerdo entre los tres evaluadores fue bajo.",
        "",
        "Los valores negativos de ICC, alfa ordinal o kappa no se "
        "reemplazan por cero ni se modifican, ya que corresponden a "
        "los resultados producidos por las puntuaciones originales.",
        "",
        "Los intervalos de confianza del alfa ordinal son amplios e "
        "incluyen valores próximos a cero, por lo que las estimaciones "
        "de fiabilidad deben interpretarse con cautela.",
        "",
        "Estos resultados deben interpretarse considerando el número "
        "reducido de evaluadores y el carácter exploratorio del estudio. "
        "No se utilizan como evidencia de equivalencia entre los dos "
        "procedimientos.",
        "",
        "## Potencia y alcance inferencial",
        "",
        "El análisis comparativo utiliza 11 pares temáticos estrictos. "
        "Con ese tamaño efectivo, el efecto mínimo detectable declarado "
        "para la interpretación del estudio es aproximadamente "
        f"`dz ≈ {MDE_DZ_11_PARES:.2f}`.",
        "",
        "Por esta limitación de tamaño muestral, los resultados se "
        "interpretan como **exploratorios**.",
        "",
        "La ausencia de significancia estadística no debe interpretarse "
        "como demostración de equivalencia entre requisitos humanos y LLM.",
        "",
        "## Reproducibilidad",
        "",
        "Los resultados de este documento se generan automáticamente mediante:",
        "",
        "`06_Experimento/repeticion_A4/analisis/analisis_A5.py`",
        "",
        "a partir de las tres hojas originales almacenadas en:",
        "",
        "`06_Experimento/repeticion_A4/evaluaciones_completadas/`",
        "",
        "Las puntuaciones originales no se modifican durante el análisis.",
        "",
        f"El intervalo de confianza del alfa ordinal se genera con hasta "
        f"{N_BOOTSTRAP} remuestreos bootstrap por dimensión y semilla base "
        f"`{SEMILLA}`.",
        "",
    ])

    SALIDA_MD.write_text(
        "\n".join(lineas),
        encoding="utf-8"
    )

    # ========================================================
    # RESUMEN EN TERMINAL
    # ========================================================

    print()
    print("=" * 72)
    print("RESUMEN A5")
    print("=" * 72)

    for r in resultados:
        print(
            f"{r['dimension']}: "
            f"ICC(2,1)={fmt(r['ICC_2_1'])}, "
            f"ICC(2,k)={fmt(r['ICC_2_k'])}, "
            f"alfa={fmt(r['alfa_ordinal'])}, "
            f"kappa={fmt(r['fleiss_kappa'])}, "
            f"bootstrap válidos={r['bootstrap_validos']}"
        )

    print()
    print(
        f"Generado: {SALIDA_CSV}"
    )

    print(
        f"Generado: {SALIDA_MD}"
    )

    print()
    print(
        "A5 finalizado correctamente."
    )


if __name__ == "__main__":
    main()
