import numpy as np
import matplotlib.pyplot as plt

fs=100
t = np.arange(0, 1, 1/fs)
x = np.sin(2*np.pi*120*t)
omega = [1, 2, 5, 7]

# y = x * np.exp(-2j * np.pi * t)
# plt.plot(t, y)
# plt.xlabel("Timp")
# plt.ylabel("Amplitudine")
# plt.title("Figura 1")
# plt.axhline(0, color='black', linewidth=1)
# plt.show()

# frecventa de infasurare
for i in range(4):
    y = x * np.exp(-2j * np.pi * omega[i] * t)
    plt.subplot(2, 2, i +1)
    plt.plot(np.real(y), np.imag(y), linestyle='-', markersize=3, color='purple')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlabel("Real")
    plt.ylabel("Imaginar")


plt.show()
