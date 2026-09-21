# Corrección F3 — trazabilidad de fechas de notas de campo

Fecha de corrección: 21/09/2026.

## Problema identificado

El plan de mejora observó que ocho notas de EFT, FAM y FIS estaban registradas como contemporáneas del 17/06/2026, aunque las sesiones vigentes corresponden a septiembre de 2026. También señaló que la nota histórica de FAM-04 resumía una transcripción que no correspondía al audio.

## Corrección aplicada

Se separaron tres conceptos que antes estaban mezclados:

1. fecha real de la sesión;
2. fecha de redacción declarada de la nota;
3. fecha de incorporación al repositorio.

Las fechas de sesión se mantienen alineadas con `02_Evidencias/elegibilidad.csv`. Las fechas de redacción declaradas por el equipo se registran sin presentarlas como evidencia independiente cuando el repositorio no contiene metadatos suficientes para confirmarlas.

`EFT-01` se conserva como archivo histórico/preparatorio porque su fecha de redacción declarada (05/09/2026) es anterior a la sesión vigente (06/09/2026).

`FAM-04` queda sin nota contemporánea válida: el archivo histórico ya estaba en GitHub el 13/09/2026, antes de la entrevista real del 17/09/2026, y además resumía una versión de transcripción que no correspondía al audio revisado posteriormente.

## Resultado

No se mantiene ninguna sesión de EFT/FAM/FIS con la fecha ficticia 17/06/2026. No se crea evidencia retrospectiva para aparentar notas contemporáneas y se conserva la trazabilidad de los nombres históricos.

## Corrección posterior de EFT-02

Durante la revisión final del 21/09/2026, el equipo detectó que la fecha `06/09/2026` asignada previamente a `EFT-02` fue un error de digitación. La fecha correcta es `07/09/2026`, coherente con la hoja original de correspondencia conservada como `10_Autoria/correspondencia/2026-09-07_Entrevista_Estudiante_Fisioterapia_EFT-02_Peticion_Entrevista.jpeg`.

Se corrigieron las tablas documentales relacionadas sin modificar el contenido de la evidencia original.