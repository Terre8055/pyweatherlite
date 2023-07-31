import unittest
from src.pycloudlib.index import Scaffold, LegacyScaffold

class TestScaffold(unittest.TestCase):

    def test_get_temp(self):
        # Test the API response for get_temp method
        s = Scaffold()

        temperature = s.get_temp(pkey="a98d0f2d0f6973a5203ba90cff1f2807", city="London")
        self.assertIsInstance(temperature, float)
        self.assertIsNotNone(temperature)


    def test_get_humidity(self):
        # Test the API response for get_humidity method
        s = Scaffold()

        humidity = s.get_humidity(pkey="a98d0f2d0f6973a5203ba90cff1f2807", city="London")
        self.assertIsNotNone(humidity)


    def test_get_pressure(self):
        # Test the API response for get_pressure method
        s = Scaffold()

        pressure = s.get_pressure(pkey="a98d0f2d0f6973a5203ba90cff1f2807", city="London")
        self.assertIsNotNone(pressure)


    def test_get_visibility(self):
        # Test the API response for get_visibility method
        s = Scaffold()

        visibility = s.get_visibility(pkey="a98d0f2d0f6973a5203ba90cff1f2807", city="London")
        self.assertIsNotNone(visibility)


    def test_get_windspeed(self):
        # Test the API response for get_windspeed method
        s = Scaffold()

        ws = s.get_windspeed(pkey="a98d0f2d0f6973a5203ba90cff1f2807", city="London")
        self.assertIsNotNone(ws)

    def test_get_wdesc(self):
        # Test the API response for get_weather_desc method
        s = Scaffold()

        wd = s.get_weather_desc(pkey="a98d0f2d0f6973a5203ba90cff1f2807", city="London")
        self.assertIsInstance(wd, str)
        self.assertIsNotNone(wd)

    def test_get_country(self):
        # Test the API response for get_country method
        s = Scaffold()

        wd = s.get_country(pkey="a98d0f2d0f6973a5203ba90cff1f2807", city='London')
        self.assertIsNotNone(wd)
        self.assertTrue(wd, 'GB')



class TestLegacyScaffold(unittest.TestCase):

    def test_get_temp(self):
        # Test the API response for get_temp method
        s = LegacyScaffold()

        temperature = s.get_temp(pkey="a98d0f2d0f6973a5203ba90cff1f2807", lon=5.5571096, lat=5.5571096)
        self.assertIsInstance(temperature, float)
        self.assertIsNotNone(temperature)


    def test_get_humidity(self):
        # Test the API response for get_humidity method
        s = LegacyScaffold()

        humidity = s.get_humidity(pkey="a98d0f2d0f6973a5203ba90cff1f2807", lon=5.5571096, lat=5.5571096)
        self.assertIsNotNone(humidity)


    def test_get_pressure(self):
        # Test the API response for get_pressure method
        s = LegacyScaffold()

        pressure = s.get_pressure(pkey="a98d0f2d0f6973a5203ba90cff1f2807", lon=5.5571096, lat=5.5571096)
        self.assertIsNotNone(pressure)


    def test_get_visibility(self):
        # Test the API response for get_visibility method
        s = LegacyScaffold()

        visibility = s.get_visibility(pkey="a98d0f2d0f6973a5203ba90cff1f2807", lon=5.5571096, lat=5.5571096)
        self.assertIsNotNone(visibility)


    def test_get_windspeed(self):
        # Test the API response for get_windspeed method
        s = LegacyScaffold()

        ws = s.get_windspeed(pkey="a98d0f2d0f6973a5203ba90cff1f2807", lon=5.5571096, lat=5.5571096)
        self.assertIsNotNone(ws)

    def test_get_wdesc(self):
        # Test the API response for get_weather_desc method
        s = LegacyScaffold()

        wd = s.get_weather_desc(pkey="a98d0f2d0f6973a5203ba90cff1f2807", lon=5.5571096, lat=5.5571096)
        self.assertIsInstance(wd, str)
        self.assertIsNotNone(wd)

    def test_get_country(self):
        # Test the API response for get_country method
        s = LegacyScaffold()

        wd = s.get_country(pkey="a98d0f2d0f6973a5203ba90cff1f2807", lon=5.5571096, lat=5.5571096)
        self.assertIsInstance(wd, str)
        self.assertIsNotNone(wd)
        self.assertTrue(wd, 'GH')
