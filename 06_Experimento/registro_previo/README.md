# Registro OSF — experimento SICST

## Identificación

- **Registro:** https://osf.io/82q76/
- **DOI:** `10.17605/OSF.IO/82Q76`
- **ID:** `82q76`
- **Fecha UTC:** `2026-09-13T00:50:38.265668Z`
- **Hora Ecuador continental (UTC-5):** `2026-09-12 19:50:38`

## Evidencia de esta carpeta

- `consulta.json` — respuesta guardada de la API pública de OSF para el
  registro `82q76`.
- `osf_registration.pdf` — exportación legible de la página del registro.

## Alcance temporal (corregido el 18/09/2026)

Las entrevistas del SICST fueron realizadas previamente como parte de la
elicitación de requisitos.

El registro OSF corresponde al **experimento comparativo humano-LLM**. Esa
fase utiliza las transcripciones anonimizadas existentes como corpus fuente
fijo.

**Corrección respecto de una versión anterior de este README:** la marca
temporal del registro (2026-09-12, 19:50 hora Ecuador) es **posterior**,
no anterior, a la generación del conjunto de requisitos LLM y a la
recolección de las puntuaciones de la evaluación original con origen no indicado en la hoja.

Los metadatos internos de las cuatro hojas de evaluación originales registran su
último guardado el 2026-09-12 entre las 13:11 y las 13:16 hora Ecuador,
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

## Verificación de `consulta.json`

Desde la raíz del repositorio:

```bash
python -m json.tool 06_Experimento/registro_previo/consulta.json > /dev/null
```

Para consultar nuevamente la API pública:

```bash
curl -sS https://api.osf.io/v2/registrations/82q76/
```
