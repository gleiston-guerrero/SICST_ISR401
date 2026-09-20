# Instrumentos del experimento SICST — Enfoque 1

## Evaluación original con origen no indicado

`../datos_crudos/hoja_evaluacion_ciega.csv` contiene 66 `ITEM` sin una
columna que revele el origen humano/LLM.

Los cuatro evaluadores utilizaron la rúbrica definida en
`rubrica_evaluacion_requisitos.md`.

## Reconstrucción post-evaluación del origen

Después de la evaluación, el origen se reconstruye de forma determinista
comparando el texto de cada ITEM con:

- la matriz de trazabilidad para los RF humanos;
- `../datos_crudos/requisitos_llm.csv` para los 33 RF LLM completos.

La reconstrucción del origen se realiza de forma determinista con los
archivos versionados del experimento y no depende de un artefacto externo
de desciego.

El script valida que se reconstruyan exactamente 33 RF humanos y 33 RF LLM,
sin coincidencias faltantes ni ambiguas.
