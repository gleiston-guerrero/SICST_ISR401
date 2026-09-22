# Verificación literal de la codificación — C1

## Alcance

Se revisó la matriz vigente `matriz_codificacion_SICST.csv` frente a las transcripciones disponibles y las definiciones de `libro_codigos.csv`.

Criterio aplicado:

- una asignación `1` se conserva únicamente cuando existe una cita literal suficiente que respalda la definición vigente del subtema;
- una asignación sin respaldo literal suficiente se cambia a `0`;
- una asignación previamente en `0` puede cambiar a `1` cuando se identifica evidencia literal suficiente;
- no se crean respuestas, participantes ni citas.

## Resultado

- Filas de la matriz verificadas: **18**
- Subtemas disponibles: **17**
- Asignaciones positivas finales con cita: **203**
- Asignaciones `1 → 0` retiradas por falta de cita suficiente: **65**
- Asignaciones `0 → 1` incorporadas por evidencia literal suficiente: **8**
- Citas consolidadas: **203**

Las citas verificables se encuentran en:

`citas_codificacion.csv`

El detalle de todos los cambios se encuentra en:

`cambios_codificacion_C1.csv`

## Sincronización de saturación

Como la matriz cambió durante C1, se regeneraron también:

- `saturacion_actualizada.csv`
- `curva_saturacion_SICST.png`

Se mantuvo el orden cronológico documentado de las 16 entrevistas del corpus principal y se excluyeron las filas `WALK` del cálculo, igual que en el script versionado.

El resultado final acumula **17 subtemas**.

## Nota sobre WALK

`WALK-NTEC-01` y `WALK-TEC-01` permanecen en la matriz como evidencia complementaria, pero no forman parte del cálculo de saturación del corpus principal.

## Nota de integridad

Esta revisión valida respaldo textual dentro de las transcripciones disponibles. No sustituye la verificación auditiva pendiente de B1/B3 ni convierte una transcripción no cotejada palabra por palabra con su audio en evidencia auditiva verificada.

## Verificación automatizada final

El 21/09/2026 se incorporó y ejecutó el script
`verificar_citas_codificacion.py` sobre la matriz y las transcripciones
vigentes.

La verificación automática obtuvo:

- filas de matriz: **18**;
- subtemas: **17**;
- asignaciones positivas en la matriz: **203**;
- citas registradas: **203**;
- citas literales verificadas: **203**;
- positivos sin cita: **0**;
- citas sobrantes: **0**;
- fallos totales: **0**.

Cada fila positiva de `matriz_codificacion_SICST.csv` tiene una cita literal
verificable en `citas_codificacion.csv`, junto con el archivo fuente y la
línea o rango de líneas correspondiente.

El script comprueba automáticamente:

1. que los valores de la matriz sean `0` o `1`;
2. que cada asignación positiva tenga exactamente una cita;
3. que no existan citas correspondientes a valores `0`;
4. que el archivo fuente exista;
5. que la cita aparezca literalmente en la transcripción indicada;
6. que la línea o rango de líneas registrado corresponda con la ubicación
   real de la cita.

Resultado final de la ejecución:

`RESULTADO C1: OK — 0 FALLOS`

