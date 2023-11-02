
import numpy as np
import matplotlib.pyplot as plt
import time
##3pickle


N = [128, 256, 512, 1024, 2048, 4096, 8192]
def my_fft(x):
    N = len(x)
    f = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            f[k] = np.exp(-2j * np.pi * k * n / N)
            X = np.dot(f, x)
    return X


my_total_t = []
fft_total_t = []

for n in N:
    x = np.random.random(n)
    start_my_t = time.perf_counter()
    my_result = my_fft(x)
    my_total_t.append(time.perf_counter() - start_my_t)
    print(my_total_t)

    start_fft_t = time.perf_counter()
    fft_result = np.fft.fft(x)
    fft_total_t.append(time.perf_counter() - start_fft_t)
    print(fft_total_t)


plt.figure(figsize=(10, 6))
plt.plot(N, my_total_t, label='FT Proprie', marker='o')
plt.plot(N, fft_total_t, label='numpy.fft', marker='o')
plt.yscale('log')
#plt.xscale('log')
plt.xlabel('Valorile vectorului (N)')
plt.ylabel('Timp de executie (secunde)')
plt.title('Comparatie intre FFT Proprie si numpy.fft')
plt.legend()
plt.grid()
plt.show()
