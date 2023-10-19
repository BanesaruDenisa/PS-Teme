import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal

amp = 1
f = 10
t = np.arange(0, 1, 0.00005)
faze = [np.pi/2, np.pi/3, np.pi/4, np.pi/6]

x = [amp*np.sin(2*np.pi*f*t + f) for f in faze]

zn = np.random.normal(1, len(x))
snr = [0.1, 1, 10, 100]

def calc_zgomot(x , zn, snr):
    for s in x:
        for i in snr:
            gama = np.linalg.norm(x)**2 / (i * np.linalg.norm(zn)**2)
            x_nou = s + gama * zn

    return x_nou

plt.figure(figsize=(16, 14))
for x, f in zip(x, faze):
    plt.plot(t, calc_zgomot(x, zn, snr), label=f'Faza= {f} rad')
plt.title('xn(tn)')
plt.xlabel('t')
plt.ylabel('x(t)')


plt.show()