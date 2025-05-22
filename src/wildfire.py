import cartopy
import cartopy.feature
import xarray as xr
import datetime as dt
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import imageio
import os

import geopandas as gpd

DATA_DIR = "test"
MERRA2_VARS = {
    "temperature": "TLML",
    "pressure": "PS",
    "humidity": "QLML",
    "surface_height": "HLML",
    "wind_speed": "SPEEDLML"
}

class wildfireMap():
    def __init__(self) -> None:
        self.bounds = {
        "lat_min": -90,
        "lat_max": 90,
        "lon_min": -180,
        "lon_max": 180
        }
        self.features = []
        self.dates = []

        self.wf_perimeters = True
        self.temprature = False
        self.wind = False
        return None
    
    def helloWorld(self) -> None:
        '''Prints Hello World'''
        print("Hello World")

    def savePlt(self, fileLocation: str, fileType: str = "png") -> str:
        '''Saves the current matlibplot plt to the given file location.\n
        The filetype determines what the image is saved as. Default is png'''
        return None
    
    def testPlt(self):
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        return None
    
    def showPlt(self) -> None:
        '''Shows the current matlibplot'''
        plt.show()
        return None
    
    def setBounds(self, lat_min: float, lat_max: float, lon_min: float, lon_max: float) -> bool:
        self.bounds["lat_min"] = lat_min
        self.bounds["lat_max"] = lat_max
        self.bounds["lon_min"] = lon_min
        self.bounds["lon_max"] = lon_max
        return True
    
    def setFeatures(self, **kwargs) -> bool: 
        for feature in kwargs:
            print(f"{feature}")
        return False
    
    def setDates(self, list_of_dates: list):
        self.dates.extend(list_of_dates) 
        return False
    
    def setLayers(self, wind = False, temp = False, wf_perimeter = False) -> None:
        if wind:
            self.wind = wind
        if temp:
            self.temp = temp
        if wf_perimeter:
            self.wf_perimeter = wf_perimeter

    
    def createPlot(self) -> bool:
        for date in self.dates:
            date_np = np.datetime64(date)

            year = date_np.astype('datetime64[Y]').astype(int) + 1970
            month = date_np.astype('datetime64[M]').astype(int) % 12 + 1
            day = (date_np - date_np.astype('datetime64[M]')).astype(int) + 1


            ds_merra2 = xr.open_dataset(f"MERRA2_100.inst1_2d_lfo_Nx.{year}{month:02}{day:02}.nc4")
            ds_perimeter = xr.open_dataset(f"data/US_HIST_FIRE_PERIM_2017_DD83.shp")
            print(ds_perimeter)

            temperature = ds_merra2[MERRA2_VARS["temperature"]]

            lat = ds_merra2["lat"]
            lon = ds_merra2["lon"]


            #initialize 0-23 time

            current_time = np.datetime64(date, 'h')
            end_time = current_time + np.timedelta64(23, 'h')

            if self.wf_perimeter:
                data_perimeter = gpd.read_file(f"data/US_HIST_FIRE_PERIM_2017_DD83.shp")
                data_perimeter = data_perimeter.to_crs(epsg=4326, inplace=True)


            
            image_list = []
            while current_time <= end_time:
                plt.close()
                temp_time = temperature.sel(time=current_time)


                ax = plt.axes(projection=ccrs.PlateCarree())
                ax.set_extent([
                    self.bounds["lon_min"], self.bounds["lon_max"],
                    self.bounds["lat_min"], self.bounds["lat_max"]
                ])            
                ax.add_feature(cfeature.COASTLINE)
                ax.add_feature(cfeature.LAND)
                ax.add_feature(cfeature.OCEAN)
                ax.add_feature(cfeature.BORDERS, linestyle=':')
                ax.add_feature(cfeature.STATES, linestyle=':')
                ax.set_title(f"Temperature at {current_time} UTC")
                p = ax.pcolormesh(
                    lon, lat, temp_time,
                    transform=ccrs.PlateCarree(),
                    cmap='coolwarm',
                    shading='auto',
                    vmax=310,
                    vmin=250
                )
                if not os.path.isdir("output"):
                    os.mkdir("output")
                plt.colorbar(p, ax=ax, orientation='vertical', label='Temperature (K)')
                plt.tight_layout()
                image_list.append(f"./output/{current_time}.png")
                plt.savefig(f"./output/{current_time}.png")
                plt.close()
                current_time += np.timedelta64(1, 'h')
            images = []
            for file in image_list:
                images.append(imageio.imread(file))
            imageio.mimsave(f"./output/{date}.gif" , images, fps=5, format='GIF-PIL')
            for image in image_list:
                os.remove(image)






        return False
    
    



    


