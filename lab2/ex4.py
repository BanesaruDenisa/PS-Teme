import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

f_sin = 4
amp_sin = 2
t_sin = np.linspace(0, 1, 1000)
f_sawtooth = 10
amp_saw = 1
t_saw = np.linspace(0, 1, 1000)
x_sin = amp_sin * np.sin(2 * np.pi * f_sin * t_sin)
x_sawtooth = signal.sawtooth(2 * np.pi * f_sawtooth * t_saw)
x_suma = x_sin + x_sawtooth

plt.figure(figsize=(16, 14))
plt.subplot(3, 1, 1)
plt.plot(t_sin, x_sin, color='black')
plt.title('Semnal Sinusoidal')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t_saw, x_sawtooth)
plt.title('Semnal Sawtooth')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_sin, x_suma, color='green')
plt.title('Suma Semnalelor')
plt.grid(True)

plt.show()