# Dataset reproducible SICST — Zenodo

## Descripción

Este documento describe el depósito de datos del proyecto **Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)** y conserva la referencia al repositorio reproducible vigente.

El depósito Zenodo versión 1.0 fue publicado el 05/09/2026. El repositorio GitHub ha recibido correcciones y artefactos posteriores, por lo que ambos estados deben distinguirse.

## Autores

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul (ORCID: 0009-0006-0056-8482)

## Publicación

- DOI: `10.5281/zenodo.22315298`
- URL DOI: `https://doi.org/10.5281/zenodo.22315298`
- Zenodo: `https://zenodo.org/records/22315298`
- Versión: `1.0`
- Fecha de publicación: `2026-09-05`
- Acceso: Público / Open

## Registro del protocolo experimental en OSF

- DOI: `10.17605/OSF.IO/82Q76`
- URL DOI: `https://doi.org/10.17605/OSF.IO/82Q76`
- Fecha y hora UTC registrada en la evidencia del proyecto: `2026-09-13T00:50:38Z`
- Fecha y hora Ecuador continental: `2026-09-12 19:50:38`

El registro OSF se documenta en el proyecto como un registro retrospectivo del protocolo y no como una prerregistración confirmatoria anterior a la generación de los datos experimentales.

## Archivos verificados del registro Zenodo

La lista pública de Zenodo fue verificada el 21/09/2026 y muestra exactamente cuatro archivos de nivel superior:

1. `CITATION_FINAL.cff` — 1.3 kB.
2. `LICENSE-DATA_FINAL.txt` — 2.2 kB.
3. `README_PUBLICACION_FINAL.md` — 1.8 kB.
4. `SICST_Dataset_Reproducible_v1.0_Zenodo_FINAL.zip` — 16.5 kB.

Tamaño total mostrado por Zenodo: aproximadamente `21.8 kB`.

## Aclaración sobre el contenido del depósito

Versiones anteriores de la documentación del repositorio describían el depósito como si incluyera directamente artefactos actuales del experimento comparativo humano–LLM, entre ellos:

- `prompt_generacion_RF_llm.md`;
- `matriz_trazabilidad_tema_RF.csv`;
- `analisis_experimento_llm_humano.py`.

La lista pública del registro Zenodo no muestra esos archivos como elementos independientes. Por ello, esta documentación ya no afirma que formen parte del depósito como archivos separados.

El depósito sí contiene `SICST_Dataset_Reproducible_v1.0_Zenodo_FINAL.zip`. No se atribuye al ZIP un contenido interno que no haya sido verificado directamente contra la versión depositada.

## Fuente reproducible vigente

La versión actual del proyecto se encuentra en:

`https://github.com/gleiston-guerrero/SICST_ISR401`

### Cuestionario general

Los datos y materiales reproducibles vigentes se encuentran principalmente en:

`07_Datos/`

La cadena de reproducción declarada por el repositorio es:

```bash
python 07_Datos/scripts/orquestar.py
```

### Experimento comparativo humano–LLM

Los artefactos vigentes del experimento se encuentran principalmente en:

`06_Experimento/`

Entre ellos se documentan en el repositorio:

- `prompts_llm/prompt_generacion_RF_llm.md`
- `datos_crudos/`
- `datos_procesados/`
- `datos_procesados/matriz_trazabilidad_tema_RF.csv`
- `scripts_analisis/analisis_experimento_llm_humano.py`
- `resultados/`
- `registro_previo/`
- `osf_deviations.pdf`

La reproducción declarada del análisis experimental es:

```bash
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

Estas rutas describen el **repositorio vigente** y no deben interpretarse automáticamente como la lista de archivos del depósito histórico Zenodo v1.0.

## Integridad

Los hashes SHA-256 del cuestionario general se mantienen en:

`07_Datos/checksums_datos.sha256`

La existencia de esos hashes en el repositorio actual no implica que todos los archivos actuales estuvieran incluidos en el depósito del 05/09/2026.

## Privacidad

El paquete público no debe incluir identificadores directos, consentimientos firmados, firmas, rostros, audios ni videos identificables de participantes.

Los códigos de participante se mantienen para trazabilidad académica. La evidencia sensible se conserva separada de la capa pública del proyecto.

## Citación

Para el depósito Zenodo, consultar:

- DOI: `https://doi.org/10.5281/zenodo.22315298`
- archivo depositado `CITATION_FINAL.cff`

Para el código y materiales vigentes del proyecto, consultar el repositorio:

`https://github.com/gleiston-guerrero/SICST_ISR401`

## Trazabilidad temporal

Debe distinguirse entre:

- **Zenodo v1.0:** publicación del 05/09/2026;
- **OSF:** registro del protocolo el 12/09/2026 19:50:38 (Ecuador continental), equivalente a 13/09/2026 00:50:38 UTC;
- **repositorio vigente:** incluye correcciones y artefactos posteriores a ambas fechas.

Esta distinción evita atribuir retrospectivamente al depósito Zenodo archivos que solo están demostrados en versiones posteriores del repositorio.
