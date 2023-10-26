import numpy as np
import matplotlib.pyplot as plt

fs = 1000
timp = np.arange(0, 1, 1/fs)
semnal_original = np.sin(2 * np.pi * 100 * timp)

semnal_decimat = semnal_original[::4]


plt.figure(figsize=(10, 6))


plt.subplot(2, 1, 1)
plt.plot(timp, semnal_original)
plt.title('Semnal Original')
plt.grid(True)

timp_decimat = np.arange(0, 1, 1/(4*fs))
plt.subplot(2, 1, 2)
plt.plot(timp_decimat, semnal_decimat)
plt.title('Semnal Decimat')
plt.grid(True)

plt.tight_layout()
plt.show()
