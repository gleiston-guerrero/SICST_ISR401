# Desviaciones y observaciones del cuestionario

## H1 — Exportación original y ráfagas de respuestas

### Exportación original

Se conserva una copia sin modificar de la exportación descargada directamente de Google Forms:

`02_Evidencias/Respuestas/exportacion_original_google_forms.xlsx`

Características verificadas de la exportación:

- hoja principal: `Form Responses 1`;
- rango con datos: `A1:Z80`;
- 79 respuestas y 26 columnas;
- la primera columna se denomina `Timestamp`;
- periodo observado: 23/07/2026 21:38:20 a 01/09/2026 09:14:56;
- SHA-256: `e624de7e2d00398eb84e152b441a3cf444bdd58e21c70c175ba12bc53bd41050`.

El hash se conserva en:

`02_Evidencias/Respuestas/exportacion_original_google_forms.sha256`

La versión procesada existente en el repositorio sustituyó el encabezado `Timestamp` por `0`; por ese motivo, la exportación original se conserva separada y no se sobrescribe.

### Ráfagas observadas

Las marcas temporales de la exportación original confirman varios intervalos cortos entre respuestas consecutivas. En total se identifican **31 intervalos menores de 60 segundos**, coincidiendo con la observación del plan de mejora.

#### 02/08/2026

Se registraron **26 respuestas** en dos bloques principales:

- 00:57:34 a 02:05:04: 16 respuestas;
- 08:37:15 a 08:45:04: 10 respuestas.

#### 31/08/2026

Se registraron **13 respuestas consecutivas**, con códigos `EV2-PAC-54` a `EV2-PAC-66`, entre aproximadamente **20:29:33 y 20:37:13**, es decir, en unos **7 minutos y 41 segundos**.

La exportación de Google Forms confirma las marcas temporales, pero por sí sola **no documenta la causa** de la velocidad de respuesta. No se atribuye retrospectivamente una explicación que no esté respaldada por evidencia contemporánea. Si existieron formularios en papel, digitación asistida, aplicación presencial conjunta u otra causa documentada, esa evidencia debe conservarse y citarse aparte.

### Análisis de sensibilidad

Para evaluar cuánto influye la ráfaga del 31/08, se recalcularon indicadores excluyendo únicamente las 13 respuestas `EV2-PAC-54` a `EV2-PAC-66`.

Archivo reproducible de resultados:

`07_Datos/resultados/analisis_sensibilidad_H1.csv`

Resultados principales:

- N total: 79 → 66.
- Pacientes/expacientes: 62 → 49.
- Las medias Likert principales cambian entre **0,07 y 0,17 puntos** en escala 1–5.
- La proporción de respuestas `Si` a “ver el avance” cambia de **84,21 %** a **80,95 %**.
- En aceptación de cámara, la categoría `Si` sin calificativo cambia de **27,63 %** a **14,29 %**.
- La aceptación positiva combinada (`Si` + `Si, pero solo con autorizacion previa`) cambia de **84,21 %** a **80,95 %**.

Por tanto, la exclusión de la ráfaga produce cambios pequeños en las medias generales, pero sí modifica de forma visible la distribución interna de las categorías de aceptación de cámara. Los resultados del cuestionario deben interpretarse teniendo presente esta sensibilidad.

## H2 — Recodificación y normalización de códigos

### Comparación con la versión del 02/08/2026

El commit histórico `2d685cd9bb624c39c5300fcfdb94dbbc52cfb50e` contenía tres códigos que posteriormente fueron corregidos. La comparación se realizó contra la exportación original actual de Google Forms, preservada en `02_Evidencias/Respuestas/exportacion_original_google_forms.xlsx`.

La versión histórica anonimizada no conservaba la columna `Timestamp`; por ello, la correspondencia de los registros se verificó mediante el perfil y el contenido de las respuestas.

