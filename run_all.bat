@echo off
call venv\Scripts\activate
python scripts\fetch_weather.py
python scripts\process_data.py
python notebooks\analysis_script.py
pause
