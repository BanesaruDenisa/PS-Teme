import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

file = 'Train.csv'
data = pd.read_csv(file, delimiter=',')

t = 3600
f_esant = 1 / t

x = data['Count'].values
#### transformata
N = len(x)
transformata = np.fft.fft(x)
#X = abs(transformata/N)
#X = X[:N//2]
#frecvente = f_esant*np.linspace(0, N/2, N/2)/N   aveam eroare
#frecvente = np.fft.fftfreq(N, f_esant)


transformata[0] = 0
X = abs(transformata/N)
frecvente = np.fft.fftfreq(N, f_esant)

plt.figure(figsize=(12, 6))
plt.plot(frecvente, X)
plt.title("Transformata Fourier ")
plt.xlabel("Frecventa (Hz)")
plt.ylabel("Modul X")
plt.grid()
plt.show()

# f)  frecventa maxima
f_max_index = np.argmax(X)
f_max = np.abs(frecvente[f_max_index])
print(f"Frecventa maxima este {f_max}")

sort_index = np.argsort(X)[::-1]
top_4frecvente = np.abs(frecvente[sort_index[:4]])

print("Cele 4 frecvente principale sunt:")
for i, f in enumerate(top_4frecvente):

    ore_per_ciclu = 1 / f / 3600
    zile_per_ciclu = ore_per_ciclu / 24
    saptamani_ciclu = zile_per_ciclu / 7

    print(f"Frecvența {i + 1}: {f} Hz, echivalent cu {ore_per_ciclu} ore per ciclu")
    print(f"Frecvența {i + 1}: {f} Hz, echivalent cu {zile_per_ciclu} zile per ciclu")
    print(f"Frecvența {i + 1}: {f} Hz, echivalent cu {saptamani_ciclu} saptamani per ciclu")

    # o zi o saptamana si un an



