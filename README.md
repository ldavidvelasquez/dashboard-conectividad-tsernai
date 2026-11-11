# Conectividad funcional del hábitat idóneo de *Thryophilus sernai* (1986–2024)

Dashboard web con los valores anuales observados de la probabilidad de conectividad (PC) y el área conectada equivalente (ECA) del hábitat idóneo de *Thryophilus sernai*. Los valores se calcularon con `Makurhini::MK_dPCIIC()` usando todos los parches de hábitat como nodos, distancias de costo mínimo entre bordes de parches y una dispersión de 3,12 km con probabilidad 0,5.

**Ver el dashboard:** https://ldavidvelasquez.github.io/dashboard-conectividad-tsernai/

## Contenido

| Pestaña | Qué muestra |
|---|---|
| 01 · Conectividad anual | Series temporales de PC, ECA, ECA frente al área de hábitat, ECA como % del área del paisaje y ECA como % del área de hábitat |
| 02 · Descriptivos | n, media, desviación estándar, CV, mínimo, cuartiles y máximo de PC, ECA y ECA normalizado para el periodo seleccionado |
| 03 · Datos por año | Tabla anual con nodos, área de hábitat, PC, ECA y ECA normalizado |

Los gráficos y la tabla anual presentan valores observados; no incluye modelos ni ajustes estadísticos.

## Datos

- [`data/conectividad_por_anio_PC_ECA.xlsx`](data/conectividad_por_anio_PC_ECA.xlsx): archivo original.
- [`data/conectividad_por_anio.csv`](data/conectividad_por_anio.csv): las 7 variables del dashboard.
- [`data/descriptivos.csv`](data/descriptivos.csv): estadísticos descriptivos de la serie completa.
- `data/datos.js`: los mismos datos en el formato que lee el dashboard.

Colores basados en la leyenda de coberturas y usos del suelo de MapBiomas.
