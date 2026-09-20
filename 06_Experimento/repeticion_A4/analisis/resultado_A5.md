# Resultado A5 — fiabilidad y potencia exploratoria

## Datos analizados

- 66 requisitos funcionales.
- 3 evaluadores nuevos.
- 5 dimensiones puntuadas de 1 a 5.
- 330 puntuaciones por evaluador.
- 990 puntuaciones en total.

## Métodos

- ICC(2,1): modelo de dos vías, efectos aleatorios, acuerdo absoluto, evaluador individual.
- ICC(2,k): modelo de dos vías, efectos aleatorios, acuerdo absoluto, promedio de los 3 evaluadores.
- Alfa ordinal: calculado a partir de correlaciones policóricas entre evaluadores.
- IC 95 % del alfa ordinal: bootstrap con hasta 1000 remuestreos por dimensión.
- Kappa de Fleiss: acuerdo entre los 3 evaluadores sobre las cinco categorías de puntuación.

## Resultados

| Dimensión | ICC(2,1) | ICC(2,k) | Alfa ordinal | IC95% alfa | Fleiss κ |
|---|---:|---:|---:|---:|---:|
| Completitud | -0.021 | -0.065 | -0.107 | [-0.737, 0.266] | -0.057 |
| Ausencia de ambigüedad | -0.018 | -0.055 | -0.038 | [-0.671, 0.301] | -0.002 |
| Verificabilidad | -0.082 | -0.294 | -0.350 | [-1.266, 0.135] | -0.041 |
| Corrección respecto a la fuente | 0.019 | 0.056 | 0.033 | [-0.577, 0.399] | 0.024 |
| Consistencia interna | -0.023 | -0.073 | -0.121 | [-0.759, 0.253] | -0.056 |

## Interpretación de la fiabilidad

Los coeficientes obtenidos son cercanos a cero o negativos en la mayoría de las dimensiones. Esto indica que, en esta muestra, el grado de acuerdo entre los tres evaluadores fue bajo.

Los valores negativos de ICC, alfa ordinal o kappa no se reemplazan por cero ni se modifican, ya que corresponden a los resultados producidos por las puntuaciones originales.

Los intervalos de confianza del alfa ordinal son amplios e incluyen valores próximos a cero, por lo que las estimaciones de fiabilidad deben interpretarse con cautela.

Estos resultados deben interpretarse considerando el número reducido de evaluadores y el carácter exploratorio del estudio. No se utilizan como evidencia de equivalencia entre los dos procedimientos.

## Potencia y alcance inferencial

El análisis comparativo utiliza 11 pares temáticos estrictos. Con ese tamaño efectivo, el efecto mínimo detectable declarado para la interpretación del estudio es aproximadamente `dz ≈ 0.94`.

Por esta limitación de tamaño muestral, los resultados se interpretan como **exploratorios**.

La ausencia de significancia estadística no debe interpretarse como demostración de equivalencia entre requisitos humanos y LLM.

## Reproducibilidad

Los resultados de este documento se generan automáticamente mediante:

`06_Experimento/repeticion_A4/analisis/analisis_A5.py`

a partir de las tres hojas originales almacenadas en:

`06_Experimento/repeticion_A4/evaluaciones_completadas/`

Las puntuaciones originales no se modifican durante el análisis.

El intervalo de confianza del alfa ordinal se genera con hasta 1000 remuestreos bootstrap por dimensión y semilla base `20260918`.
