# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_processed/weather_history.csv", parse_dates=["fetched_at"])

plt.figure(figsize=(8,4))
plt.plot(df["fetched_at"], df["temp_C"])
plt.title("�������� ����������� (�C)")
plt.xlabel("����� UTC")
plt.ylabel("����������� �C")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_plot.png")  # <- ��������� ��� ����
plt.show()  # <- ��� ������ ��������
