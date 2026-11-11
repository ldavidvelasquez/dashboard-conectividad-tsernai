# Dashboard de conectividad del hábitat de T. sernai

Antes de hacer cualquier cosa en esta carpeta, lee el contexto completo del proyecto:

@CONTEXTO_PROYECTO.md

Reglas clave:
- Responde en español.
- Valores observados: sin modelos ni ajustes estadísticos. La única síntesis es la tabla de descriptivos, que pidió el usuario.
- La tabla de conectividad por año muestra solo `anio`, `n_nodos`, `area_nodos_km2`, `PC`, `ECA_km2`, `ECA_pct_paisaje` y `ECA_pct_habitat`. La segunda tabla muestra el PC observado frente al PC máximo posible.
- No agregues notas de interpretación sobre los gráficos: el usuario pidió quitarlas.
- Mantén la paleta MapBiomas y el diseño del dashboard de fragmentación.
- Antes de hacer push a GitHub, muestra una vista previa local (abre `index.html`) y espera la aprobación del usuario.
- Los datos se regeneran con `python scripts/actualizar_datos.py`. No edites `data/datos.js` a mano.
