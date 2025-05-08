# Weather Analysis Pipeline 🛠️🌦️

Автоматизированный пайплайн для сбора, обработки и визуализации данных о погоде в Москве с использованием OpenWeatherMap API.

## Цель проекта 🎯
- Регулярный сбор актуальных метеорологических данных
- Автоматизация процессов ETL (Extract, Transform, Load)
- Визуализация динамики изменения температуры
- Создание шаблона для анализа временных рядов

## Структура проекта 📂
```bash
weather_analysis/
data_processed/ # Обработанные данные
│ └── weather_history.csv # Исторические данные в табличном формате
├── data_raw/ # Сырые данные от API
│ └── YYYY-MM-DD_HH-MM.json # Пример именования файлов с погодой
├── notebooks/
│ └── analysis_script.py # Генерация графиков из истории
├── scripts/
│ ├── fetch_weather.py # Получение данных с OpenWeatherMap API
│ └── process_data.py # Трансформация JSON -> CSV
├── .env # Конфигурация (API ключи)
├── requirements.txt # Зависимости
└── run_all.bat # Скрипт полного цикла обработки
```

## Начало работы 🚀

### Предварительные требования
- Python 3.10+
- Активный API ключ OpenWeatherMap ([инструкция по получению](https://openweathermap.org/appid))

### Установка
1. Клонировать репозиторий
```bash
git clone https://github.com/yourusername/weather-analysis.git
cd weather-analysis
```

2. Создать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```
3. Установить зависимости:
```bash
pip install -r requirements.txt
```
4. Добавить API ключ в файл .env:
```bash
OWM_API_KEY=ваш_уникальный_ключ_тут
```

## Использование 

### Ручной запуск

1. Получить свежие данные:
```bash
python scripts/fetch_weather.py
Создает JSON-файл в data_raw с текущей погодой
```
2. Обработать данные:
```bash
python scripts/process_data.py
Конвертирует все сырые JSON-файлы в единый CSV
```
3.Визуализировать данные:
```bash
python notebooks/analysis_script.py
Генерирует график температуры в папке data_processed
```

## Автоматический режим

```bash
./run_all.bat  # Windows
Выполняет полный цикл: сбор -> обработка -> визуализация
```

## Технические детали

### Зависимости

- Основные библиотеки:
	- requests == 2.31.0 - HTTP-запросы к API
	- pandas == 2.0.3 - обработка данных
	- matplotlib == 3.7.2 - визуализация
	- python-dotenv == 1.0.0 - управление переменными окружения

 
 ## Пример отображения графика  
 ![temperature_plot](https://github.com/user-attachments/assets/c055b9c2-9cba-4dd4-b524-40bb90950277)

