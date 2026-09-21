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

## H2

Pendiente documentar aquí la tabla antes/después de recodificación de códigos, conforme al plan de mejora.
