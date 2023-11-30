import numpy as np
import matplotlib.pyplot as plt

N = 64

Y1 = np.zeros((N, N))
Y2 = np.zeros((N, N))
Y3 = np.zeros((N, N))

Y1[0, 5] = Y1[0, N-5] = 1
Y2[5, 0] = Y2[N-5, 0] = 1
Y3[5, 5] = Y3[N-5, N-5] = 1

y1 = np.fft.ifft2(Y1).real
y2 = np.fft.ifft2(Y2).real
y3 = np.fft.ifft2(Y3).real

fig, axs = plt.subplots(2, 3, figsize=(15, 10))

axs[0, 0].imshow(np.fft.fftshift(Y1), cmap='gray')
axs[0, 0].set_title("Spectrum of Y1")
axs[0, 1].imshow(np.fft.fftshift(Y2), cmap='gray')
axs[0, 1].set_title("Spectrum of Y2")
axs[0, 2].imshow(np.fft.fftshift(Y3), cmap='gray')
axs[0, 2].set_title("Spectrum of Y3")

axs[1, 0].imshow(y1, cmap='gray')
axs[1, 0].set_title("Spatial Domain of Y1")
axs[1, 1].imshow(y2, cmap='gray')
axs[1, 1].set_title("Spatial Domain of Y2")
axs[1, 2].imshow(y3, cmap='gray')
axs[1, 2].set_title("Spatial Domain of Y3")

plt.tight_layout()
plt.show()
