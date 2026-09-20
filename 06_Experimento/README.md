# Experimento SICST — Enfoque 1: calidad de RF humano vs. LLM

## Descripción

Este directorio contiene los artefactos del experimento comparativo del
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**,
registrado en OSF con DOI `10.17605/OSF.IO/82Q76`.

El estudio compara:

1. **33 RF humanos**, obtenidos durante el proceso normal de ingeniería de
   requisitos del SICST.
2. **33 RF generados por GPT-5.5-mini**, utilizando como corpus fuente las
   mismas transcripciones anonimizadas empleadas durante la elicitación.

Las entrevistas pertenecen a una etapa previa de levantamiento de requisitos.
Posteriormente, sus transcripciones anonimizadas se reutilizaron como corpus
fuente fijo para el brazo LLM.

## Pregunta de investigación

¿Existen diferencias significativas en la calidad de los requisitos
funcionales obtenidos mediante un proceso humano de ingeniería de requisitos
y aquellos generados mediante un modelo de lenguaje?

**H0:** No existen diferencias estadísticamente significativas.  
**H1:** Existen diferencias estadísticamente significativas.

## Registro OSF y cronología

- **OSF ID:** `82q76`
- **DOI:** `10.17605/OSF.IO/82Q76`
- **Fecha UTC:** `2026-09-13T00:50:38.265668Z`
- **Ecuador continental (UTC-5):** `2026-09-12 19:50:38`

Las entrevistas originales ya existían previamente como parte de la
elicitación de requisitos. Por tanto, el registro OSF no se presenta como
preregistro de la recolección de campo original.

El registro corresponde al experimento comparativo humano–LLM y a la fase
posterior de generación LLM, evaluación de requisitos y análisis. En la
documentación inicial esta evaluación fue descrita como “ciega”; sin embargo,
la revisión posterior de la relación de los evaluadores con el corpus no
permite sostener un cegamiento metodológico completo. En consecuencia,
el contraste inferencial se reporta con alcance **exploratorio**, no como una
prueba confirmatoria plenamente preregistrada.

La evidencia verificable se conserva en:

```text
registro_previo/
├── README.md
├── consulta.json
└── osf_registration.pdf
```

## Diseño experimental

El experimento considera:

- 66 RF evaluados en total;
- 33 RF humanos;
- 33 RF generados por LLM;
- 4 evaluadores;
- origen humano o LLM no indicado explícitamente en la hoja de evaluación;
- 5 dimensiones de calidad evaluadas mediante escala Likert de 1 a 5.

Las dimensiones evaluadas son:

- completitud;
- ausencia de ambigüedad;
- verificabilidad;
- corrección respecto a la fuente;
- consistencia interna.

El análisis estadístico incluye:

- κ de Fleiss por dimensión sobre los 66 ítems;
- análisis descriptivos por origen;
- 11 pares temáticos estrictos;
- Shapiro-Wilk sobre las diferencias de cada par;
- t de Student apareada o Wilcoxon de rangos con signo, según corresponda;
- corrección Holm-Bonferroni sobre las cinco dimensiones principales;
- diferencia media humano − LLM;
- IC bootstrap del 95 % de la diferencia media;
- Cohen's dz como tamaño del efecto para datos apareados;
- IC bootstrap del 95 % de Cohen's dz;
- 10 000 remuestreos bootstrap con semilla base 42.

## Relación de los evaluadores con el estudio y limitaciones de independencia

La revisión posterior de la procedencia de los evaluadores originales permitió
identificar que sus nombres coinciden con participantes previamente vinculados
al corpus y a actividades de levantamiento de información del proyecto,
correspondientes a:

- `EFT-01`
- `EFT-02`
- `EFT-03`
- `FAM-01`

Por esta razón, los cuatro evaluadores originales no se presentan como
evaluadores independientes o completamente ajenos al estudio.

La hoja de evaluación no mostraba explícitamente una columna que indicara el
origen humano o LLM de cada requisito. No obstante, esta ocultación de la
etiqueta de origen no constituye por sí sola evidencia suficiente de un
cegamiento metodológico completo, debido a la relación previa de los
evaluadores con el corpus y con actividades del proyecto.

