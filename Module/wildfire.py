import cartopy
import cartopy.feature
import xarray
import datetime as dt
import matplotlib.pyplot as plt


class wildfireMap():
    def __init__(self) -> None:
        self.bounds = {
        "lat_min": 0,
        "lat_max": 0,
        "lon_min": 0,
        "lon_max": 0
        }
        features = []
        dates = []

        wf_perimeters = False
        temprature = False
        wind = False
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
        self.bounds["lon_max"] = lat_max
        return True
    
    def setFeatures(self, **kwargs) -> bool: 
        for feature in kwargs:
            print(f"{feature}")
        return False
    
    def setDates(self, list_of_dates: list):
        return False
    
    def setLayers(self, wind = False, temp = False, wf_perimeter = False):
        return False
    
    def createPlot(self) -> bool:
        plt.clf()
        
        return False
    


    


