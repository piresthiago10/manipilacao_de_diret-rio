import os
import time
from pathlib import Path
from datetime import datetime, timedelta

arquivo = "/home/piresthiago10/Desenvolvimento/manipilacao_de_diretorio/windows/app.py"
timestamp = os.path.getmtime(arquivo)
print(datetime.fromtimestamp(timestamp))
diferenca_tempo = datetime.now() - datetime.fromtimestamp(timestamp)
print("Diferenca {}".format(str(diferenca_tempo.total_seconds())))
ten_minute = 600.0000
datetime_time_obj2 = timedelta(seconds=ten_minute)
print("Segundos {}".format(datetime_time_obj2))
datetime_time_obj = ten_minute
datetime_diferenca_obj = diferenca_tempo.total_seconds()
# datetime_diferenca_obj = datetime.strptime(str(diferenca_tempo.total_seconds()), "%H:%M:%S.%f")
print(datetime_time_obj)
print(datetime_diferenca_obj)
if datetime_diferenca_obj > datetime_time_obj:
    print('ok')
else:
    print('schrebells')