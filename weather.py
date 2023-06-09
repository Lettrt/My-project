import requests
from datetime import datetime, timedelta
from config import API_KEY

url = 'https://api.openweathermap.org/data/2.5/weather'
url_forecast = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather_forecast_for_today():
    params = {
        'q': 'Bishkek',
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru',
    }

    response = requests.get(url_forecast, params=params)

    if response.status_code == 200:
        data = response.json()
        today_date = datetime.now().strftime('%Y-%m-%d')
        weather_info = ''
        for forecast in data['list']:
            if forecast['dt_txt'].startswith(today_date):
                weather_info += f"Дата и время: {forecast['dt_txt']}\n"
                weather_info += f"Температура: {forecast['main']['temp']} °C\n"
                weather_info += f"Описание: {forecast['weather'][0]['description']}\n\n"

        return weather_info
    else:
        return f"Ошибка выполнения запроса: {response.status_code}"


def get_weather_forecast_for_tomorrow():
    params = {
        'q': 'Bishkek',
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru',
    }

    response = requests.get(url_forecast, params=params)

    if response.status_code == 200:
        data = response.json()
        tomorrow_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        weather_info = ''
        for forecast in data['list']:
            if forecast['dt_txt'].startswith(tomorrow_date):
                weather_info += f"Дата и время: {forecast['dt_txt']}\n"
                weather_info += f"Температура: {forecast['main']['temp']} °C\n"
                weather_info += f"Описание: {forecast['weather'][0]['description']}\n\n"

        return weather_info
    else:
        return f"Ошибка выполнения запроса: {response.status_code}"