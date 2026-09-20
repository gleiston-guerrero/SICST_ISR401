# Historial de versiones del libro de códigos — SICST

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Asignatura:** Ingeniería de Requisitos (ISR-401)  
**Documento de trazabilidad retrospectiva:** 20/09/2026

## Propósito

Este documento registra la evolución verificable del libro de códigos utilizado en la codificación temática del proyecto SICST.

No sustituye el historial Git ni modifica versiones anteriores. Su objetivo es dejar explícito cuándo se amplió el libro de códigos, qué subtemas se incorporaron y qué evidencia estaba siendo integrada en esa etapa.

## Versión inicial — 12 subtemas

Antes del commit `547a504`, el archivo:

`02_Evidencias/Codificacion_Tematica/libro_codigos.csv`

contenía **12 subtemas**, identificados desde `SUB-01` hasta `SUB-12`.

Los subtemas eran:

| Código | Subtema |
|---|---|
| SUB-01 | Adherencia y recordatorios |
| SUB-02 | Instrucciones y dosificación |
| SUB-03 | Apoyo audiovisual |
| SUB-04 | Supervisión y corrección de ejecución |
| SUB-05 | Registro de dolor y fatiga |
| SUB-06 | Seguimiento del progreso |
| SUB-07 | Comunicación con fisioterapeuta |
| SUB-08 | Privacidad de cámara y datos |
| SUB-09 | Acceso familiar autorizado |
| SUB-10 | Seguridad y señales de alarma |
| SUB-11 | Accesibilidad y facilidad de uso |
| SUB-12 | Organización centralizada |

## Ampliación a 17 subtemas

El **11/09/2026**, mediante el commit:

`547a5043fba6b504a810f2a9d7a67117223f19e5`

con mensaje:

`Update libro_codigos.csv with new entries and definitions`

el libro de códigos fue ampliado de **12 a 17 subtemas**.

La marca temporal del commit es `2026-09-11T14:15:55Z`, equivalente aproximadamente a las **09:15:55 de Ecuador continental (UTC-5)**.

La ampliación ocurrió después de incorporar y revisar evidencia de entrevistas de los grupos **EFT**, **FAM** y **FIS**, de acuerdo con la revisión del Plan de Mejora de Datos.

No se afirma que cada nuevo subtema provenga exclusivamente de un único perfil o participante. La ampliación se documenta como una revisión del libro de códigos realizada con un corpus cualitativo más amplio disponible en ese momento.

## Subtemas añadidos

Los cinco subtemas incorporados fueron:

| Código | Categoría | Subtema | Definición incorporada |
|---|---|---|---|
| SUB-13 | Gobernanza de IA | Control profesional de las decisiones | Necesidad de que el fisioterapeuta conserve la decisión clínica y revise las sugerencias del sistema antes de modificar tratamientos, ejercicios o cargas. |
| SUB-14 | Gobernanza de IA | Explicabilidad e incertidumbre | Necesidad de comprender las razones y los datos que sustentan una recomendación automatizada, así como sus límites o incertidumbre. |
| SUB-15 | Gestión del plan | Vigencia y versiones de rutinas | Dificultad para distinguir instrucciones actuales de anteriores o necesidad de identificar la rutina vigente, su fecha de actualización y los cambios realizados. |
| SUB-16 | Alertas | Priorización y frecuencia de avisos | Necesidad de distinguir alertas urgentes de avisos informativos, definir cuándo notificar al paciente o familiar y evitar notificaciones excesivas. |
| SUB-17 | Privacidad | Revocación y gestión de permisos | Necesidad de consultar, modificar, revocar o establecer vencimiento a permisos de acceso, así como conocer quién accedió a la información. |

## Datos disponibles en la etapa de ampliación

En la etapa en que se amplió el libro de códigos ya se habían incorporado al proceso de análisis transcripciones correspondientes a:

- estudiantes de fisioterapia (`EFT`);
- familiares o cuidadores (`FAM`);
- profesional de fisioterapia (`FIS`);
- además de las entrevistas de pacientes y demás evidencia cualitativa que ya formaba parte del repositorio.

Por tanto, la versión de 17 subtemas debe entenderse como una **revisión posterior del esquema de codificación**, realizada después de ampliar las fuentes disponibles para el análisis.

## Regla de trazabilidad

La versión histórica de 12 subtemas no se elimina ni se reescribe.

El historial Git conserva la evolución del archivo, mientras que la versión vigente de:

`02_Evidencias/Codificacion_Tematica/libro_codigos.csv`

contiene los **17 subtemas**.

Cualquier cambio posterior al libro de códigos debe documentar:

1. fecha real del cambio;
2. códigos añadidos, modificados o retirados;
3. motivo;
4. evidencia utilizada;
5. commit correspondiente.
