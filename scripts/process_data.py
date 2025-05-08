# -*- coding: utf-8 -*-
import os
import glob
import json
from time import timezone
import pandas as pd
from datetime import datetime

from pandas.core.reshape import encoding


def load_latest_raw():
    """Найти и загрузить самый свежий JSON-файл из data_raw/"""
    files = sorted(glob.glob("data_raw/*.json"))
    if not files:
        raise FileNotFoundError("Нет файлов в папке data_raw/. Сначала запустите файл fetch.bat")
    with open(files[-1], encoding="utf-8") as f:
        return json.load(f)
    

def json_to_df(data):
    """Вытащить из ответа OpenWeatherMap ключевая поля в одном ряду DataFrame"""
    rec = {
        "fetched_at": datetime.utcnow(),
        "city": data.get("name"),
        "country": data["sys"].get("country"),
        "temp_C": data["main"].get("temp"),
        "feels_like_C": data["main"].get("feels_like"),
        "temp_min_C": data["main"].get("temp_min"),
        "temp_max_C": data["main"].get("temp_max"),
        "weather_desc": data["weather"][0].get("description")
        }
    return pd.DataFrame([rec])


def save_processed(df):
    """ Сохранить DataFrame в data_processed/weather_current.csv"""
    os.makedirs("data_processed", exist_ok=True)
    hist_path = "data_processed/weather_history.csv"
    header = not os.path.exists(hist_path)
    df.to_csv(hist_path, mode="a", header=header, index=False, float_format="%.2f", encoding="utf-8-sig")

if __name__ == "__main__":
    raw = load_latest_raw()
    df = json_to_df(raw)
    save_processed(df)