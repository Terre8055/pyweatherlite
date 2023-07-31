from .helpers import SetContextData 
import requests as rq



def fetch_weather_data(func):
    def wrapper(self, *args, **kwargs):
        pkey = kwargs.get('pkey', "")
        city = kwargs.get('city', "")

        self.open_coords_url(pkey, city)
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.get_latitude}&lon={self.get_longitude}&appid={pkey}"
        response = rq.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return func(self, data, *args, **kwargs)
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None

    return wrapper


def legacy_fetch(func):
    def wrapper(self, *args, **kwargs):
        lon = kwargs.get('lon', "")
        lat = kwargs.get('lat', "")
        pkey = kwargs.get('pkey', "")


        self.set_coordinates(lon, lat)
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.get_latitude}&lon={self.get_longitude}&appid={pkey}"
        response = rq.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return func(self, data, *args, **kwargs)
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None

    return wrapper

class Scaffold(SetContextData):
    """Class to retrieve forecast operations
    @get_temp = get current temperature
    @get_humidity = get current humidity
    @get_pressure = get current pressure 
    @get_visibility = get current visibility
    @get_weather_desc = get weather description
    @get_Windspeed = get current windspeed    
    """

    @fetch_weather_data
    def get_temp(self, data, *args, **kwargs):
        temperature = data['main']['temp']
        return temperature

    @fetch_weather_data
    def get_humidity(self, data, *args, **kwargs):
        humidity = data['main']['humidity']
        return humidity
    
    @fetch_weather_data
    def get_pressure(self, data, *args, **kwargs):
        pressure = data['main']['pressure']
        return pressure


    @fetch_weather_data
    def get_visibility(self, data, *args, **kwargs):
        visibility = data['visibility']
        return visibility

    
    @fetch_weather_data
    def get_windspeed(self, data, *args, **kwargs):
        windspeed = data['wind']['speed']
        return windspeed
    
    @fetch_weather_data
    def get_weather_desc(self, data, *args, **kwargs):
        desc = data['weather'][0]['description']
        return desc
    
    @fetch_weather_data
    def get_country(self, data, *args, **kwargs):
        country = data['sys']['country']
        return country


class LegacyScaffold(SetContextData):
    """Class to retrieve forecast operations
    @get_temp = get current temperature
    @get_humidity = get current humidity
    @get_pressure = get current pressure 
    @get_visibility = get current visibility
    @get_weather_desc = get weather description
    @get_Windspeed = get current windspeed    
    """

    @legacy_fetch
    def get_temp(self, data, *args, **kwargs):
        temperature = data['main']['temp']
        return temperature

    @legacy_fetch
    def get_humidity(self, data, *args, **kwargs):
        humidity = data['main']['humidity']
        return humidity
    
    @legacy_fetch
    def get_pressure(self, data, *args, **kwargs):
        pressure = data['main']['pressure']
        return pressure


    @legacy_fetch
    def get_visibility(self, data, *args, **kwargs):
        visibility = data['visibility']
        return visibility

    
    @legacy_fetch
    def get_windspeed(self, data, *args, **kwargs):
        windspeed = data['wind']['speed']
        return windspeed
    
    @legacy_fetch
    def get_weather_desc(self, data, *args, **kwargs):
        desc = data['weather'][0]['description']
        return desc
    
    @legacy_fetch
    def get_country(self, data, *args, **kwargs):
        country = data['sys']['country']
        return country