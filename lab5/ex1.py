import numpy as np
import matplotlib.pyplot as plt
import csv

x = np.genfromtxt('Train.csv', delimiter=',')

fs = 1000
t = len(x) / fs
N = len(x) - 1

# semnal = np.array(x)
# x_esant = semnal[::int(1 / (fs * (1.0 / t)))]
#
# X = np.fft.fft(x)
# X = abs(X/N)
# X = X[:N/2]
# f = fs*np.linspace(0, N//2, N//2)/N
#
# plt.stem(t, x_esant)
# plt.axhline(0, color='black', linewidth=1)
# plt.axvline(0, color='black', linewidth=1)
# plt.xlabel("Esantionare")
# plt.ylabel("Nr masini")





x['time_diff'] = x['time_diff'].diff
x['time_diff_seconds'] = x['time_diff'].dt.total_seconds()
x = x.dropna()
interval = x['time_diff_seconds'].mean()
frecventa = 1 / interval

print(f"Frecventa de esantionare este: {frecventa}")
