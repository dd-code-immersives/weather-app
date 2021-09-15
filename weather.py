import requests
import csv

api_key = "c65f07a477ed814d4725adf9eabb948b"

base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(city_name, flags):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        if len(flags) > 0:
            for flag in flags:
                if flag == "temp":
                    print(" Temperature YOU WANT(in kelvin unit) = " +
                          str(current_temperature))
                if flag == "pressure":
                    print(
                        "Atmospheric pressure YOU WANT (in hPa unit) = " + str(current_pressure))
                if flag == "hum":
                    print("Humidity YOU WANT (in percentage) = " +
                          str(current_humidity))
                if flag == "desc":
                    print("Description YOU WANT = " + str(weather_description))
        else:
            print("Temperature (in kelvin unit) = " + str(current_temperature))
            print("Atmospheric pressure (in hPa unit) = " + str(current_pressure))
            print("Humidity (in percentage) = " + str(current_humidity))
            print("Description = " + str(weather_description))
    else:
        print(" City Not Found ")
