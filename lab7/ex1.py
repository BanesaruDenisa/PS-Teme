from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift


n1, n2 = np.meshgrid(np.linspace(1, 5, 200), np.linspace(1, 5, 200))

x1 = np.sin(2 * np.pi * n1 + 3 * np.pi * n2)
x2 = np.sin(4 * np.pi * n1) + np.cos(6 * np.pi * n2)

X1 = fftshift(fft2(x1))
X2 = fftshift(fft2(x2))

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].imshow(x1, cmap='gray')
axs[0, 0].set_title('Image from Function x1')
axs[0, 0].axis('off')

axs[1, 0].imshow(np.log(np.abs(X1)), cmap='gray')
axs[1, 0].set_title('Spectrum of x1')
axs[1, 0].axis('off')

axs[0, 1].imshow(x2, cmap='gray')
axs[0, 1].set_title('Image from Function x2')
axs[0, 1].axis('off')

axs[1, 1].imshow(np.log(np.abs(X2)), cmap='gray')
axs[1, 1].set_title('Spectrum of x2')
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
