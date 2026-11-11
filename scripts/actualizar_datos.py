"""Regenera la carpeta data/ del dashboard a partir del Excel de conectividad.

Uso (desde cualquier carpeta):
    python scripts/actualizar_datos.py                 # usa ../resultados/03_tablas_finales/conectividad_por_anio_PC_ECA.xlsx
    python scripts/actualizar_datos.py RUTA_AL_EXCEL   # usa otro Excel con las mismas hojas

Lee las hojas conectividad_por_anio y descriptivos y escribe en data/:
    datos.js                    datos que lee index.html (window.DATOS)
    conectividad_por_anio.csv   solo las 7 variables del dashboard
    descriptivos.csv            hoja descriptivos, tal como está en el Excel
    <copia del Excel>
Requiere pandas y openpyxl.
"""
import json
import shutil
import sys
from pathlib import Path

import pandas as pd

DASHBOARD = Path(__file__).resolve().parents[1]
src = (Path(sys.argv[1]) if len(sys.argv) > 1
       else DASHBOARD.parent / "resultados" / "03_tablas_finales" / "conectividad_por_anio_PC_ECA.xlsx")
out = DASHBOARD / "data"
out.mkdir(exist_ok=True)

x = pd.ExcelFile(src)
anual = x.parse("conectividad_por_anio")
descr = x.parse("descriptivos")

# Solo las variables que muestra el dashboard (dA, dECA, rECA, tipo de cambio y controles quedan en el Excel)
cols = ["anio", "n_nodos", "area_nodos_km2", "PC", "ECA_km2", "ECA_pct_paisaje", "ECA_pct_habitat"]
anual = anual[cols].sort_values("anio")
anual.to_csv(out / "conectividad_por_anio.csv", index=False, encoding="utf-8-sig")
descr.to_csv(out / "descriptivos.csv", index=False, encoding="utf-8-sig")
if src.resolve() != (out / src.name).resolve():
    shutil.copy2(src, out / src.name)

datos = {"anual": {c: anual[c].tolist() for c in cols}}
(out / "datos.js").write_text(
    "// Generado desde " + src.name + " - no editar a mano\nwindow.DATOS = "
    + json.dumps(datos, ensure_ascii=False) + ";\n", encoding="utf-8")

print("Datos actualizados en", out)
print("Años:", anual["anio"].min(), "-", anual["anio"].max(), "| variables:", len(cols) - 1)
