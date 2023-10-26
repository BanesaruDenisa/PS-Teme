import numpy as np
import matplotlib.pyplot as plt

# Generați un semnal sinusoidal cu frecvența de esantionare de 1000 Hz
fs = 1000
timp = np.arange(0, 1, 1/fs)  # Vector de timp de la 0 la 1 secundă
semnal_original = np.sin(2 * np.pi * 100 * timp)  # Semnal cu frecvența de 100 Hz

# Decimați semnalul la 1/4 din frecvența inițială (păstrați doar fiecare al 4-lea element)
semnal_decimat = semnal_original[::4]

# Afișați cele două semnale în subgrafice
plt.figure(figsize=(10, 6))

# Subplot pentru semnalul original
plt.subplot(2, 1, 1)
plt.plot(timp, semnal_original)
plt.title('Semnal Original')
plt.grid(True)

# Subplot pentru semnalul decimat
timp_decimat = np.arange(0, 1, 1/(4*fs))  # Vector de timp decimat
plt.subplot(2, 1, 2)
plt.plot(timp_decimat, semnal_decimat)
plt.title('Semnal Decimat')
plt.grid(True)

plt.tight_layout()
plt.show()
