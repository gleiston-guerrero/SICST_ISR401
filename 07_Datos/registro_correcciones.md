# Registro de correcciones — Plan de mejora de datos SICST

**Plan recibido:** 19/09/2026  
**Repositorio de referencia al recibir el plan:** `gleiston-guerrero/SICST_ISR401`, HEAD `f16af8a`  
**Regla:** no se reescribe historial. Cada corrección se incorpora mediante commit nuevo y se registra aquí.

> IMPORTANTE: los campos `PENDIENTE` deben reemplazarse por el hash real únicamente cuando la tarea correspondiente se haya completado y verificado. No escribir hashes inventados.

| Tarea | Cambio / estado | Evidencia o archivo | Commit |
|---|---|---|---|
| A1 | Pendiente de acción en OSF sobre el registro retrospectivo antiguo | OSF `82q76` | PENDIENTE |
| A2 | Pendiente de evidencia primaria de los evaluadores antiguos o rotulado de procedencia no verificable | declaraciones / hojas originales | PENDIENTE |
| A3 | Se documentó la relación de los evaluadores originales con el corpus, se retiraron afirmaciones no sustentadas de independencia y se sustituyeron las referencias a “evaluación ciega” por una descripción factual del procedimiento: origen no indicado explícitamente en la hoja. | `06_Experimento/README.md`, `06_Experimento/registro_previo/README.md` | `0af95428`, `d1288d58`, `18b2d2db` |
| A4 | Repetición realizada con 3 evaluadores nuevos (`EVAL-01`, `EVAL-02`, `EVAL-03`), 66 requisitos normalizados, orden fijado con semilla `20260918`, rúbrica A4 versionada, control de fuga de estilo y registro OSF `drt3c`. Las tres evaluaciones completadas se conservan como datos crudos. Se añadieron transcripciones revisadas de las tres sesiones y copias redactadas de los consentimientos complementarios, preservando nombres y firmas fuera del repositorio público. El registro OSF fue verificado como `Accepted` antes de la primera sesión real. | `06_Experimento/repeticion_A4/`, `06_Experimento/repeticion_A4/evidencia_sesiones/` | `cd23f392`, `e0f939b9`, `9144b885`, `fbdbcefc`, `38a9804d`, `2173d529`, `330e53c8`, `4843b624`, `34b744fe`, `3c4f3f40`, `4f864580`, `0fab44ed`, `728d9c34`, `cb21b27e`, `e238aba9`, `1e3bda79`, `faf62c59`, `632f60a5`, `d129b04f` |
| A5 | Análisis de fiabilidad ejecutado sobre las tres evaluaciones A4: ICC(2,1), ICC(2,k), alfa ordinal con IC 95 %, κ de Fleiss y declaración de MDE `dz ≈ 0.94`. Los resultados se reportan como exploratorios y sin afirmaciones de equivalencia. | `06_Experimento/repeticion_A4/analisis/analisis_A5.py`, `06_Experimento/repeticion_A4/analisis/resultados_fiabilidad_A5.csv`, `06_Experimento/repeticion_A4/analisis/resultado_A5.md` | `1c10e1a4`, `b501e21a`, `8a3d1465` |
| A6 | Se corrigió la ficha del brazo LLM: quedó rotulada como reconstrucción retrospectiva, se corrigió la contradicción 18/19 archivos, se reconoció la inclusión de archivos WALK y se corrigió el nombre de PAC-07. La exportación o capturas completas de la conversación original siguen pendientes de recuperación. | `06_Experimento/prompts_llm/prompt_generacion_RF_llm.md` | `c2db184e` |
| A7 | Se unificó la definición de consistencia interna y se eliminaron las referencias a una “clave privada” inexistente. La versión auténtica utilizada el 12/09 continúa pendiente de recuperación, por lo que la versión actual está identificada como corrección retrospectiva. | `06_Experimento/instrumentos/rubrica_evaluacion_requisitos.md`, `06_Experimento/instrumentos/README.md` | `5c8a078e`, `da349dd4`, `7eeaa17f` |
| B1 | Pendiente retranscripción desde audio de FAM-04 | audio original + transcripción | PENDIENTE |
| B2 | Se documentó la elegibilidad y el proceso de reclutamiento de los 18 participantes vigentes mediante códigos anonimizados. El archivo registra fecha de actividad, perfil, forma real de contacto, vínculo previo con el equipo, indicaciones comunicadas antes de participar, criterio de inclusión, estado dentro del corpus y evidencia de respaldo. Durante la revisión B1 del 20/09/2026 se confirmó que `FAM-04`, aunque conserva ese código histórico por trazabilidad, corresponde realmente al perfil paciente/expaciente y no a familiar/cuidador. Los datos de reclutamiento y vínculo que no contaban con registro contemporáneo se identifican como reconstrucción retrospectiva; no se inventaron chats ni evidencias inexistentes. Se mantienen 16 entrevistas en el corpus principal y 2 sesiones WALK como evidencia complementaria. | `02_Evidencias/elegibilidad.csv`, `02_Evidencias/Consentimientos/`, `02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv` | `1185ae56`, `29bf57ff` |
| B3 | Pendiente transcripción literal de piezas faltantes y verificación de ritmos/extremos de las transcripciones | audios/videos originales + transcripciones | PENDIENTE |
| B4 | Duraciones del README reemplazadas por valores obtenidos mediante `ffprobe`; total documentado 11875.815 s ≈ 197.93 min. | `02_Evidencias/Transcripciones/README.md`, `02_Evidencias/Fichas tecnicas/duraciones_reales_ffprobe.csv` | `18b45a4b`, `bc6a8b82` |
| B5 | Pendiente verificar y versionar las guías realmente utilizadas frente a las transcripciones | guías + transcripciones | PENDIENTE |
| B6 | Se documentaron las exclusiones de `EV2-PAC-02` y las entrevistas PAC-10 a PAC-14, se preservó la trazabilidad de sus artefactos históricos y se corrigió el primer commit de Frixon a `9824b6a`. | `02_Evidencias/exclusiones_corpus.md`, `10_Autoria/declaracion_cambio_composicion_equipo.md` | `d0f5884f`, `086d6c3a` |
| B7 | Se corrigió la composición documental del corpus y se estableció como definición vigente un corpus principal de 16 entrevistas: 9 participantes con perfil paciente/expaciente, 3 estudiantes de fisioterapia, 3 familiares/cuidadores y 1 profesional. El código histórico `FAM-04` se conserva por trazabilidad, aunque su perfil real corresponde a paciente/expaciente. Las sesiones `WALK-NTEC-01` y `WALK-TEC-01` permanecen como evidencia complementaria y se excluyen del conteo principal y del análisis de saturación. El cierre definitivo de B7 queda sujeto a confirmar, después de B1–B3, que las verificaciones pendientes no modifiquen nuevamente la composición del corpus. | `02_Evidencias/Transcripciones/README.md`, `02_Evidencias/Codificacion_Tematica/README.md`, `02_Evidencias/elegibilidad.csv` | `3adfd273`, `528e663c`, `29bf57ff`, `04b263ad`, `3f945eab` |
| C1 | Pendiente crear y verificar `citas_codificacion.csv` para las codificaciones vigentes y retirar codificaciones sin cita literal verificable | matriz + transcripciones | PENDIENTE |
| C2 | Pendiente codificación verificable de EV2-PAC-07 con citas literales | matriz + transcripción PAC-07 | PENDIENTE |
| C3 | Pendiente realizar doble codificación real sobre al menos 30 % del corpus final con 17 subtemas, trabajos independientes previos a comparación y κ por código con IC | `10_Autoria/doble_codificacion/` | PENDIENTE |
| C4 | Script de saturación corregido para leer la matriz vigente, usar orden cronológico y excluir WALK; CSV y figura regenerados. | `02_Evidencias/Codificacion_Tematica/generar_curva_saturacion.py`, `02_Evidencias/Codificacion_Tematica/saturacion_actualizada.csv`, `02_Evidencias/Codificacion_Tematica/curva_saturacion_SICST.png` | `49a3ce06`, `17124d50` |
| C5 | Historial de versiones del libro de códigos documentado, incluyendo la ampliación de 12 a 17 subtemas del 11/09/2026. | `02_Evidencias/Codificacion_Tematica/historial_libro_codigos.md` | `8b9ee24b` |
| D1–D4 | Pendientes de reconstrucción verificable de procedencia real, corrección de afirmaciones de origen y actualización de matriz/ERS | `04_Trazabilidad/`, `01_ERS/` | PENDIENTE |
| D5 | Pendiente ejecutar la comprobación de rutas/enlaces y corregir todas las referencias inexistentes hasta obtener 0 faltantes | script de comprobación + documentación | PENDIENTE |
| D6 | Pendiente declarar correctamente la naturaleza del `.tex` como reconstrucción posicional o rehacer la fuente, y alinear la versión documental | `01_ERS/README.md`, ERS | PENDIENTE |
| E1 | Pendiente declarar completamente el estado real del MVP —incluyendo almacenamiento local, ausencia de backend/login real y simulaciones— y corregir la Tabla 81 del ERS | `05_MVP/README.md`, ERS | PENDIENTE |
| E2 | Pendiente ejecutar casos de prueba reales de los requisitos Must y registrar caso, fecha, resultado y evidencia | CSV de ejecución + evidencia | PENDIENTE |
| F1 | Pendiente repetir member checking real con participantes del corpus, 17 subtemas, grabación y acta | grabación + acta | PENDIENTE |
| F2 | Pendiente cotejo y corrección de actas, códigos, roles, fechas y evidencias de walkthrough | walkthrough | PENDIENTE |
| F3 | Pendiente fijar fechas reales de notas de campo o aportar evidencia contemporánea que las respalde | notas + registros | PENDIENTE |
| G1 | Pendiente revisión visual de información identificable y autorización escrita antes de cualquier eventual limpieza de historial | archivos sensibles | PENDIENTE |
| G2 | Pendiente cotejo físico de consentimientos originales y retiro/declaración de cualquier dato que no pueda respaldarse | originales | PENDIENTE |
| G3 | Pendiente crear la declaración de desviación ética y enlazarla desde el README; no existe aval institucional firmado en la evidencia actual | `08_Etica/README.md`, futura `08_Etica/declaracion_desviacion_etica.md` | PENDIENTE |
| G4 | Pendiente declarar explícitamente la procedencia de los 4 `Formato_*.docx` y del archivo `HCL - HOJA.docx` | `02_Evidencias/Documentos_Organizacion/README.md` | PENDIENTE |
| G5 | Pendiente completar la declaración de uso de IA con los `.drawio`, conversión PDF→LaTeX, documentos generados con `python-docx`, RNF de IA y demás usos efectivamente realizados | `10_Autoria/declaracion_uso_ia.md` | PENDIENTE |
| H1–H3 | Pendientes de exportación original de Forms, documentación de recodificaciones e instrumento completo | cuestionario + exportación original | PENDIENTE |
| I1 | Pendiente alineación final de versión/URL al cerrar v2.3 y completar CHANGELOG desde 26/07 | README, CITATION, CHANGELOG | PENDIENTE |
| I2 | Pendiente verificar la lista exacta de los archivos del depósito Zenodo del 05/09 antes de corregir su documentación | Zenodo `10.5281/zenodo.22315298` | PENDIENTE |
| I3 | Pendiente fijar finales de línea en `.gitattributes`, fijar versiones exactas de dependencias y realizar prueba final en Windows/autocrlf | `.gitattributes`, `07_Datos/requirements.txt` | PENDIENTE |

## Cierre

Antes de crear `v2.3-datos`:

1. sustituir todos los `PENDIENTE` que realmente se hayan completado por el hash del commit correspondiente;
2. no marcar como hecha ninguna tarea que dependa de evidencia todavía no obtenida;
3. regenerar manifiestos/checksums cuando corresponda;
4. ejecutar las verificaciones reproducibles;
5. crear la etiqueta anotada únicamente sobre el commit final.
