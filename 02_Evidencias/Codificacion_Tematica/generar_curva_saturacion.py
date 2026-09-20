from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# CONFIGURACIÓN
# ============================================================

CARPETA = Path(__file__).resolve().parent

MATRIZ = CARPETA / "matriz_codificacion_SICST.csv"
SALIDA_CSV = CARPETA / "saturacion_actualizada.csv"
SALIDA_FIGURA = CARPETA / "curva_saturacion_SICST.png"

# Orden cronológico documentado actualmente para el corpus de entrevistas.
# Las sesiones WALK se excluyen del análisis de saturación.
ORDEN_CRONOLOGICO = [
    "EV2-PAC-01",
    "EV2-PAC-03",
    "EV2-PAC-04",
    "EV2-PAC-05",
    "EV2-PAC-06",
    "EV2-PAC-07",
    "EV2-PAC-08",
    "EV2-PAC-09",
    "EFT-01",
    "EFT-02",
    "EFT-03",
    "FAM-01",
    "FAM-02",
    "FAM-03",
    "FAM-04",
    "FIS-01",
]


def main():
    if not MATRIZ.exists():
        raise FileNotFoundError(
            f"No se encontró la matriz requerida: {MATRIZ}"
        )

    df = pd.read_csv(MATRIZ)

    if "codigo" not in df.columns:
        raise ValueError(
            "La matriz debe contener una columna llamada 'codigo'."
        )

    columnas_subtemas = [
        columna for columna in df.columns
        if columna.startswith("SUB-")
    ]

    if not columnas_subtemas:
        raise ValueError(
            "No se encontraron columnas de subtemas SUB-xx."
        )

    # Excluir walkthrough del análisis de saturación.
    entrevistas = df[
        ~df["codigo"].astype(str).str.startswith("WALK")
    ].copy()

    codigos_matriz = set(
        entrevistas["codigo"].astype(str)
    )
    codigos_orden = set(ORDEN_CRONOLOGICO)

    faltantes_en_orden = codigos_matriz - codigos_orden
    faltantes_en_matriz = codigos_orden - codigos_matriz

    if faltantes_en_orden or faltantes_en_matriz:
        raise ValueError(
            "El orden cronológico no coincide con el corpus actual. "
            f"Sin ordenar: {sorted(faltantes_en_orden)}. "
            f"No presentes en matriz: {sorted(faltantes_en_matriz)}."
        )

    entrevistas["codigo"] = pd.Categorical(
        entrevistas["codigo"],
        categories=ORDEN_CRONOLOGICO,
        ordered=True,
    )

    entrevistas = entrevistas.sort_values(
        "codigo"
    ).reset_index(drop=True)

    temas_vistos = set()
    filas_saturacion = []

    for indice, fila in entrevistas.iterrows():
        temas_presentes = {
            columna
            for columna in columnas_subtemas
            if int(fila[columna]) == 1
        }

        temas_nuevos = temas_presentes - temas_vistos
        temas_vistos.update(temas_presentes)

        filas_saturacion.append(
            {
                "orden": indice + 1,
                "participante": str(fila["codigo"]),
                "temas_nuevos": len(temas_nuevos),
                "temas_acumulados": len(temas_vistos),
            }
        )

    saturacion = pd.DataFrame(filas_saturacion)

    saturacion.to_csv(
        SALIDA_CSV,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    plt.figure(figsize=(10, 5))
    plt.plot(
        saturacion["orden"],
        saturacion["temas_acumulados"],
        marker="o",
    )
    plt.xticks(
        saturacion["orden"],
        saturacion["participante"],
        rotation=90,
    )
    plt.xlabel("Entrevista")
    plt.ylabel("Subtemas acumulados")
    plt.title("Curva de saturación temática — SICST")
    plt.tight_layout()
    plt.savefig(
        SALIDA_FIGURA,
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    print(f"Matriz leída: {MATRIZ.name}")
    print(f"Entrevistas analizadas: {len(saturacion)}")
    print("Walkthrough excluidos del cálculo de saturación.")
    print(
        f"Subtemas acumulados al final: "
        f"{saturacion['temas_acumulados'].iloc[-1]}"
    )
    print(f"CSV generado: {SALIDA_CSV.name}")
    print(f"Figura generada: {SALIDA_FIGURA.name}")


if __name__ == "__main__":
    main()
