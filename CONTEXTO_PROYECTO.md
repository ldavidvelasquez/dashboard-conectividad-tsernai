# Contexto del proyecto: Dashboard de conectividad del hábitat de *T. sernai*

Última actualización: 11 de noviembre de 2026.

## 1. Propósito

Dashboard web público con los **valores anuales observados (1986–2024)** de la conectividad funcional del hábitat idóneo de *Thryophilus sernai*. Sirve para compartir los resultados con cualquier persona mediante un enlace, desde el celular o desde el computador.

Sigue el diseño del dashboard de fragmentación (`Salidas_fragmentacion/SALIDAS_22/resultados/01_metricas/DASHBOARD`, https://ldavidvelasquez.github.io/dashboard-fragmentacion-tsernai/).

- **Enlace público:** https://ldavidvelasquez.github.io/dashboard-conectividad-tsernai/
- **Repositorio:** https://github.com/ldavidvelasquez/dashboard-conectividad-tsernai (público, rama `main`, publicado con GitHub Pages desde la raíz)
- **Cuenta de GitHub:** `ldavidvelasquez`

## 2. Origen de los datos

- **Fuente única:** `../resultados/03_tablas_finales/conectividad_por_anio_PC_ECA.xlsx`, en la carpeta `SALIDAS_CONECTIVIDAD2`.
- **Scripts que generaron el Excel:** `SALIDAS_CONECTIVIDAD2/00_configuracion.R` a `03_tablas_graficos.R`, o el script único `replicar_conectividad_PC_ECA.R`.
- **Método:** se documenta en `SALIDAS_CONECTIVIDAD2/Informe_tecnico_conectividad_PC_ECA.docx`. En resumen:
  - `Makurhini::MK_dPCIIC()` con todos los parches de hábitat como nodos (vecindad de 8 celdas, sin umbral de área);
  - distancias de costo mínimo entre bordes de parches sobre la matriz de resistencia de cada año;
  - dispersión de 3,12 km por la cobertura más permeable, con probabilidad de 0,5;
  - área del paisaje de 2 422,97 km².

| Hoja del Excel | Uso en el dashboard |
|---|---|
| `conectividad_por_anio` | Pestañas 01 y 03. Solo las variables `anio`, `n_nodos`, `area_nodos_km2`, `PC`, `ECA_km2`, `ECA_pct_paisaje` y `ECA_pct_habitat` |
| `descriptivos` | Descarga de la pestaña 02. La tabla se recalcula en el navegador para el periodo elegido; con la serie completa coincide con esta hoja |
| `medias_por_periodo`, `comparacion_nodos_1ha`, `control_nodos_S22` | No se usan |

**Variables calculadas por `scripts/actualizar_datos.py`.** No están en el Excel.
- `hab_pct_paisaje` = 100 · `area_nodos_km2` / LA.
- `PC_max` = (`area_nodos_km2` / LA)²: el PC que habría si todo el hábitat fuera un único parche continuo.
- `PC_obs_max_pct` = 100 · `PC` / `PC_max`, que equivale a (`ECA_pct_habitat`)² / 100. El script lo verifica.

LA se obtiene del propio Excel: LA = 100 · `ECA_km2` / `ECA_pct_paisaje` = 2 422,97 km².

## 3. Qué contiene el dashboard

**Encabezado.**
- Título, franja de colores de la leyenda MapBiomas y resumen de los parámetros.
- Debajo hay un selector de periodo (año inicial y final) que filtra las tres pestañas.

**01 · Conectividad anual.**
- Nota con tres definiciones, todas con el texto que eligió el usuario:
  - PC, solo la primera frase de su texto;
  - "PC observado / máximo separa la conectividad de la cantidad de hábitat";
  - ECA.
- Fichas con el valor del último año del periodo, más el del primer año como referencia.
- Ocho gráficos en cuatro grupos:
  - **Conectividad funcional:** PC por año; ECA por año.
  - **PC observado frente al PC máximo posible:**
    - PC máximo posible frente a PC observado: dos líneas; la banda gris es la conectividad perdida por la separación entre parches;
    - Hábitat (% del paisaje);
    - PC observado / máximo.
  - **ECA frente al área de hábitat:** dos líneas; la banda gris es el hábitat no conectado.
  - **ECA normalizado:** ECA como % del área del paisaje; ECA como % del área de hábitat.
- Cada gráfico lleva título, una fórmula o definición breve y el nombre de la variable. Sin notas de interpretación: el usuario pidió quitarlas.

**02 · Descriptivos.** Panel visualmente separado, con banda verde oscuro.
- Tabla de n, media, DE, CV, mínimo (año), Q1, mediana, Q3 y máximo (año) para PC, ECA, ECA % del paisaje y ECA % del hábitat.
- Los cuartiles se calculan con el método tipo 7, el de R por defecto.

**03 · Datos por año.** Dos tablas con enlaces de descarga:
- conectividad por año, con las 7 variables;
- PC observado frente al PC máximo posible: año, hábitat (% del paisaje), PC máximo posible, PC observado y PC observado / máximo.

**Interacción.**
- Al pasar el cursor o tocar un gráfico se ve el valor de cada año.
- Cada pestaña tiene enlace directo: `#anual`, `#descriptivos` y `#datos`.

## 4. Decisiones tomadas por el usuario (respetarlas en cualquier cambio)

1. **Contenido pedido:**
   - gráficos de PC, ECA, ECA frente al área de hábitat, ECA % del paisaje y ECA % del hábitat;
   - tabla de descriptivos;
   - tabla por año solo con las 7 variables indicadas.
   - Añadido el 11 de noviembre:
     - definición del PC con el texto literal del usuario;
     - gráficos de PC máximo posible frente a PC observado, Hábitat (% del paisaje) y PC observado / máximo;
     - tabla del PC observado frente al máximo.
   - Después el usuario pidió:
     - quitar de las definiciones las frases sobre el 17 % del paisaje, la fórmula del PC máximo posible y la de distancias de costo mínimo;
     - quitar las notas "Cómo leerlo" de los gráficos.
2. **Mismo diseño que el dashboard de fragmentación:** estética sobria, técnica y profesional, con la paleta de la leyenda de **MapBiomas**.
3. **Valores observados:** sin modelos, tendencias ajustadas ni pruebas. La única síntesis estadística es la tabla de descriptivos, que el usuario pidió.
4. **Optimizado para celular y computador.** Se verificó a 390 px (dentro de un iframe) y a 1366 px de ancho, sin desplazamiento horizontal de la página.
5. **Mostrar una vista previa local antes de publicar** cualquier cambio en GitHub.

## 5. Colores (leyenda MapBiomas)

Todos tienen un contraste de 4:1 o más sobre fondo blanco.

| Grupo | Color | Clase MapBiomas | Variables |
|---|---|---|---|
| Hábitat (nodos) | `#1f8d49` | Formación boscosa | `n_nodos`, `area_nodos_km2` |
| Conectividad funcional | `#2532e4` | Río, lago u océano | `PC`, `ECA_km2` |
| ECA normalizado | `#026975` | Formación forestal inundable | `ECA_pct_paisaje`, `ECA_pct_habitat` |

- **Verde oscuro de la banda del panel 02:** `#04381d` (Manglar).
- **Tema:** solo claro, sin modo oscuro.

## 6. Estructura de esta carpeta

```
DASHBOARD/
├── index.html               # todo el dashboard: HTML + CSS + JS (sin librerías; gráficos en SVG propio)
├── data/
│   ├── datos.js             # datos que lee index.html (generado, no editar a mano)
│   ├── conectividad_por_anio.csv
│   ├── pc_maximo_por_anio.csv
│   ├── descriptivos.csv
│   └── conectividad_por_anio_PC_ECA.xlsx   # copia del Excel original
├── scripts/
│   └── actualizar_datos.py  # regenera data/ desde el Excel
├── README.md                # portada del repositorio en GitHub
├── CONTEXTO_PROYECTO.md     # este documento
├── CLAUDE.md                # instrucciones para Claude Code (importa este documento)
├── .nojekyll                # GitHub Pages sirve los archivos tal cual
└── .git/
```

En `index.html` las variables se definen en el arreglo `M` (nombre en español, unidad, decimales, grupo y descripción) y los colores en `GRUPOS`.

## 7. Cómo actualizar

**Si cambia el Excel (por ejemplo, al repetir el análisis):**
1. Ejecuta `python scripts/actualizar_datos.py`. Por defecto usa `../resultados/03_tablas_finales/conectividad_por_anio_PC_ECA.xlsx`; si quieres otro archivo, pásalo como argumento.
2. Abre `index.html` en el navegador y revisa los cambios.
3. Publica:
   ```
   git add -A
   git commit -m "Actualiza datos"
   git push
   ```
   GitHub Pages se actualiza en 1 o 2 minutos y el enlace no cambia.

**Si cambia el diseño:** edita `index.html`, revisa la vista previa local y publica igual que en el paso 3.

**Herramientas en este equipo:**
- **Git y GitHub CLI:** GitHub CLI está en `C:\Program Files\GitHub CLI\gh.exe` y tiene sesión iniciada con `ldavidvelasquez`.
- **Python:** versión 3.13, con pandas y openpyxl.
- **Capturas de verificación:** se hacen con Edge sin ventana (`msedge.exe --headless=new --screenshot`). Edge sin ventana no baja de unos 500 px de ancho; para verificar a 390 px, carga la página dentro de un iframe de 390 px.

## 8. Historial

- **11 de noviembre de 2026:**
  - Se creó el dashboard (pestañas 01 a 03) a partir de los resultados de `SALIDAS_CONECTIVIDAD2` y se publicó en GitHub Pages.
  - Se añadieron la comparación del PC observado con el PC máximo posible (tres gráficos y una tabla) y la definición del PC.
