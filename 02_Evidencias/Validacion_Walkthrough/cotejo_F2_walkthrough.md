# F2 — Cotejo y corrección de evidencias walkthrough

**Fecha de revisión:** 21/09/2026

## Objetivo

Este documento registra las correcciones realizadas sobre las evidencias de walkthrough observadas en el plan de mejora de datos SICST.

Se preservan los documentos originales sin alterar los códigos o fechas manuscritas que contienen. Cuando un acta utiliza un código histórico distinto al código vigente, la equivalencia se documenta expresamente para mantener trazabilidad.

## Correcciones realizadas

### EV2-PAC-04

Se detectó que dos documentos estaban intercambiados entre las carpetas de consentimiento y validación walkthrough.

La versión vigente quedó organizada así:

- `02_Evidencias/Consentimientos/EV2-PAC-04_Consentimiento_Firmado.jpeg`: consentimiento informado correspondiente a EV2-PAC-04.
- `02_Evidencias/Validacion_Walkthrough/EV2-PAC-04_Acta_Walkthrough.jpeg`: parte 1 del acta de walkthrough.
- `02_Evidencias/Validacion_Walkthrough/EV2-PAC-04_Acta_Walkthrough_Parte2.jpeg`: parte 2 del acta de walkthrough.

La copia pública del consentimiento fue redactada para ocultar datos personales identificables.

### EV2-PAC-09

El archivo `EV2-PAC-09_Acta_Walkthrough_Parte2.png` correspondía en realidad a un consentimiento informado y no a una segunda parte del acta.

Por esta razón se retiró de `02_Evidencias/Validacion_Walkthrough/`.

La evidencia vigente queda:

- `02_Evidencias/Validacion_Walkthrough/EV2-PAC-09_Acta_Walkthrough.png`: acta de walkthrough.
- `02_Evidencias/Consentimientos/EV2-PAC-09_Consentimiento_Firmado.jpeg`: consentimiento informado correspondiente.

No se modificó el historial de Git; la corrección se realizó mediante un commit nuevo.

### EV2-PAC-01

La fecha `14/07/2026` registrada previamente para el walkthrough era incorrecta.

La fecha verificada y utilizada actualmente es:

- Walkthrough: `19/07/2026`.
- Entrevista: `19/07/2026`.

Por tanto, el walkthrough no ocurrió antes de la entrevista por varios días como sugería la documentación anterior.

La nota asociada fue renombrada a:

`2026-07-19_Walkthrough_Paciente_EV2-PAC-01_Notas.jpeg`

La bitácora y el registro de elaboración de notas fueron actualizados con la misma fecha.

### EV2-PAC-03

La fecha `13/07/2026` registrada previamente para el walkthrough era incorrecta.

La fecha verificada y utilizada actualmente es:

- Walkthrough: `19/07/2026`.
- Entrevista: `19/07/2026`.

Por tanto, el walkthrough no ocurrió antes de la entrevista por varios días como sugería la documentación anterior.

La nota asociada fue renombrada a:

`2026-07-19_Walkthrough_Paciente_EV2-PAC-03_Notas.jpeg`

La bitácora y el registro de elaboración de notas fueron actualizados con la misma fecha.

### WALK-NTEC-01

El código vigente del participante es:

`WALK-NTEC-01`

El acta física conserva el código histórico:

`WALK-PAC-02`

Este código fue utilizado durante una etapa anterior de organización documental, antes de la normalización de códigos utilizada actualmente.

La equivalencia vigente es:

- Código histórico del acta: `WALK-PAC-02`.
- Código vigente: `WALK-NTEC-01`.
- Perfil real: paciente/expaciente utilizado como usuario no técnico para la validación.
- Fecha de actividad: `19/07/2026`.

El contenido del acta original no fue alterado para reemplazar retrospectivamente el código histórico.

El consentimiento público fue normalizado al nombre:

`WALK-NTEC-01_Consentimiento_Firmado.jpeg`

### WALK-TEC-01

El código vigente del participante es:

`WALK-TEC-01`

El acta física conserva el código histórico:

`WALK-FIS-01`

El participante corresponde al perfil de fisioterapeuta y fue utilizado como usuario técnico durante la validación.

La evidencia conservada permite distinguir dos fechas distintas:

- Fecha de firma del acta/consentimiento: `19/07/2026`.
- Fecha real de la sesión registrada en video: `23/07/2026`, aproximadamente a las 20:23.

Estas fechas no se modifican para hacerlas coincidir artificialmente. La firma previa y la sesión posterior se documentan como eventos distintos.

La equivalencia vigente es:

- Código histórico del acta: `WALK-FIS-01`.
- Código vigente: `WALK-TEC-01`.
- Rol: fisioterapeuta.
- Fecha de consentimiento/acta: `19/07/2026`.
- Fecha de sesión: `23/07/2026`.

La bitácora y `elegibilidad.csv` utilizan `23/07/2026` como fecha de la actividad.

La copia pública del consentimiento se conserva como:

`WALK-TEC-01_Consentimiento_Firmado.jpg`

La nota de campo asociada fue renombrada a:

`2026-07-23_Walkthrough_Tecnico_WALK-TEC-01_Notas.jpeg`

## Códigos históricos y códigos vigentes

| Código histórico | Código vigente | Perfil vigente |
|---|---|---|
| `WALK-PAC-02` | `WALK-NTEC-01` | Paciente/expaciente — usuario no técnico |
| `WALK-FIS-01` | `WALK-TEC-01` | Fisioterapeuta — usuario técnico |

Los códigos históricos permanecen visibles dentro de las actas originales por trazabilidad. No se editaron las imágenes para aparentar que originalmente utilizaron los códigos actuales.

## Archivos de referencia

Las correcciones se reflejan en:

- `02_Evidencias/elegibilidad.csv`
- `02_Evidencias/Consentimientos/`
- `02_Evidencias/Validacion_Walkthrough/`
- `10_Autoria/bitácora_sesiones/bitacora_elicitacion.csv`
- `10_Autoria/notas_campo/registro_elaboracion_notas.csv`

## Integridad documental

No se alteraron fechas manuscritas, firmas, códigos históricos ni contenidos de las actas originales.

Las correcciones se limitaron a:

- clasificación correcta de documentos;
- nombres de archivo;
- códigos vigentes en los registros de trazabilidad;
- roles;
- fechas verificadas de actividad;
- explicación explícita de las diferencias históricas.

Los documentos originales se mantienen como evidencia de cómo fueron generados en su momento.
