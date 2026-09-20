# Transcripciones de entrevistas — SICST

Esta carpeta contiene las transcripciones anonimizadas obtenidas durante el proceso de levantamiento de información del proyecto **Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

Las transcripciones representan evidencia cualitativa obtenida mediante entrevistas a pacientes o expacientes, familiares o cuidadores, estudiantes de fisioterapia y profesionales relacionados con el proceso de terapia física.

---

# Objetivo

El objetivo de las transcripciones es conservar la evidencia primaria disponible para:

- identificar necesidades de los usuarios;
- analizar problemas del proceso actual de rehabilitación;
- obtener información para la definición de requisitos;
- apoyar la validación de funcionalidades propuestas del sistema SICST;
- mantener trazabilidad entre entrevistas, análisis cualitativo y requisitos.

---

# Corpus analítico vigente

De acuerdo con la composición actualmente documentada, el **corpus principal de entrevistas** está conformado por **16 entrevistas anonimizadas**.

La distribución es la siguiente:

## Pacientes o expacientes de terapia física — 9

- EV2-PAC-01
- EV2-PAC-03
- EV2-PAC-04
- EV2-PAC-05
- EV2-PAC-06
- EV2-PAC-07
- EV2-PAC-08
- EV2-PAC-09
- FAM-04 *(código histórico conservado; perfil real: paciente/expaciente)*

## Estudiantes de fisioterapia — 3

- EFT-01
- EFT-02
- EFT-03

## Familiares o cuidadores — 3

- FAM-01
- FAM-02
- FAM-03

## Profesional relacionado con fisioterapia — 1

- FIS-01

Total:

```text
9 participantes con perfil paciente/expaciente + 3 EFT + 3 FAM + 1 FIS = 16 entrevistas
```

---

# Sesiones walkthrough complementarias

Además del corpus principal de 16 entrevistas, se conservan como evidencia complementaria las sesiones identificadas como:

- WALK-NTEC-01
- WALK-TEC-01

Estas sesiones **no se contabilizan dentro de las 16 entrevistas del corpus principal** y no se incorporan al cálculo de saturación temática.

En la carpeta también existen otros artefactos históricos de walkthrough asociados a códigos de participantes. Su existencia no implica que deban sumarse como entrevistas del corpus principal. Su tratamiento corresponde a evidencia complementaria de validación y debe mantenerse diferenciado del corpus analítico de entrevistas.

---

# Convención de nombres

Los archivos de entrevista siguen, cuando aplica, la estructura:

```text
TRANSCRIPCIONES_[CODIGO]_Entrevista.txt
```

Ejemplo:

```text
TRANSCRIPCIONES_EFT-01_Entrevista.txt
```

Donde:

- `EFT` corresponde al tipo de participante;
- `01` corresponde al identificador anonimizado;
- `Entrevista` indica el tipo de evidencia.

Existen nombres históricos con variaciones de espacios, acentos o sufijos. Esos nombres se conservan mientras se revisa su trazabilidad y no se modifican retroactivamente sin necesidad.

---

# Tipos de participantes

| Código | Participante |
|---|---|
| EV2-PAC | Paciente o expaciente |
| EFT | Estudiante de fisioterapia |
| FAM | Familiar o cuidador |
| FIS | Profesional relacionado con fisioterapia |
| WALK-NTEC | Participante de sesión walkthrough no técnica |
| WALK-TEC | Participante de sesión walkthrough técnica |

> **Nota de trazabilidad:** `FAM-04` conserva su código histórico para no romper referencias previas, pero la revisión de la evidencia confirmó que su perfil real corresponde a paciente/expaciente y no a familiar/cuidador.

---

# Consentimiento y anonimización

Los archivos públicos utilizan códigos para reducir la exposición de información identificable.

La verificación completa de los consentimientos originales y de la cobertura ética de cada participante se documenta por separado dentro del plan de mejora. Por esta razón, este README no sustituye el cotejo físico de consentimientos requerido en las tareas éticas.

No deben publicarse nombres reales, firmas, números de identificación, teléfonos, correos u otros datos personales que permitan identificar directamente a los participantes.

---

# Duración de los registros principales documentados

La siguiente tabla corresponde a **18 registros multimedia listados en esta sección**:

- 16 entrevistas del corpus principal;
- 2 sesiones walkthrough complementarias (`WALK-NTEC-01` y `WALK-TEC-01`).

Las duraciones fueron obtenidas mediante `ffprobe`.

| Registro | Duración |
|---|---:|
| EV2-PAC-01 | 04:46 |
| EV2-PAC-03 | 04:17 |
| EV2-PAC-04 | 07:25 |
| EV2-PAC-05 | 13:09 |
| EV2-PAC-06 | 12:15 |
| EV2-PAC-07 | 09:26 |
| EV2-PAC-08 | 10:00 |
| EV2-PAC-09 | 07:37 |
| EFT-01 | 17:09 |
| EFT-02 | 17:27 |
| EFT-03 | 13:59 |
| FAM-01 | 14:34 |
| FAM-02 | 11:06 |
| FAM-03 | 13:05 |
| FAM-04 | 12:39 |
| FIS-01 | 07:13 |
| WALK-NTEC-01 | 03:57 |
| WALK-TEC-01 | 17:52 |

**Duración total de estos 18 registros multimedia:** `11 875,815 s`, equivalente a aproximadamente **197,93 minutos (3 h 17 min 56 s)**.

Los valores fueron verificados mediante `ffprobe` y se documentan en:

```text
02_Evidencias/Fichas tecnicas/duraciones_reales_ffprobe.csv
```

Para `EFT-01`, la duración total corresponde a la suma de las dos partes registradas:

- Parte 1: `00:09:10,248`
- Parte 2: `00:07:58,752`
- Total: `00:17:09,000`

La inclusión de `WALK-NTEC-01` y `WALK-TEC-01` en esta tabla de duración no los convierte en entrevistas del corpus principal.

---

# Relación con otros artefactos

Las **16 entrevistas del corpus principal** se utilizan como fuente para:

- codificación temática;
- matriz de codificación;
- análisis de saturación;
- triangulación de evidencia;
- definición y trazabilidad de requisitos.

Los resultados derivados se encuentran en:

```text
02_Evidencias/Codificacion_Tematica/
```

Las sesiones walkthrough se tratan como evidencia complementaria de validación y deben mantenerse diferenciadas del corpus principal de entrevistas.

---

# Integridad de la evidencia

El análisis vigente debe utilizar únicamente evidencia respaldada por los archivos reales disponibles.

No se deben agregar:

- participantes inexistentes;
- respuestas generadas artificialmente;
- entrevistas no realizadas;
- información sin respaldo documental.

Cualquier cambio posterior en la composición del corpus debe actualizar también:

- este README;
- la matriz de codificación;
- el análisis de saturación;
- la triangulación;
- la documentación del proyecto;
- `07_Datos/registro_correcciones.md`.

---

# Exclusiones documentadas

Las exclusiones detectadas durante la revisión del corpus se documentan en:

```text
02_Evidencias/exclusiones_corpus.md
```

Ese registro conserva la trazabilidad histórica sin restaurar archivos retirados ni reescribir el historial Git.

---

# Estado de la tarea B7

Este README corrige la contradicción documental que mezclaba entrevistas y walkthroughs en un mismo conteo.

La definición actualmente utilizada es:

```text
16 entrevistas del corpus principal
+ 2 sesiones WALK complementarias
```

La tarea B7 solo podrá considerarse completamente cerrada cuando también se resuelvan las verificaciones pendientes de B1–B3 y se confirme que esas revisiones no modifican la composición final del corpus.
