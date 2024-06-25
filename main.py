#inserts into db
import schedule
import time 
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()


def job(): 
    import requests
    from insert_into_db import insertIntoDb

    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=27.7055&lon=85.3440&units=metric&appid=app_id')

    response_data = response.json()

    #data below is just to see the json tags of the api
    #response_data = {'coord': {'lon': 85.344, 'lat': 27.7055}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'base': 'stations', 'main': {'temp': 27.15, 'feels_like': 28.68, 'temp_min': 27.15, 'temp_max': 27.15, 'pressure': 1010, 'humidity': 65}, 'visibility': 8000, 'wind': {'speed': 3.6, 'deg': 280}, 'clouds': {'all': 40}, 'dt': 1717942387, 'sys': {'type': 1, 'id': 9201, 'country': 'NP', 'sunrise': 1717888946, 'sunset': 1717938815}, 'timezone': 20700, 'id': 7800827, 'name': 'Kathmandu', 'cod': 200}

    #timestamp in unix 
    timestamp = response_data['dt'] #response object is non subscriptable. Dump json data onto another variable and use the respective variable to extract json data to put in other variables.

    from datetime import datetime

    time = datetime.fromtimestamp(timestamp, tz=None)
    print(time)
    weather = response_data['weather'][0]['main']
    max_temp = response_data['main']['temp_max']
    min_temp = response_data['main']['temp_min']
    humidity = response_data['main']['humidity']

    insertIntoDb(time ,max_temp, min_temp, humidity)

    #print(response['weather'][0]['id'], )
    #accessing weather's id-- call weather key of the response json, then go to the 0th index of the weather list and access the 'id' key value from the dictionary in the 0th index.

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