Esta aclaración no elimina ni sustituye la evidencia del procedimiento
original. Los archivos, hojas, resultados y registros históricos se conservan
para mantener la trazabilidad del experimento tal como fue ejecutado.

La limitación se documenta retrospectivamente para evitar afirmar una
independencia o un cegamiento que no pueden demostrarse con la evidencia
disponible.

Como acción correctiva, la repetición documentada en
`06_Experimento/repeticion_A4/` utiliza tres evaluadores nuevos ajenos al corpus
y al equipo, requisitos normalizados, orden aleatorio previamente definido y
una rúbrica versionada antes de la recolección.

## Evaluación original con origen no indicado en la hoja

Los cuatro evaluadores recibieron una hoja de evaluación con 66 requisitos
identificados únicamente mediante códigos `ITEM-xxx` y su descripción.

La hoja no contenía ninguna columna que indicara si cada requisito provenía
del proceso humano o había sido generado mediante el LLM.

Las columnas correspondientes a:

- completitud;
- ausencia de ambigüedad;
- verificabilidad;
- corrección respecto a la fuente;
- consistencia interna;

se entregaron vacías para que cada evaluador registrara su propia
puntuación de 1 a 5.

La hoja no mostraba explícitamente la etiqueta correspondiente al origen real
de cada requisito. Esta característica del instrumento se conserva como parte
de la descripción histórica del procedimiento, pero no se utiliza como
evidencia suficiente para afirmar un cegamiento metodológico completo.

Las cuatro evaluaciones se realizaron durante una misma sesión de trabajo y de
forma secuencial utilizando el mismo computador. Cada participante completó su
propia hoja. Antes de pasar al siguiente evaluador se verificó únicamente que
la hoja estuviera completa y se guardó el archivo correspondiente. De acuerdo
con el procedimiento documentado, las puntuaciones de los evaluadores anteriores
no se mostraron al siguiente participante. El uso de una misma sesión y un mismo
equipo constituye una limitación del procedimiento y no se presenta como evidencia
de independencia experimental entre evaluadores.

## Reconstrucción post-evaluación del origen

Una vez finalizadas y recibidas las cuatro evaluaciones, el script de análisis
reconstruye de forma determinista la correspondencia:

`ITEM-xxx → origen → RF real`

La reconstrucción utiliza:

- `datos_crudos/hoja_evaluacion_ciega.csv`, que contiene los identificadores
  ITEM y el texto de cada requisito;
- `datos_procesados/matriz_trazabilidad_tema_RF.csv`, utilizada como fuente
  para los RF humanos;
- `datos_crudos/requisitos_llm.csv`, que contiene los 33 RF LLM completos.

El archivo completo `requisitos_llm.csv` se utiliza porque la matriz temática
documenta principalmente las correspondencias de comparación y puede omitir
requisitos que no participan en un pareo.

No se requiere una clave privada externa.

El script valida automáticamente que la reconstrucción produzca exactamente:

- 66 ITEM;
- 33 requisitos humanos;
- 33 requisitos LLM;

y que no existan coincidencias faltantes ni ambiguas.

El mapa reconstruido se guarda en:

`resultados/mapa_origen_items_reconstruido.csv`

Este archivo es un artefacto **post-evaluación** generado únicamente para el
análisis estadístico y su reproducibilidad. No estuvo disponible para los
evaluadores antes ni durante su calificación.

## Pares temáticos

El análisis principal exploratorio utiliza los **11 pares temáticos estrictos**
identificados mediante:

`tipo == "pareado"`

Estos pares contienen 22 de los 66 requisitos evaluados.

Los otros 44 requisitos se mantienen para:

- trazabilidad;
- análisis descriptivos;
- cálculo de acuerdo entre evaluadores;

pero no se fuerzan artificialmente a una comparación uno a uno.

Los pares utilizados en el análisis se almacenan en:

`resultados/pares_estrictos_utilizados.csv`

## Resultados generados

El script principal genera los siguientes archivos dentro de
`06_Experimento/resultados/`:

