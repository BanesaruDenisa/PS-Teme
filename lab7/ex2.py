from scipy import fftpack, misc
import numpy as np
import matplotlib.pyplot as plt


X = misc.face(gray=True)


F = fftpack.fft2(X)
F_shifted = fftpack.fftshift(F)

def calculate_snr(signal, noise):
    signal_power = np.sum(signal ** 2)
    noise_power = np.sum(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)


desired_snr = 20

rows, cols = X.shape
crow, ccol = rows // 2, cols // 2
mask = np.ones((rows, cols), dtype=np.uint8)

for r in range(rows):
    for c in range(cols):
        distance = np.sqrt((r - crow)**2 + (c - ccol)**2)
        if distance > 20:
            mask[r, c] = 0


F_shifted_filtered = F_shifted * mask

F_filtered = fftpack.ifftshift(F_shifted_filtered)
X_filtered = fftpack.ifft2(F_filtered).real


noise = X - X_filtered
snr = calculate_snr(X_filtered, noise)


fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(X, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(X_filtered, cmap='gray')
axs[1].set_title(f'Filtered Image (SNR: {snr:.2f} dB)')
axs[1].axis('off')

plt.show()
