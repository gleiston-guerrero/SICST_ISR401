"""
02_limpiar_datos.py

Genera datos_procesados/respuestas_cuestionario_procesadas.csv a partir de
los datos crudos: elimina la columna de fecha/hora (para reducir
información temporal innecesaria en los datos derivados), recorta espacios
en blanco, normaliza los códigos de participante y descarta filas
completamente vacías.

H2:
- conserva los datos crudos sin sobrescribirlos;
- elimina espacios al inicio/final de todos los campos;
- normaliza el prefijo histórico `EVA2-PAC-12` a `EV2-PAC-12`;
- valida que todos los códigos procesados tengan el formato
  `EV2-PAC-##` o `EV2-ENT-##`.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "07_Datos" / "datos_crudos" / "respuestas_cuestionario_2B.csv"
PROCESSED = ROOT / "07_Datos" / "datos_procesados" / "respuestas_cuestionario_procesadas.csv"

PATRON_CODIGO = re.compile(r"^EV2-(?:PAC|ENT)-\d{2}$")


def normalizar_codigo(codigo):
    codigo = codigo.strip()

    # Error de prefijo presente en la exportación original.
    if codigo == "EVA2-PAC-12":
        return "EV2-PAC-12"

    return codigo


def main():
    with open(RAW, "r", encoding="utf-8-sig", newline="") as f:
        filas = list(csv.reader(f))

    encabezado = [c.strip() for c in filas[0]]
    datos = [f for f in filas[1:] if any(c.strip() for c in f)]

    datos_limpios = []
    for fila in datos:
        limpia = [c.strip() for c in fila]

        # En los datos crudos la columna 0 es fecha/hora y la columna 2
        # contiene el código del participante.
        if len(limpia) > 2:
            limpia[2] = normalizar_codigo(limpia[2])

            if not PATRON_CODIGO.fullmatch(limpia[2]):
                raise ValueError(
                    f"Código de participante no normalizado: {limpia[2]!r}"
                )

        datos_limpios.append(limpia)

    # La primera columna es fecha/hora de respuesta; se excluye de la
    # versión procesada. Los datos crudos se preservan sin modificación.
    encabezado_procesado = encabezado[1:]
    datos_procesados = [fila[1:] for fila in datos_limpios]

    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(encabezado_procesado)
        writer.writerows(datos_procesados)

    print(f"OK: {PROCESSED.relative_to(ROOT)} ({len(datos_procesados)} filas)")


if __name__ == "__main__":
    main()
