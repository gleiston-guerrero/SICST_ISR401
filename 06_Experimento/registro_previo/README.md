# Registro OSF — experimento SICST

## Identificación

- **Registro:** https://osf.io/82q76/
- **DOI:** `10.17605/OSF.IO/82Q76`
- **ID:** `82q76`
- **Fecha UTC del registro original:** `2026-09-13T00:50:38.265668Z`
- **Hora Ecuador continental (UTC-5):** `2026-09-12 19:50:38`

## Actualización pública del registro — 21/09/2026

El registro OSF `82q76` fue actualizado públicamente el 21/09/2026 para
corregir la cronología declarada en la versión original.

La actualización reconoce expresamente que, al momento del registro original,
ya existían datos y artefactos relevantes para el estudio, incluidas las
entrevistas de campo, el conjunto de requisitos generado mediante LLM y las
hojas correspondientes a la evaluación original.

Por esta razón, el registro se considera retrospectivo respecto de esas fases
del estudio y los análisis derivados se documentan como exploratorios, no como
análisis confirmatorios preregistrados.

La actualización fue realizada desde la cuenta del integrante responsable de
la subsanación, con permisos administrativos otorgados sobre el mismo registro.
No se creó un registro nuevo ni se modificaron o retrofecharon los artefactos
originales.

- **Registro público:** https://osf.io/82q76/
- **Fecha de actualización:** 21/09/2026
- **Evidencia API posterior a la actualización:** `consulta_actualizada_2026-09-21.json`

## Evidencia de esta carpeta

- `consulta.json` — respuesta de la API pública de OSF conservada como
  evidencia del estado previo del registro `82q76`.
- `consulta_actualizada_2026-09-21.json` — respuesta de la API pública
  obtenida después de la actualización del registro.
- `osf_registration.pdf` — exportación legible conservada de la página del
  registro.

## Alcance temporal

Las entrevistas del SICST fueron realizadas previamente como parte de la
elicitación de requisitos.

El registro OSF corresponde al **experimento comparativo humano-LLM**. Esa
fase utiliza las transcripciones anonimizadas existentes como corpus fuente
fijo.

La marca temporal del registro original (2026-09-12, 19:50 hora Ecuador) es
**posterior**, no anterior, a la generación del conjunto de requisitos LLM y
a la recolección de las puntuaciones de la evaluación original con origen no
indicado en la hoja.

Los metadatos internos de las cuatro hojas de evaluación originales registran
su último guardado el 2026-09-12 entre las 13:11 y las 13:16 hora Ecuador,
más de seis horas antes del registro. El conjunto LLM se generó ese mismo día,
antes de la sesión de evaluación.

Por lo tanto, el registro es retrospectivo respecto de las tres fases del
estudio:

- entrevistas de campo;
- generación del conjunto LLM;
- evaluación original con origen no indicado en la hoja.

El análisis estadístico se reporta como **exploratorio**, no como
confirmatorio preregistrado, en concordancia con esta cronología real.

No se modifican ni retrofechan los artefactos originales para aparentar una
cronología diferente.

## Verificación de las evidencias JSON

Desde la raíz del repositorio:

```bash
python -m json.tool 06_Experimento/registro_previo/consulta.json > /dev/null
python -m json.tool 06_Experimento/registro_previo/consulta_actualizada_2026-09-21.json > /dev/null
```

Para consultar nuevamente la API pública:

```bash
curl -sS https://api.osf.io/v2/registrations/82q76/
```
