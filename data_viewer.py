import xarray as xr
import geopandas as gpd 
data_perimeter = gpd.read_file(f"data/US_HIST_FIRE_PERIM_2017_DD83.shp")
print(data_perimeter)

