import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import pandas as pd

lista_dias = []

today = dt.datetime.now()
today = today.date()

try:
    for i in range(1, 33):
        ultimo_dia = dt.date(2025, 10, i)
        lista_dias.append(str(ultimo_dia))
except:
    print(f"Ultimo dia do mes: {i-1}")

print(ultimo_dia)
print(lista_dias)

