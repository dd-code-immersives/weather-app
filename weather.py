import requests

import csv
import string

API_KEY = "c65f07a477ed814d4725adf9eabb948b"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name, flags):
    """
    Gets the weather for multiple cities
    """
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    JsonFile = response.json()
    c_name = city_name
    if JsonFile["cod"] != "404":
        JsonMain = JsonFile["main"]
        k_temp = JsonMain["temp"]
        c_temp = k_temp - 273.15
        f_temp = str(round(c_temp * (9/5) + 32, 2))
        c_pressure = str(JsonMain["pressure"])
        c_humidity = str(JsonMain["humidity"])
        jsonWeather = JsonFile["weather"]
        w_description = str(jsonWeather[0]["description"])
        if len(flags) > 0:
            for flag in flags:
                if flag == "temp":
                    print(f"The temperature at {c_name} is {f_temp}F˚")
                if flag == "pressure":
                    print(f"The pressure at {c_name} is {c_pressure}hPa")
                if flag == "hum":
                    print(f"The humidity at {c_name} is {c_humidity}%")
                if flag == "desc":
                    print(f"The description at {c_name} is {w_description}")
        else:
            print(f"""
            The weather info you requested for 
            {c_name}
            Temperature: {f_temp}F˚ 
            Barometric pressure is at {c_pressure}hPa
            Humidity is {c_humidity}%
            Weather description is as follows: {w_description}
            """)
    else:
        print(" City Not Found ")

API_KEY = "c65f07a477ed814d4725adf9eabb948b"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def build_weather_request(city_name):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

def get_weather(city_name, flags):

    response = build_weather_request(city_name)

    if response["cod"] != "404":

        y = response["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = response["weather"]
        weather_description = z[0]["description"]

        if "temp" in flags:
            print(" Temperature (in kelvin unit) = " +
                  str(current_temperature))
        if "hum" in flags:
            print("\n humidity (in percentage) = " +
                  str(current_humidiy))

        if "pressure" in flags:

            print("Atmospheric pressure (in hPa unit) = " +
                  str(current_pressure))

        if "desc" in flags:
            print("description = " +
                  str(weather_description))

    else:
        print(" City Not Found ")

if __name__ == '__main__':
    main()
