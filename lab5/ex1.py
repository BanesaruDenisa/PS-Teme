import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


file = 'Train.csv'
x = pd.read_csv(file, delimiter=',')
x['Datetime'] = pd.to_datetime(x['Datetime'])
time_diff = x['Datetime'].diff().dropna()

t = 3600
f_esant = 1 / t
f_nyquist = f_esant / 2

total_time = x['Datetime'].iloc[-1] - x['Datetime'].iloc[0]

nr_masini = x['Count']
esantioane = x['ID']

print(f"Timpul total este: {total_time}")
print(f"Frecventa de esantionare este: {f_esant}")
print(f"Frecventa de maxima este: {f_nyquist}")

plt.figure(figsize=(15, 6))
plt.plot(esantioane, nr_masini, label='Traffic Count')
plt.xlabel('Esantioane')
plt.ylabel('Nr masini')
plt.title('Traffic Data')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()