| Registro | Código en versión 02/08 | Código en exportación original actual | Explicación |
|---|---|---|---|
| Fisioterapeuta, respuesta del 29/07/2026 01:20:12 | `EV2-ENT-01` | `EV2-ENT-02` | La versión del 02/08 repetía `EV2-ENT-01` para dos fisioterapeutas. La exportación original actual distingue al segundo registro como `EV2-ENT-02`. |
| Fisioterapeuta, respuesta del 01/08/2026 12:40:28 | `EV2-PAC-11` | `EV2-ENT-03` | El código histórico utilizaba el prefijo de paciente para un registro cuyo perfil es fisioterapeuta. La exportación original actual lo identifica como `EV2-ENT-03`. |
| Paciente/expaciente, respuesta del 01/08/2026 14:16:06 | `EV2-ENT-02` | `EV2-PAC-02 ` | El código histórico utilizaba el prefijo de entrevistador/fisioterapeuta para un registro cuyo perfil es paciente/expaciente. La exportación original conserva `EV2-PAC-02 ` con un espacio final; el paso de limpieza lo normaliza a `EV2-PAC-02`. |

Estas tres recodificaciones se documentan como cambios de identificador. No modifican las respuestas asociadas a cada registro.

### Ausencia de `PAC-09` y `PAC-11` en el cuestionario

Después de normalizar los 79 códigos de la exportación original, la secuencia de códigos de paciente contiene `EV2-PAC-01` a `EV2-PAC-78`, con dos ausencias: `EV2-PAC-09` y `EV2-PAC-11`.

- `EV2-PAC-09` no aparece como código de respuesta en la exportación original de Google Forms. Por tanto, su ausencia en el conjunto del cuestionario no fue causada por el paso de limpieza ni por una eliminación posterior.
- `EV2-PAC-11` tampoco aparece como respuesta del cuestionario en la exportación original actual. La versión del 02/08 utilizó históricamente `EV2-PAC-11` para un registro de perfil fisioterapeuta; ese registro corresponde actualmente a `EV2-ENT-03`.
- La existencia de códigos similares en entrevistas, walkthrough u otras evidencias del proyecto no se utiliza para crear retrospectivamente respuestas del cuestionario que no estén presentes en la exportación original.

No se rellenan los números ausentes ni se crean participantes para completar la secuencia.

### Respuestas idénticas de `EV2-PAC-10` y `EVA2-PAC-12`

La exportación original contiene dos registros con contenido de respuesta idéntico en todas las preguntas del cuestionario:

- `EV2-PAC-10`: 01/08/2026 11:28:04.
- `EVA2-PAC-12`: 01/08/2026 12:23:26.

Los registros difieren en la marca temporal y en el código, pero las respuestas del cuestionario coinciden. La exportación por sí sola no permite determinar si se trata de respuestas independientes coincidentes, copia o duplicación. Por integridad, ambos registros se conservan y la coincidencia se documenta sin atribuir una causa no demostrada.

En los datos procesados el código `EVA2-PAC-12` se normaliza únicamente en su identificador a `EV2-PAC-12`; sus respuestas no se alteran.

### Normalización aplicada en el paso de limpieza

El archivo `07_Datos/scripts/02_limpiar_datos.py` realiza la normalización sobre los datos derivados y conserva intactos los datos crudos.

Se aplican estas reglas:

| Valor en exportación/dato crudo | Valor procesado |
|---|---|
| `EV2-PAC-02 ` | `EV2-PAC-02` |
| ` EV2-PAC-41` | `EV2-PAC-41` |
| ` EV2-PAC-42` | `EV2-PAC-42` |
| `EVA2-PAC-12` | `EV2-PAC-12` |

El script valida además que todos los códigos procesados cumplan el patrón `EV2-PAC-##` o `EV2-ENT-##`. La versión procesada resultante conserva **79 filas**, no contiene códigos con espacios iniciales/finales y no contiene prefijos mezclados `EVA2`.
