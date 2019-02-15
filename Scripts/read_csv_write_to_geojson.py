
from geopandas import GeoDataFrame
from shapely.geometry import Point
import pandas as pd
import geopandas as gp


df = pd.read_csv(r'C:\Users\mmann\Google Drive\HousingLife\Historic Designation\data\Affordable_Housing\Affordable_Housing_simple_clean.csv')


#%%


geometry = [Point(xy) for xy in zip(df.LONGITUDE, df.LATITUDE)]
df = df.drop(['LONGITUDE', 'LATITUDE'], axis=1)
crs = {'init': 'epsg:4326'}
gdf = GeoDataFrame(df, crs=crs, geometry=geometry)
gdf.crs = {'init' :'epsg:4326'}

gdf.to_crs({'init': 'epsg:4326'})

#%%
gdf.to_json()
gdf.to_file(r'.\Google Drive\HousingLife\Historic Designation\data\Affordable_Housing\Affordable_Housing_simple_clean2.geojson', 
            driver='GeoJSON')