import pandas as gp
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import sys


df = gp.read_excel('E:/_testExcelSql/clientes_xy.xlsx')

# Filtrado vectorizado en un solo paso
mask = (df['lat'] != -90) & (df['Comuna'] == 'TALCAHUANO')
df = df[mask].copy()
'''
# elimina registros anomalos
df = df[df['lat'] != -90].copy() 

# selecciona comuna
df = df[df['Comuna'] == 'TALCAHUANO'].copy() 
'''
   # 5. Verificar nuevamente si el DataFrame está vacío después del filtrado
if df.empty:
        print("No hay registros válidos después del filtrado. Terminando ejecución.")
        sys.exit(0)

# Convertir DataFrame a GeoDataFrame
gdf = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df['lng'], df['lat']),
    crs="EPSG:4326"  # Sistema de coordenadas WGS84
)

# Visualizar
fig, ax = plt.subplots(figsize=(10,10))
gdf.plot(ax=ax, color='red', markersize=5, aspect=1)

# Añadir contexto de mapa (requiere contextily)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
'''
plt.title('Distribución de Clientes')
plt.show()
'''