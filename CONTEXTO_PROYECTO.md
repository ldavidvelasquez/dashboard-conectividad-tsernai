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

## 3. Qué contiene el dashboard

**Encabezado.**
- Título, franja de colores de la leyenda MapBiomas y resumen de los parámetros.
- Debajo hay un selector de periodo (año inicial y final) que filtra las tres pestañas.

**01 · Conectividad anual.**
- Nota con la definición de PC y ECA.
- Fichas con el valor del último año del periodo, más el del primer año como referencia.
- Cinco gráficos:
  - PC por año;
  - ECA por año;
  - ECA frente al área de hábitat: dos líneas con banda gris = hábitat no conectado;
  - ECA como % del área del paisaje;
  - ECA como % del área de hábitat.

**02 · Descriptivos.** Panel visualmente separado, con banda verde oscuro.
- Tabla de n, media, DE, CV, mínimo (año), Q1, mediana, Q3 y máximo (año) para PC, ECA, ECA % del paisaje y ECA % del hábitat.
- Los cuartiles se calculan con el método tipo 7, el de R por defecto.

**03 · Datos por año.** Tabla con las 7 variables y enlaces de descarga.

**Interacción.**
- Al pasar el cursor o tocar un gráfico se ve el valor de cada año.
- Cada pestaña tiene enlace directo: `#anual`, `#descriptivos` y `#datos`.

## 4. Decisiones tomadas por el usuario (respetarlas en cualquier cambio)

1. **Contenido pedido:**
   - gráficos de PC, ECA, ECA frente al área de hábitat, ECA % del paisaje y ECA % del hábitat;
   - tabla de descriptivos;
   - tabla por año solo con las 7 variables indicadas.
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

- **11 de noviembre de 2026:** se creó el dashboard (pestañas 01 a 03) a partir de los resultados de `SALIDAS_CONECTIVIDAD2`.
