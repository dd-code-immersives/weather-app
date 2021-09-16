import requests

# Enter your API key here
API_KEY = "c65f07a477ed814d4725adf9eabb948b"

# base_url variable to store url
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# builing the api request for openweathermap


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
