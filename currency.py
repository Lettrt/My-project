import requests
from config import API_CUR

API_KEY = API_CUR

def get_usd_rub_exchange_rate():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/RUB"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["conversion_rate"]
    else:
        return f"Ошибка выполнения запроса: {response.status_code}"

def get_usd_kgs_exchange_rate():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/KGS"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["conversion_rate"]
    else:
        return f"Ошибка выполнения запроса: {response.status_code}"

def get_rub_kgs_exchange_rate():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/RUB/KGS"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["conversion_rate"]
    else:
        return f"Ошибка выполнения запроса: {response.status_code}"
