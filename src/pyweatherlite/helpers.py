from .Base import BaseClass
import requests as rq


"""Module that defines classes with instance specific modules"""


class SetContextData(BaseClass):
    """Set data to parent class instance variables

    Args:
        BaseClass (_type_): Parent class
    """

    def set_coordinates(
            self,
            longitude:float = 0.00,
            latitude:float = 0.00
    ):
        """Set coordinates for lon and lat"""

        self._longitude = longitude
        self._latitude = latitude
        
    def open_coords_url(self, pkey:str = "", city:str = "London",):
        """Return long and lat coords.\
        City defaults to London if not defined
            """
        
        _user_city = city
        _user_pkey = pkey

        if city:
            try:
                url_def = rq.get("https://api.openweathermap.org/geo/1.0/direct?q={},&appid={}".format(_user_city, _user_pkey))
                url_def.raise_for_status()  # Raise HTTPError for non-2xx responses
            except rq.exceptions.RequestException as e:
                print(f"Error getting data: {e}")

        
        if url_def is not None:                
            lon = url_def.json()[0]['lon']
            lat = url_def.json()[0]['lat']

            self.set_coordinates(lon, lat)

        

 