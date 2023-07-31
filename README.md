# pyweatherlite Documentation

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Terre8055/pycloudlib.svg)](https://github.com/Terre8055/pycloudlib/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Terre8055/pycloudlib.svg)](https://github.com/Terre8055/pycloudlib/network)
[![GitHub issues](https://img.shields.io/github/issues/Terre8055/pycloudlib.svg)](https://github.com/Terre8055/pycloudlib/issues)

A lightweight Python library to extract weather data from OpenWeatherMap.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Getting Started](#getting-started)
  - [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Introduction

`pyweatherlite` is a simple and easy-to-use Python library that allows you to retrieve weather data from OpenWeatherMap. It provides convenient methods to access various weather attributes such as temperature, humidity, pressure, wind speed, and more.

Key features:

- Lightweight and easy to integrate into your projects.
- Flexible configuration to use your API key and location for weather data retrieval.
- Support for fetching weather data based on latitude and longitude.

## Installation

You can install `pyweatherlite` using `pip`:


## Usage

### Getting Started

To use `pyweatherlite`, you'll need to sign up for an API key from OpenWeatherMap (https://openweathermap.org/api). Once you have the API key, you can use the library to retrieve weather data for various attributes.

Here's a simple example to get the current temperature:

```python
from pyweatherlite.index import Scaffold, LegacyScaffold

# Set your OpenWeatherMap API key and City
api_key = "YOUR_API_KEY"
city = "YOUR_CITY_NAME"

# Create a WeatherFetcher instance
inst = Scaffold()

# Get the current temperature for a specific city
temperature = inst.get_temp(pkey=apikey, city="London")

print(f"The current temperature in London is {temperature}°C.")

# Assuming you have your city coordinates then use LegacyScaffold
inst = LegacyScaffold()

api_key = "YOUR_API_KEY"
longitude = "YOUR_LONGITUDE_COORD"
latitude = "YOUR_LATITUDE_COORD"

# Get the current temperature for a specific coordinates
temperature = inst.get_temp(pkey=apikey, lon=longitude, lat=latitude)

print(f"The current temperature is {temperature}°C.")
```
### Contributing

We welcome contributions from the community! If you have any bug fixes, improvements, or new features to add, feel free to open a pull request on our GitHub repository. Please ensure that your code follows the project's coding guidelines.

### License

This project is licensed under the MIT License. 

### Credits

    Author: Michael Appiah Dankwah (https://github.com/Terre8055)