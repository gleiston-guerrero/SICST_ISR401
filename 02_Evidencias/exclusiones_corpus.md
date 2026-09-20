# Exclusiones del corpus y tratamiento de aportes históricos — SICST

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Asignatura:** Ingeniería de Requisitos (ISR-401)  
**Fecha de documentación retrospectiva:** 20/09/2026

## Propósito

Este documento registra de forma explícita las exclusiones detectadas durante la revisión del corpus y el tratamiento de aportes históricos de integrantes que ya no forman parte del equipo activo.

La finalidad es mantener trazabilidad sin reescribir el historial Git ni crear datos que no puedan respaldarse. Cuando una fecha o motivo exacto no puede verificarse con la evidencia disponible, se declara expresamente como no verificable.

## Exclusiones del corpus

| Código / evidencia | Tratamiento actual | Motivo documentado | Fecha de exclusión o retiro verificable | Evidencia de historial |
|---|---|---|---|---|
| `EV2-PAC-02` | Excluido del corpus final de entrevistas | No se conserva una transcripción canónica verificable de entrevista en el corpus actual. No se atribuye un motivo adicional que no pueda demostrarse. | Fecha exacta no verificada con la evidencia disponible; exclusión documentada retrospectivamente el 20/09/2026. | Ausente del corpus final vigente. |
| `EVA2-PAC-10` — entrevista | Excluida del corpus de entrevistas; no implica eliminar automáticamente otras evidencias de walkthrough o cuestionario | La transcripción de entrevista fue retirada del repositorio y no forma parte del corpus final de entrevistas. | 08/09/2026, aproximadamente 18:50 hora Ecuador | Commit `de350d1` elimina `TRANSCRIPCIÓN EVA2-PAC-10 Entrevista.txt`. |
| `EVA2-PAC-11` — entrevista | Excluida del corpus de entrevistas; se conserva por separado la evidencia de walkthrough existente | La transcripción de entrevista fue retirada del repositorio y no forma parte del corpus final de entrevistas. | 08/09/2026, aproximadamente 18:39 hora Ecuador | Commit `fadb7fb` elimina `TRANSCRIPCIONES_EVA2-PAC-11_Entrevista.txt`. |
| `EVA2-PAC-12` — entrevista | Excluida del corpus de entrevistas; se conserva por separado la evidencia de walkthrough existente | La transcripción de entrevista fue retirada del repositorio y no forma parte del corpus final de entrevistas. | 04/09/2026, aproximadamente 20:35 hora Ecuador | Commit `85d7b55` elimina `TRANSCRIPCIONES_EVA2-PAC-12_Entrevista.txt` (el registro de GitHub aparece en UTC como 05/09/2026 01:35). |
| `EVA2-PAC-13` — entrevista | Excluida del corpus de entrevistas; se conserva por separado la evidencia de walkthrough existente | La transcripción de entrevista fue retirada del repositorio y no forma parte del corpus final de entrevistas. | 08/09/2026, aproximadamente 18:49 hora Ecuador | Commit `c87258b` elimina `TRANSCRIPCIONES_EVA2-PAC-13_Entrevista.txt`. |
| `EVA2-PAC-14` — entrevista | Excluida del corpus de entrevistas; se conserva por separado la evidencia de walkthrough existente | El Plan de Mejora del 19/09/2026 identifica la entrevista entre las exclusiones realizadas entre el 04 y el 08/09. No se asigna un hash específico mientras no se localice evidencia suficiente para hacerlo. | Entre 04/09/2026 y 08/09/2026, según el Plan de Mejora; fecha exacta pendiente de evidencia verificable. | Plan de Mejora de Datos del 19/09/2026 y ausencia de entrevista canónica en el corpus vigente. |

## Alcance de estas exclusiones

La exclusión de una **entrevista** no significa que deba eliminarse automáticamente toda evidencia asociada al mismo código.

En particular, para `EVA2-PAC-10` a `EVA2-PAC-14` existen artefactos de walkthrough y/o cuestionario en el repositorio actual. Esos artefactos deben tratarse conforme a su propia procedencia, consentimiento, elegibilidad y finalidad, y no deben contabilizarse como entrevistas del corpus solo por compartir código de participante.

Este documento no restaura archivos retirados ni modifica retrospectivamente sus fechas. Únicamente registra el tratamiento analítico actual.

## Tratamiento de aportes de exintegrantes

### Morán Pilaguano Frixon Fernando

Los aportes históricos realizados por Morán Pilaguano Frixon Fernando se conservan en el historial Git bajo su autoría original.

- Primer commit verificado: `9824b6a`, 02/08/2026.
- Último commit documentado: `99d44f0`, 24/08/2026.
- Sus contribuciones previas no se eliminan ni se reasignan a los integrantes activos.
- No se presentan como trabajo realizado por él durante la etapa de cierre posterior a su salida del equipo.

La descripción detallada se mantiene en:

`10_Autoria/declaracion_cambio_composicion_equipo.md`

### Viteri García Jonathan Enrique

No se identifican commits propios de Viteri García Jonathan Enrique en el historial Git documentado para esta entrega.

Su nombre puede conservarse cuando corresponda a la composición histórica del equipo, pero no se le atribuyen artefactos o commits que no estén respaldados por evidencia verificable.

## Regla de conservación

Las exclusiones se aplican al análisis vigente y no mediante reescritura del historial Git.

Los archivos o aportes históricos que existieron permanecen trazables mediante los commits correspondientes. Cualquier cambio posterior debe incorporarse como un commit nuevo y registrarse también en:

`07_Datos/registro_correcciones.md`
