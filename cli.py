import weather
import argparse
import json
import csv


my_parser = argparse.ArgumentParser()
my_parser.add_argument('--temp', action='store_true')
my_parser.add_argument('--pressure', action='store_true')
my_parser.add_argument('--hum', action='store_true')
my_parser.add_argument('--desc', action='store_true')
my_parser.add_argument('--city_file', type=argparse.FileType('r'))
args = my_parser.parse_args()
lst = []
if not args.city_file:
    city = input("Enter city name : ")
    if args.temp:
        lst.append(f"The temp is: {weather.weather_cli(city)['main']['temp']}")
    if args.pressure:
        lst.append(
            f"The pressure is: {weather.weather_cli(city)['main']['pressure']}")
    if args.hum:
        lst.append(
            f"The humidity is: {weather.weather_cli(city)['main']['humidity']}")
    if args.desc:
        lst.append(
            f"The description is: {weather.weather_cli(city)['weather']['description']}")
    for x in lst:
        print(x)
else:
    data = {}
    data['temperature'] = 0
    data['pressure'] = 0
    data['hum'] = 0
    data['desc'] = 0
    data['city_count'] = 0
    for city_list in csv.reader(args.city_file):
        for city in city_list:
            city = city.strip()
            if args.temp:
                data['temperature'] += int(weather.weather_cli(city)
                                           ['main']['temp'])
            if args.pressure:
                data['pressure'] += int(weather.weather_cli(city)
                                        ['main']['pressure'])
            if args.hum:
                data['hum'] += int(weather.weather_cli(city)
                                   ['main']['humidity'])
            if args.desc:
                data['desc'] += int(weather.weather_cli(city)
                                    ['weather']['description'])
            data['city_count'] += 1
    with open('data/data.txt', 'w') as outfile:
        json.dump(data, outfile)
        for k, v in data.items():
            if v != 0 and k != 'city_count':
                print(f"the average {k} is {v/data['city_count']}")
