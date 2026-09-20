# Rúbrica de Evaluación de Calidad de Requisitos Funcionales — SICST

> **Nota de procedencia:** esta versión contiene correcciones retrospectivas
> realizadas después de la evaluación original del 12/09/2026 para unificar
> definiciones y documentar las limitaciones metodológicas detectadas durante
> la revisión. No se presenta como una reconstrucción de una versión original
> que no pueda verificarse. Si se recupera la versión auténtica utilizada el
> 12/09/2026, deberá conservarse separadamente como evidencia histórica.

## Objetivo

Evaluar comparativamente la calidad de los Requisitos Funcionales (RF)
elicitados por el equipo humano y los generados por el modelo de lenguaje
(LLM), mediante una escala Likert de 1 a 5 en cinco dimensiones.

## Escala

Cada dimensión se puntúa de **1** (no cumple en absoluto) a **5** (cumple
totalmente), sin puntos intermedios ambiguos.

---

## Dimensiones de evaluación

### 1. Completitud

¿La información proporcionada en el requisito permite comprender
completamente la funcionalidad esperada, sin dejar vacíos relevantes?

### 2. Ausencia de ambigüedad

¿El requisito está redactado de forma precisa, sin términos vagos ni
interpretaciones múltiples posibles?

### 3. Verificabilidad

¿Es posible comprobar objetivamente si el requisito fue implementado
correctamente (se puede definir una prueba o criterio de aceptación)?

### 4. Corrección respecto a la fuente

¿El requisito refleja fielmente lo que se dijo en la transcripción de
entrevista de la que proviene, sin agregar ni distorsionar información?

### 5. Consistencia interna

¿El requisito es coherente y no contradice otros requisitos funcionales
o elementos relacionados del sistema?

---

## Registro de evaluación

Cada evaluador completa su hoja individual en:

```
datos_crudos/evaluaciones_ciegas/Evaluacion_<nombre>.xlsx
```

Puntuando cada uno de los 66 ítems anonimizados de
`datos_crudos/hoja_evaluacion_ciega.csv` en las 5 dimensiones anteriores.

## Ocultación de la etiqueta de origen

La hoja utilizada en la evaluación original no mostraba explícitamente una
columna que indicara si cada ítem provenía del proceso humano o del LLM.

Esta ocultación de la etiqueta de origen no se presenta como evidencia de un
cegamiento metodológico completo, debido a la relación previa de los
evaluadores originales con participantes y actividades del estudio.

Después de la evaluación, el origen de los ítems se reconstruye de forma
determinista a partir de los archivos versionados del experimento.

## Evaluadores participantes

4 evaluadores: Mishell, Angel, Dayana y Sebas.
