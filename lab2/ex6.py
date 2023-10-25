import numpy as np
import matplotlib.pyplot as plt

fs = 100
ts = np.arange(0, 1, 1/fs)
fa = fs/2
fb = fs/4
fc = 0
xa = np.cos(2*np.pi*fa*ts )
xb = np.cos(2*np.pi*fb*ts )
xc = np.cos(2*np.pi*fc*ts)

plt.figure(figsize=(16, 14))
plt.subplot(3, 1, 1)
plt.plot(ts, xa, color='black')
plt.title('Semnal f=fs/2 Hz')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(ts, xb)
plt.title('Semnal f=fs/4 Hz')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(ts, xc, color='green')
plt.title('Suma f=0 Hz')
plt.grid(True)

plt.show()