- `mapa_origen_items_reconstruido.csv`
- `descriptivos_por_grupo.csv`
- `fleiss_kappa.csv`
- `pares_estrictos_utilizados.csv`
- `prueba_hipotesis_apareada.csv`
- `figura_comparacion_pareada.png`

Una ejecución válida debe reconstruir:

- **66 ITEM**;
- **33 requisitos humanos**;
- **33 requisitos LLM**;
- **11 pares temáticos estrictos**.

En la ejecución reproducible actual no se observaron diferencias
estadísticamente significativas en las cinco dimensiones principales después
de aplicar la corrección Holm-Bonferroni.

La ausencia de significancia estadística no debe interpretarse como prueba de
equivalencia entre los dos procedimientos. Los resultados deben interpretarse
considerando conjuntamente:

- los valores p;
- los intervalos de confianza;
- los tamaños del efecto;
- el tamaño efectivo de 11 pares;
- el nivel de acuerdo entre evaluadores.

## Reproducción

Para reproducir el análisis se recomienda utilizar **Python 3.12**.

Desde la raíz del repositorio:

```bash
python3.12 -m venv .venv-sicst
source .venv-sicst/bin/activate
python -m pip install --upgrade pip
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

En sistemas Ubuntu o GitHub Codespaces, si Python 3.12 informa que
`venv` o `ensurepip` no están disponibles, puede instalarse previamente:

```bash
sudo apt update
sudo apt install -y python3.12-venv
```

La ejecución debe finalizar indicando:

```text
ITEM reconstruidos: 66
RF humanos: 33
RF LLM: 33
Pares estrictos: 11
```

Las salidas se escriben automáticamente en:

`06_Experimento/resultados/`

## Regla de consistencia

Los resultados, el ERS y el manuscrito final deben utilizar las cifras
producidas por la misma ejecución reproducible.

Si una cifra cambia después de regenerar el análisis, debe actualizarse el
documento que haya quedado desfasado.

No deben modificarse manualmente los CSV de resultados con el objetivo de
forzar coincidencias entre documentos.

## Corrección prospectiva A4 y análisis A5

Como acción correctiva posterior al experimento original, se realizó una nueva
repetición documentada en:

`06_Experimento/repeticion_A4/`

La repetición conserva separadas las evidencias del experimento original y los
datos de la nueva ejecución.

Las tres evaluaciones reales completadas se conservan en:

`06_Experimento/repeticion_A4/evaluaciones_completadas/`

y corresponden a `EVAL-01`, `EVAL-02` y `EVAL-03`.

Los tres evaluadores recibieron un archivo Excel de evaluación con los 66
requisitos funcionales normalizados y presentados en el orden aleatorio
previamente definido.

Cada evaluador registró sus puntuaciones en las cinco dimensiones establecidas
por la rúbrica dentro de su archivo Excel correspondiente.

Los archivos Excel completados se conservaron como evidencia primaria de esta
nueva repetición y no sustituyen ni modifican las cuatro evaluaciones del
experimento original.

Cada evaluador calificó los mismos 66 requisitos normalizados y aleatorizados
en las cinco dimensiones de calidad establecidas.

El análisis reproducible solicitado en A5 se encuentra en:

`06_Experimento/repeticion_A4/analisis/`

Los archivos principales son:

- `analisis_A5.py`
- `resultados_fiabilidad_A5.csv`
- `resultado_A5.md`

El análisis A5 incluye:

- ICC(2,1);
- ICC(2,k);
- alfa ordinal con intervalo de confianza;
- κ de Fleiss;
- 1000 remuestreos bootstrap por dimensión;
- efecto mínimo detectable aproximado `dz ≈ 0,94` para 11 pares;
- interpretación explícitamente exploratoria.

Las cuatro evaluaciones originales y las tres evaluaciones de la repetición A4
se mantienen separadas para conservar la trazabilidad histórica del
experimento y de su corrección posterior.

Las puntuaciones originales no se modifican retroactivamente para alterar los
resultados estadísticos o los coeficientes de fiabilidad.
