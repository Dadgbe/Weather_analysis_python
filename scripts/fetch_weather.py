# -*- coding: cp1251 -*-
import requests
import os
import sys
import json
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OWM_API_KEY")
if not API_KEY:
    print("Ошибка: переменная окружения OWM_API_KEY не задана.")
    sys.exit(1)

CITY_NAME = "Moscow"
lat = 55.75
lon = 37.62
URL = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?lat={lat}&lon={lon}"
    f"&appid={API_KEY}"
    f"&units=metric"
    f"&lang=ru"
)

def fetch_and_save():
    resp = requests.get(URL)
    resp.raise_for_status()
    data = resp.json()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"data_raw/weather_{timestamp}.json"
    with open(fname,"w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {fname}")


if __name__ == "__main__":
    os.makedirs("data_raw", exist_ok=True)
    fetch_and_save()