# Codificación temática — SICST

Esta carpeta contiene el análisis cualitativo realizado sobre el corpus de entrevistas del proyecto **Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

La codificación temática permite identificar patrones, necesidades recurrentes, problemas del proceso actual de terapia física y elementos relevantes para la definición, validación y trazabilidad de requisitos.

---

# Objetivo

El objetivo del análisis cualitativo es identificar temas relacionados con:

- seguimiento del proceso terapéutico;
- comunicación entre pacientes y profesionales;
- cumplimiento de ejercicios asignados;
- registro y consulta de información de terapia;
- dificultades del proceso de rehabilitación;
- necesidades esperadas en una solución tecnológica.

Los resultados se utilizan como evidencia para relacionar necesidades identificadas durante el trabajo de campo con requisitos del sistema SICST.

---

# Corpus analítico vigente

Para el análisis cualitativo principal se utiliza actualmente un corpus de **16 entrevistas anonimizadas**.

## Pacientes o expacientes de terapia física — 8

- EV2-PAC-01
- EV2-PAC-03
- EV2-PAC-04
- EV2-PAC-05
- EV2-PAC-06
- EV2-PAC-07
- EV2-PAC-08
- EV2-PAC-09

## Estudiantes de fisioterapia — 3

- EFT-01
- EFT-02
- EFT-03

## Familiares o cuidadores — 4

- FAM-01
- FAM-02
- FAM-03
- FAM-04

## Profesional relacionado con fisioterapia — 1

- FIS-01

Total:

```text
8 PAC + 3 EFT + 4 FAM + 1 FIS = 16 entrevistas
```

---

# Evidencia walkthrough complementaria

Se conservan adicionalmente como evidencia complementaria de validación:

- WALK-NTEC-01
- WALK-TEC-01

Estas sesiones **no se contabilizan como entrevistas del corpus principal** y se excluyen del análisis de saturación temática.

Otros artefactos históricos de walkthrough conservados en el repositorio tampoco deben incorporarse automáticamente al conteo de entrevistas solo por existir como archivos de evidencia.

---

# Método de codificación

La codificación temática utiliza categorías y subtemas documentados en el libro de códigos vigente.

Cada código se registra mediante presencia o ausencia del subtema:

- **1:** existe evidencia suficiente del subtema dentro de la entrevista;
- **0:** no se identificó evidencia suficiente del subtema.

Un valor igual a `0` representa ausencia de evidencia suficiente para asignar el subtema; no representa necesariamente desacuerdo del participante.

La verificación literal de las asignaciones positivas mediante citas de transcripción corresponde a la tarea C1 del plan de mejora y debe documentarse separadamente.

---

# Artefactos de análisis

## Libro de códigos

Archivo:

```text
libro_codigos.csv
```

Contiene la definición de categorías, códigos y subtemas.

El historial de ampliación del libro de códigos se documenta en:

```text
historial_libro_codigos.md
```

---

## Matriz de codificación

Archivo vigente:

```text
matriz_codificacion_SICST.csv
```

Contiene la relación entre las entrevistas analizadas y los subtemas registrados durante el proceso de codificación.

---

## Análisis de saturación

Archivos vigentes:

```text
saturacion_actualizada.csv
curva_saturacion_SICST.png
generar_curva_saturacion.py
```

Estos artefactos documentan la evolución de aparición de nuevos temas durante el análisis del corpus principal.

El script de saturación utiliza el orden cronológico documentado de las **16 entrevistas del corpus principal** y excluye los códigos `WALK` del cálculo.

---

## Triangulación

Archivo conservado actualmente en el repositorio:

```text
triangulacion (1).md
```

Documenta la comparación entre diferentes fuentes de evidencia, incluyendo entrevistas, evidencia complementaria de walkthrough, necesidades identificadas y requisitos derivados.

---

# Reproducibilidad

Los datos procesados y scripts utilizados para resultados derivados se documentan adicionalmente en:

```text
07_Datos/
```

Cualquier modificación en la composición del corpus debe reflejarse posteriormente en:

- matriz de codificación;
- análisis de saturación;
- triangulación;
- resultados del manuscrito científico;
- documentación de trazabilidad;
- `07_Datos/registro_correcciones.md`.

---

# Integridad del análisis

El análisis cualitativo debe utilizar únicamente evidencia respaldada por los artefactos reales del corpus.

No se deben agregar:

- participantes inexistentes;
- entrevistas no realizadas;
- respuestas no disponibles;
- resultados sin respaldo verificable.

Los cambios en la composición del corpus deben mantenerse sincronizados entre:

- transcripciones;
- codificación temática;
- saturación;
- triangulación;
- documentación final.

---

# Doble codificación

Los artefactos históricos de doble codificación se conservan en:

```text
10_Autoria/doble_codificacion/
```

Su adecuación al requisito actualizado de la tarea C3 se revisa separadamente. La existencia de esos archivos no implica que C3 esté cerrada.

---

# Estado de la tarea B7

Este README corrige la contradicción documental previa que indicaba un número distinto de entrevistas.

La definición actualmente utilizada es:

```text
16 entrevistas del corpus principal
+ 2 sesiones WALK complementarias
```

Las sesiones WALK no se incluyen en saturación temática.

La tarea B7 solo podrá considerarse completamente cerrada cuando se resuelvan las verificaciones pendientes de B1–B3 y se confirme que no modifican la composición final del corpus.
