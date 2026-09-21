# Notas de campo y correspondencia con transcripciones

Esta carpeta conserva notas, síntesis retrospectivas y archivos históricos asociados con las sesiones de elicitación y validación del proyecto SICST.

## Corrección F3 — fechas de notas

La revisión F3 detectó que ocho archivos de EFT, FAM y FIS tenían el prefijo histórico `2026-06-17` y estaban descritos como notas contemporáneas del 17/06/2026. Esa clasificación era incompatible con las fechas vigentes de las sesiones, realizadas en septiembre de 2026.

El prefijo `2026-06-17` de esos nombres de archivo se conserva únicamente como nombre histórico y **no debe interpretarse como fecha real de sesión ni de redacción**. La fuente tabular vigente para la fecha de sesión es `02_Evidencias/elegibilidad.csv`. La fecha de redacción declarada y su estado se documentan en `registro_elaboracion_notas.csv`.

### Fechas declaradas por el equipo

| Código | Fecha de sesión vigente | Fecha real de redacción declarada | Tratamiento F3 |
|---|---:|---:|---|
| EFT-01 | 06/09/2026 | 05/09/2026 | Archivo histórico/preparatorio; no válido como nota contemporánea de la sesión |
| EFT-02 | 06/09/2026 | 06/09/2026 | Fecha declarada coincidente con la sesión; incorporado a GitHub el 13/09 |
| EFT-03 | 06/09/2026 | 06/09/2026 | Fecha declarada coincidente con la sesión; incorporado a GitHub el 13/09 |
| FAM-01 | 07/09/2026 | 07/09/2026 | Fecha declarada coincidente con la sesión; incorporado a GitHub el 13/09 |
| FAM-02 | 07/09/2026 | 07/09/2026 | Fecha declarada coincidente con la sesión; incorporado a GitHub el 13/09 |
| FAM-03 | 07/09/2026 | 07/09/2026 | Fecha declarada coincidente con la sesión; incorporado a GitHub el 13/09 |
| FIS-01 | 07/09/2026 | 07/09/2026 | Fecha declarada coincidente con la sesión; incorporado a GitHub el 13/09 |
| FAM-04 | 17/09/2026 | No determinada | Archivo previo a la sesión y basado en contenido que no correspondía al audio; no válido como nota contemporánea |

La coincidencia entre una fecha de redacción declarada y la fecha de sesión no se presenta como prueba independiente de contemporaneidad cuando no existe metadato o evidencia adicional que lo demuestre.

## FAM-04

La entrevista real de `FAM-04` corresponde al 17/09/2026. El archivo histórico de nota con prefijo `2026-06-17` ya estaba incorporado al repositorio el 13/09/2026, por lo que no puede ser una nota tomada durante esa entrevista. Además, resumía una versión de transcripción que no correspondía al audio posteriormente revisado en B1.

Por tanto:

- no se utiliza como nota contemporánea;
- no se utiliza como respaldo del contenido de la entrevista vigente;
- se conserva únicamente como artefacto histórico para mantener trazabilidad;
- la entrevista FAM-04 queda documentada sin nota contemporánea válida.

## Síntesis retrospectivas

Las otras 22 hojas correspondientes a sesiones de julio y agosto fueron elaboradas el 17/09/2026 a partir de transcripciones previamente conservadas. Se mantienen expresamente clasificadas como **síntesis posteriores** y no como notas tomadas durante la sesión original.

## Estado documental después de F3

Dentro de los 30 archivos documentales históricamente relacionados con sesiones/jornadas:

- 6 tienen una fecha de redacción declarada por el equipo que coincide con la fecha de sesión;
- 22 son síntesis retrospectivas del 17/09/2026;
- 2 son archivos históricos que no se consideran notas contemporáneas válidas (`EFT-01` y `FAM-04`).

El repositorio no transforma una fecha declarada en evidencia independiente. Cuando esa evidencia no existe, la limitación se mantiene explícita.

## Fuentes de verificación

- Fechas vigentes de sesión y perfil: `../../02_Evidencias/elegibilidad.csv`
- Registro de elaboración y clasificación de notas: `registro_elaboracion_notas.csv`
- Correspondencia sesión–transcripción–nota: `../bitácora_sesiones/bitacora_elicitacion.csv`
- Transcripciones: `../../02_Evidencias/Transcripciones/`
- Corrección específica de FAM-04: `../../02_Evidencias/Transcripciones/verificacion_muestreo_FAM-04.md`

## Principio de integridad

No se cambian fechas para aparentar contemporaneidad. Cuando una fecha real de redacción es anterior o posterior a la sesión, se declara así y el documento se clasifica según corresponda. No se crea una nueva nota para reemplazar retrospectivamente una nota que no existió durante la sesión.
