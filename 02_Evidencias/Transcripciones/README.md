# Transcripciones de entrevistas — SICST

Esta carpeta contiene las transcripciones anonimizadas obtenidas durante el proceso de levantamiento de información del proyecto **Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

Las transcripciones representan la evidencia cualitativa obtenida mediante entrevistas realizadas a pacientes, familiares, estudiantes de fisioterapia y profesionales relacionados con el proceso de terapia física.

---

# Objetivo

El objetivo de las transcripciones es conservar la evidencia primaria obtenida durante el trabajo de campo para:

- identificar necesidades de los usuarios;
- analizar problemas del proceso actual de rehabilitación;
- obtener información para la definición de requisitos;
- validar funcionalidades propuestas del sistema SICST;
- mantener trazabilidad entre entrevistas, análisis cualitativo y requisitos del sistema.

---

# Corpus de entrevistas

El corpus final está conformado por **18 entrevistas anonimizadas**.

La distribución de participantes es la siguiente:

## Pacientes o expacientes de terapia física

- EV2-PAC-01
- EV2-PAC-03
- EV2-PAC-04
- EV2-PAC-05
- EV2-PAC-06
- EV2-PAC-07
- EV2-PAC-08
- EV2-PAC-09

## Estudiantes de fisioterapia

- EFT-01
- EFT-02
- EFT-03

## Familiares o cuidadores

- FAM-01
- FAM-02
- FAM-03
- FAM-04

## Profesionales relacionados con fisioterapia

- FIS-01

## Entrevistas adicionales de validación

- WALK-NTEC-01
- WALK-TEC-01

Estas entrevistas adicionales corresponden a perfiles no técnicos y técnicos utilizados para complementar la identificación de necesidades y validación de la solución propuesta.

---

# Convención de nombres

Los archivos siguen la siguiente estructura:

```text
TRANSCRIPCIONES_[CODIGO]_Entrevista.txt
```

Ejemplo:

```text
TRANSCRIPCIONES_EFT-01_Entrevista.txt
```

Donde:

- EFT corresponde al tipo de participante.
- 01 corresponde al identificador anonimizado del participante.
- Entrevista indica el tipo de evidencia registrada.

---

# Tipos de participantes

Los códigos utilizados son:

| Código | Participante |
|---|---|
| EV2-PAC | Paciente o expaciente |
| EFT | Estudiante de fisioterapia |
| FAM | Familiar o cuidador |
| FIS | Profesional de fisioterapia |
| WALK-NTEC | Participante no técnico |
| WALK-TEC | Participante técnico |

---

# Consentimiento y anonimización

Las entrevistas fueron realizadas bajo consentimiento informado de los participantes.

Los archivos fueron anonimizados utilizando códigos identificadores para proteger la identidad de las personas participantes.

No se incluyen nombres reales ni información personal que permita identificar directamente a los participantes.

---

# Duración de entrevistas

Las siguientes duraciones corresponden a la duración técnica de los archivos multimedia de las **18 entrevistas del corpus**, obtenida mediante `ffprobe`.

| Entrevista | Duración |
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

**Duración total del corpus:** `11 875,815 s`, equivalente a aproximadamente **197,93 minutos (3 h 17 min 56 s)**.

Las duraciones anteriores documentadas en este README no correspondían con precisión a la duración técnica de los archivos multimedia. Los valores actuales fueron verificados mediante `ffprobe` y se encuentran documentados en:

```text
02_Evidencias/Fichas tecnicas/duraciones_reales_ffprobe.csv
```

Para `EFT-01`, la duración total corresponde a la suma de las dos partes de su entrevista:

- Parte 1: `00:09:10,248`
- Parte 2: `00:07:58,752`
- Total: `00:17:09,000`

Los archivos de walkthrough independientes y las preguntas adicionales separadas no se incorporan al cálculo de duración de las **18 entrevistas** listadas en esta sección.

---

# Relación con otros artefactos

Las transcripciones se utilizan como fuente para:

- codificación temática;
- matriz de codificación;
- análisis de saturación;
- triangulación de evidencia;
- definición y trazabilidad de requisitos.

Los resultados derivados se encuentran en:

```text
02_Evidencias/Codificacion_Tematica/
```

---

# Integridad de la evidencia

Las transcripciones representan únicamente entrevistas realmente realizadas y registradas dentro del proyecto SICST.

No se incluyen:

- participantes inexistentes;
- respuestas generadas artificialmente;
- entrevistas no realizadas;
- información sin evidencia dentro del corpus.

Cualquier modificación en la composición del corpus debe actualizarse también en:

- codificación temática;
- análisis de saturación;
- triangulación;
- documentación del proyecto.
