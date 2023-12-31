
import numpy as np
import matplotlib.pyplot as plt

N = 8
f = np.zeros((N, N ), dtype=complex)
t = np.linspace(0, 1, 100)
x = np.sin(2*np.pi*100*t)

for k in range(N):
    for n in range(N):
        f[k, n] = np.exp(-2j * np.pi * k * n / N)


for i in range(N):

    plt.subplot(N, 2, 2*i+1)
    plt.stem(f[i].real)
    plt.title(f"Partea reala  {i} ")
    plt.subplot(N, 2, 2 * i + 2)
    plt.stem(f[i].imag)
    plt.title(f"Partea imaginara  {i} ")
   # plt.label()
    plt.grid(True)

plt.show()


# X=f*x
ftf = np.dot(f, f.conj().T)
In = np.eye(N)
mat = np.linalg.norm(np.abs(ftf) - N*In)

if mat <= 10**(-10):
    print("Matricea Fourier este unitara")
else:
    print("Matricea Fourier nu este unitara")