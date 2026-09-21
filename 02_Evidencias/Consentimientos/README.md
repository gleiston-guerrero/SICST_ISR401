# Consentimientos informados — SICST

Esta carpeta contiene las **copias públicas y enmascaradas de los consentimientos informados** correspondientes a las actividades de levantamiento y validación realizadas para el proyecto:

**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**

Los archivos se identifican mediante códigos de participante para evitar utilizar nombres propios dentro de la estructura pública del repositorio.

La existencia de un archivo de consentimiento dentro de esta carpeta no implica por sí sola que la participación esté validada para el corpus principal. La elegibilidad, perfil real, actividad y estado de cada participante deben contrastarse con `02_Evidencias/elegibilidad.csv` y con las demás evidencias de trazabilidad disponibles.

---

## Protección de datos

Los documentos almacenados en esta carpeta corresponden únicamente a la **versión pública de los consentimientos**.

Antes de su publicación deben encontrarse protegidos o enmascarados los datos identificables, especialmente:

- número de cédula;
- firma manuscrita;
- nombres completos cuando permitan identificar directamente al participante;
- teléfonos;
- direcciones;
- correos electrónicos;
- cualquier otro dato personal identificable.

Los consentimientos originales sin censura no se publican en esta carpeta.

Los originales restringidos se documentan en [`../00_Restringido/README.md`](../00_Restringido/README.md).

El contenedor cifrado `evidencias_restringidas.7z` se distribuye como asset del Release `evidencias-2B` y no se almacena dentro del árbol Git del repositorio.

La contraseña del contenedor cifrado no debe almacenarse en el repositorio público.

---

## Convención de códigos

Los participantes se identifican mediante códigos seudonimizados.

Los prefijos utilizados corresponden a la clasificación histórica empleada durante la recolección y validación. Cuando la revisión posterior de evidencia determina que el perfil real de un participante no coincide con el prefijo histórico, se conserva el código original por trazabilidad y se documenta explícitamente el perfil correcto.

---

## PAC — Paciente o ex paciente

Ejemplo:

`EV2-PAC-01`

El prefijo `PAC` identifica participantes correspondientes al perfil de paciente o ex paciente relacionado con terapia física o rehabilitación.

Participantes documentados con perfil real de paciente o expaciente:

- `EV2-PAC-01`
- `EV2-PAC-03`
- `EV2-PAC-04`
- `EV2-PAC-05`
- `EV2-PAC-06`
- `EV2-PAC-07`
- `EV2-PAC-08`
- `EV2-PAC-09`
- `FAM-04` *(código histórico conservado; perfil real: paciente/expaciente)*

### Nota sobre `FAM-04`

El código `FAM-04` se conserva por trazabilidad histórica, pero la revisión de la evidencia realizada durante la corrección B1 determinó que el participante corresponde al perfil **paciente/expaciente** y no al perfil familiar/cuidador.

Por esta razón, `FAM-04` debe contabilizarse dentro del perfil PAC en los conteos analíticos vigentes, aunque su código histórico conserve el prefijo `FAM`.

La transcripción de `FAM-04` continúa sujeta al cotejo literal con el audio original requerido en B1.

---

## EFT — Estudiante de fisioterapia

Ejemplo:

`EFT-01`

El prefijo `EFT` identifica participantes correspondientes a estudiantes de fisioterapia que aportaron información relacionada con seguimiento, ejecución y necesidades del proceso terapéutico.

Participantes presentes:

- `EFT-01`
- `EFT-02`
- `EFT-03`

---

## FAM — Familiar o cuidador

Ejemplo:

`FAM-01`

El prefijo `FAM` identifica participantes familiares o cuidadores relacionados con el acompañamiento del paciente durante el proceso de terapia física.

Participantes actualmente clasificados con perfil real de familiar o cuidador:

- `FAM-01`
- `FAM-02`
- `FAM-03`

`FAM-04` no se incluye en este grupo porque su perfil real fue corregido a paciente/expaciente.

---

## FIS — Profesional de fisioterapia

Ejemplo:

`FIS-01`

El prefijo `FIS` identifica al profesional de fisioterapia participante en la investigación.

Participante presente:

- `FIS-01`

---

## NTEC — Usuario no técnico

Ejemplo:

`WALK-NTEC-01`

El prefijo `NTEC` se utiliza para participantes clasificados como usuarios no técnicos dentro de las sesiones de validación walkthrough.

Un usuario no técnico participa en la validación desde la perspectiva de uso, comprensión, necesidades y funcionamiento esperado del sistema.

Participante documentado:

- `WALK-NTEC-01`

Esta sesión se conserva como evidencia complementaria y no se contabiliza dentro de las 16 entrevistas del corpus principal.

---

## TEC — Usuario técnico

Ejemplo:

`WALK-TEC-01`

El prefijo `TEC` se utiliza para participantes clasificados como usuarios técnicos dentro de las sesiones de validación walkthrough.

Un usuario técnico corresponde a una persona cuyo perfil permite realizar una revisión del sistema desde una perspectiva técnica o especializada.

Participante documentado:

- `WALK-TEC-01`

Esta sesión se conserva como evidencia complementaria y no se contabiliza dentro de las 16 entrevistas del corpus principal.

---

## Diferencia entre perfiles

