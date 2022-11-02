import requests
from math import *

api_key = '' # Your API key
city = str(input("Podaj miasto: "))

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + city

weather_data = requests.get(base_url).json()

def get_temperature():
    temperature = weather_data['main']['temp'] - 273.15
    return f"W {city.capitalize()} jest {round(temperature)} °C"

def get_description():
    description = weather_data['weather'][0]['description']
    return f"{description}"

def get_wind():
    wind = weather_data['wind']['speed']
    return f"Wiatr: {round(wind)} km/h"

def get_pressure():
    pressure = weather_data['main']['pressure']
    return f"Ciśnienie w {city.capitalize()} wynosi {round(pressure)} hPa"

def get_humidity():
    humidity = weather_data['main']['humidity']
    return f"Wilgotność w {city.capitalize()} wynosi {round(humidity)} %"

def show_weather():
    print(get_temperature())
    print(get_description())
    print(get_wind())
    print(get_pressure())
    print(get_humidity())

# print(json.dumps(weather_data))
# print(weather_data)

if __name__ == '__main__':
    show_weather()
