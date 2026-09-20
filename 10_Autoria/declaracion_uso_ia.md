# Declaración de uso de Inteligencia Artificial

## Proyecto

**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**

## Integrantes

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul

## Declaración

Durante el desarrollo, corrección y cierre documental del proyecto se utilizaron herramientas de inteligencia artificial, principalmente ChatGPT, como apoyo en tareas de organización, redacción técnica, revisión, programación, transformación de documentos y preparación de artefactos.

El uso de IA fue de apoyo. Los integrantes conservaron la responsabilidad sobre la revisión, aceptación y publicación de los contenidos incorporados al repositorio.

La IA también pudo utilizarse para elaborar ejemplos, borradores, reformulaciones o materiales de trabajo. Esos contenidos no deben considerarse por sí solos evidencia empírica. Para el corpus y las conclusiones del proyecto solo deben conservarse como datos válidos aquellos elementos respaldados por una recolección documentada, con participante, fecha, consentimiento y evidencia de origen. Cuando una reconstrucción, normalización o corrección retrospectiva no pudo verificarse contra evidencia primaria, debe identificarse como tal o retirarse del análisis.

## Registro de uso

| Sección o actividad | Herramienta | Uso realizado | Verificación / límite |
|---|---|---|---|
| Organización del repositorio | ChatGPT | Revisión de estructura, rutas, archivos faltantes y consistencia documental | Revisión manual en GitHub y comparación con el plan de mejora |
| Redacción y corrección técnica | ChatGPT | Apoyo para redactar, reorganizar y corregir README, declaraciones, registros y documentación técnica | Revisión de los integrantes antes de incorporar cambios |
| Paquete reproducible `07_Datos` | ChatGPT | Apoyo en estructura de scripts, documentación y reproducibilidad | Ejecución sobre archivos reales y revisión de salidas |
| Scripts de procesamiento y análisis | ChatGPT | Apoyo en código Python para limpieza, análisis, gráficos, checksums y automatización | Ejecución local y comparación con datos existentes |
| Análisis estadístico | ChatGPT | Apoyo para estructurar cálculos y reportes de fiabilidad y acuerdo | Resultados generados mediante scripts versionados y revisados |
| Doble codificación | ChatGPT | Apoyo para organizar tablas, automatizar cálculos y documentar resultados | La herramienta no sustituye la codificación humana independiente requerida |
| Diagramas y fuentes `.drawio` | ChatGPT + draw.io | Apoyo en la definición de elementos, relaciones, nombres y estructura de diagramas; edición final en draw.io | Las fuentes editables `.drawio` se conservan en `10_Autoria/fuentes_editables/` |
| Conversión / reconstrucción PDF → LaTeX | ChatGPT | Apoyo para reconstruir contenido documental en una fuente `.tex` a partir de material PDF y corregir problemas de compilación | La fuente LaTeX debe describirse según su procedencia real; no se asume equivalencia automática con el documento original |
| Generación de documentos DOCX | ChatGPT + Python (`python-docx`) | Apoyo para generar o estructurar documentos `.docx` utilizados durante el proyecto y sus correcciones | Los archivos generados deben distinguirse de evidencia primaria y documentos externos originales |
| Requisitos y componentes relacionados con IA | ChatGPT | Apoyo en redacción y revisión de requisitos no funcionales, riesgos, componentes y trazabilidad relacionados con cámara, análisis de movimiento e IA | Se distingue entre requisitos propuestos y capacidades realmente implementadas en el MVP |
| MVP | ChatGPT | Revisión del código y documentación para identificar funciones reales, simuladas, parciales o no implementadas | `05_MVP/README.md` declara expresamente las limitaciones del prototipo |
| Revisión de transcripciones | ChatGPT | Apoyo para detectar inconsistencias, errores de reconocimiento automático y problemas de concordancia | No se declara cotejo literal contra audio cuando esa escucha no fue realizada |
| Ejemplos y borradores de entrevistas/documentos | ChatGPT | Apoyo ocasional para producir ejemplos, versiones de trabajo o redacciones de referencia | Estos materiales no deben tratarse como datos reales sin respaldo documental independiente |
| Plan de mejora de datos | ChatGPT | Apoyo para localizar tareas pendientes, preparar correcciones, registrar commits y mantener trazabilidad de cambios | Cada corrección se incorpora mediante commits nuevos; no se reescribe el historial |
| Revisión final del repositorio | ChatGPT | Identificación de archivos faltantes, inconsistencias de rutas y documentación pendiente | Verificación manual en el repositorio y mediante scripts cuando corresponde |

## Aclaración sobre diagramas `.drawio`

El repositorio contiene fuentes editables `.drawio` dentro de `10_Autoria/fuentes_editables/`. La IA se utilizó como apoyo para proponer o revisar estructura, nombres, relaciones y contenido textual de algunos diagramas.

La herramienta draw.io fue utilizada para la edición y conservación del artefacto gráfico. La existencia de un archivo `.drawio` no significa que haya sido generado íntegramente por IA.

## Aclaración sobre PDF y LaTeX

Se utilizó IA como apoyo durante actividades de conversión o reconstrucción de contenido documental hacia LaTeX y para resolver problemas de compilación.

Cuando la fuente `.tex` sea una reconstrucción derivada de un PDF u otro documento previo, debe declararse esa naturaleza de forma transparente. No debe presentarse automáticamente como fuente original contemporánea si no lo fue.

## Aclaración sobre `python-docx`

En distintas actividades se utilizaron scripts de Python y la biblioteca `python-docx` con apoyo de IA para estructurar o generar documentos de trabajo en formato DOCX.

Estos documentos deben diferenciarse de:

- evidencia primaria;
- formularios originales firmados;
- archivos recibidos de participantes o terceros;
- documentos institucionales emitidos oficialmente.

La generación automatizada de un DOCX no demuestra por sí sola autoría externa, fecha histórica ni aprobación institucional.

## Aclaración sobre requisitos de IA

El proyecto contiene documentación de requisitos y componentes relacionados con inteligencia artificial, cámara y análisis de movimiento.

El uso de IA para apoyar la redacción de estos requisitos no implica que dichas funciones estén implementadas en el MVP. El estado real del prototipo se documenta separadamente y distingue entre funciones implementadas, parciales, simuladas y no implementadas.

## Límites y responsabilidad

Los integrantes son responsables de:

- revisar los contenidos generados o sugeridos por IA;
- contrastarlos con evidencia real antes de incorporarlos como datos o resultados;
- corregir errores o afirmaciones no verificables;
- no presentar contenido generado como evidencia empírica si no existe respaldo independiente;
- declarar reconstrucciones retrospectivas cuando corresponda;
- retirar del análisis los datos que no puedan respaldarse;
- conservar la trazabilidad de las correcciones mediante Git.

Los ejemplos, respuestas hipotéticas, borradores o documentos generados con IA no se consideran automáticamente evidencia de campo. Su validez depende de que exista una fuente real verificable que respalde su incorporación al corpus.

## Responsables

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul

**Fecha de actualización:** 20/09/2026
