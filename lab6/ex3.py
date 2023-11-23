import numpy as np
import matplotlib.pyplot as plt

def rectangular_window(N):

    return np.ones(N)

def hanning_window(N):

    return 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(N) / (N - 1))

Nw = 200

rect_window = rectangular_window(Nw)
hanning_window = hanning_window(Nw)


f = 100
A = 1
phi = 0

t = np.arange(Nw) / f
semnal = A * np.sin(2 * np.pi * f * t + phi)

# Aplicăm ferestrele pe sinusoidă
semnal_rect = semnal * rect_window
semnal_hanning = semnal * hanning_window


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(t, semnal)
plt.title('Sinusoidă Originală')

plt.subplot(1, 3, 2)
plt.plot(t, semnal_rect)
plt.title('Sinusoidă cu Fereastra Dreptunghiulară')

plt.subplot(1, 3, 3)
plt.plot(t, semnal_hanning)
plt.title('Sinusoidă cu Fereastra Hanning')

plt.tight_layout()
plt.show()
