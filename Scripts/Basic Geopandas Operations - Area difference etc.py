# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:16:11 2019

@author: MMann
"""

from shapely.geometry import Point
import pandas as pd
import geopandas as gp
import os
 
os.chdir(r'C:/Users/mmann/Google Drive/HousingLife/Historic Designation/data/')
#%%
def proj_and_area(file):
    file= file.to_crs({'init': 'epsg:26918'})
    file["area"] = file['geometry'].area/ 10**6  #km/sqr 
    return file
    
afford = gp.read_file('./Affordable_Housing/Affordable_Housing_simple_clean.geojson')
water = gp.read_file('./Waterbodies/Waterbodies.shp')
hd = gp.read_file('./Historic_Districts/Historic_Districts.geojson')
zoning = gp.read_file('./Zoning_Regulations_of_2016/Zoning_Regulations_of_2016.geojson')
sf = gp.read_file('./Zoning_Regulations_of_2016/R1_3.geojson')

# find area developable - remove commercial, and other non res types
zoning = zoning[~zoning['ZONING_LAB'].isin(['ARTS-1','ARTS-2','ARTS-3','ARTS-4','D-7','D-8','HE-1','HE-2','HE-3','HE-4','StE-11',  
                                           'StE-12',  'StE-13',  'StE-14',  'StE-15',  'StE-16',  'StE-17',  'StE-18',  'StE-19',   'StE-2',   'StE-3', 
                                           'StE-4',   'StE-5',   'StE-6',   'StE-7',   'StE-8',   'StE-9','WR-1','WR-2','WR-3','WR-4',    
                                           'WR-5','WR-6','WR-7','WR-8', 'CG-1','CG-2','CG-3','CG-4','CG-5','CG-6','CG-7', 'UNZONED'])]

avaiable = gp.overlay(zoning, water, how='difference')
avaiable = gp.overlay(avaiable, hd, how='difference')
avaiable = gp.overlay(avaiable, sf, how='difference')

 
# reproject and add area 
afford,water,hd,zoning= ( proj_and_area(item) for item in [afford,water,hd,zoning])

#%%

avaiable.to_file('./Zoning_Regulations_of_2016/remaining_not_sf_hd_water_commercial.geojson', driver="GeoJSON")