| Código | Perfil | Finalidad |
|---|---|---|
| PAC | Paciente o ex paciente | Aporta necesidades y experiencia relacionada con el seguimiento de terapia física. |
| EFT | Estudiante de fisioterapia | Aporta perspectiva académica y del proceso terapéutico. |
| FAM | Familiar o cuidador | Aporta necesidades relacionadas con acompañamiento y apoyo. |
| FIS | Profesional de fisioterapia | Aporta validación clínica y profesional. |
| TEC | Usuario técnico | Participa en validaciones desde una perspectiva técnica. |
| NTEC | Usuario no técnico | Participa en validaciones orientadas al uso y comprensión del sistema. |

> **Nota de trazabilidad:** el prefijo del código no debe utilizarse como única fuente para determinar el perfil real. Cuando exista una reclasificación documentada, prevalece el perfil registrado en `02_Evidencias/elegibilidad.csv`.

---

## Estado actual de los participantes documentados

Actualmente se encuentran documentados **18 participantes distintos** dentro de la composición vigente utilizada para entrevistas y walkthroughs:

- **9 participantes con perfil paciente/expaciente**
- **3 participantes EFT**
- **3 participantes FAM**
- **1 participante FIS**
- **1 participante NTEC**
- **1 participante TEC**

Total:

```text
9 PAC + 3 EFT + 3 FAM + 1 FIS + 1 NTEC + 1 TEC = 18 participantes
```

De esos 18 participantes:

- **16 corresponden al corpus principal de entrevistas**;
- **2 corresponden a sesiones walkthrough complementarias**.

Los walkthroughs no se contabilizan dentro del corpus principal ni dentro del cálculo de saturación temática.

---

## Códigos públicos documentados

### PAC / paciente o expaciente

- `EV2-PAC-01`
- `EV2-PAC-03`
- `EV2-PAC-04`
- `EV2-PAC-05`
- `EV2-PAC-06`
- `EV2-PAC-07`
- `EV2-PAC-08`
- `EV2-PAC-09`
- `FAM-04` *(código histórico; perfil real PAC)*

### EFT

- `EFT-01`
- `EFT-02`
- `EFT-03`

### FAM

- `FAM-01`
- `FAM-02`
- `FAM-03`

### FIS

- `FIS-01`

### NTEC

- `WALK-NTEC-01`

### TEC

- `WALK-TEC-01`

---

## Archivos históricos o duplicados

Esta carpeta puede contener archivos históricos, variantes de nombre o copias en diferentes extensiones correspondientes al mismo participante.

La existencia de varios archivos para un mismo código no significa que existan varios participantes.

Asimismo, cualquier archivo adicional que no tenga correspondencia verificable en `02_Evidencias/elegibilidad.csv` no debe incorporarse automáticamente al conteo de participantes ni al corpus analítico hasta que su trazabilidad sea revisada.

---

## Relación con las evidencias de validación

Esta carpeta almacena únicamente los consentimientos públicos enmascarados.

Las actas correspondientes a las sesiones walkthrough se almacenan separadamente en:

`../Validacion_Walkthrough/`

Esta separación evita mezclar documentos de autorización con evidencias de ejecución de la técnica.

Las entrevistas del corpus principal se documentan y organizan por separado en las carpetas de transcripciones y demás evidencias asociadas.

---

## Relación con la elegibilidad

La fuente documental utilizada para verificar el perfil real y el estado analítico de cada participante es:

`../elegibilidad.csv`

En particular:

- `FAM-04` conserva un código histórico, pero su perfil real es paciente/expaciente;
- `WALK-NTEC-01` y `WALK-TEC-01` tienen estado complementario;
- las 16 entrevistas del corpus principal se mantienen separadas de los 2 walkthroughs.

Cuando exista una contradicción entre el nombre histórico de un archivo y la clasificación revisada en `elegibilidad.csv`, debe conservarse la trazabilidad del código y utilizarse la clasificación corregida para el análisis.

---

## Verificación

Para verificar las evidencias:

1. Confirmar que cada consentimiento público utiliza un código de participante.
2. Comprobar visualmente que los datos identificables estén enmascarados.
3. Contrastar cada código con `02_Evidencias/elegibilidad.csv`.
4. Verificar que la documentación del material restringido se encuentre en `../00_Restringido/README.md`.
5. Confirmar que el contenedor cifrado se distribuye mediante el Release correspondiente y no como archivo dentro del árbol Git.
6. Contrastar los códigos `WALK-TEC-01` y `WALK-NTEC-01` con sus respectivas actas en `../Validacion_Walkthrough/`.
7. Verificar que `FAM-04` sea tratado analíticamente como paciente/expaciente, manteniendo su código histórico únicamente por trazabilidad.
8. No publicar versiones originales que contengan firmas, cédulas u otros identificadores directos.
9. No asumir que la existencia de un formulario o consentimiento demuestra automáticamente autorización específica para audio, video, fotografías o uso de citas; esa cobertura debe revisarse según las tareas éticas G1–G3.
10. No incorporar al conteo participantes o archivos adicionales cuya trazabilidad no esté documentada.

---

## Limitación ética

La presencia de una copia pública de consentimiento no sustituye la verificación de los consentimientos originales ni demuestra por sí sola cobertura específica para todas las modalidades de evidencia.

La revisión ética del proyecto se documenta en:

`../../08_Etica/declaracion_desviacion_etica.md`

Cuando no pueda demostrarse una autorización específica para determinada evidencia, deberá aplicarse el tratamiento establecido en las tareas éticas correspondientes del plan de mejora.

---

## Proyecto

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Entrega:** Proyecto Fin de Curso — Entrega 4 (2B / Defensa Final)  
**Asignatura:** Ingeniería de Requerimientos
