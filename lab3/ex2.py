import numpy as np
import matplotlib.pyplot as plt

# frecventa de infasurare
fs=100
t = np.arange(0, 1, 1/fs)
x = np.sin(2*np.pi*5*t)
omega = [1, 2, 5, 7]

for i in range(4):
    y = x * np.exp(-2j * np.pi * omega[i] * t)
    plt.subplot(2, 2, i +1)
    plt.plot(np.real(y), np.imag(y), linestyle='-', markersize=3, color='purple')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlabel("Real")
    plt.ylabel("Imaginar")


plt.show()
