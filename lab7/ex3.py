import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage.restoration import denoise_nl_means, estimate_sigma


X = misc.face(gray=True)

np.random.seed(0)
noise = np.random.normal(0, 64, X.shape)
X_noisy = X + noise


X_noisy = np.clip(X_noisy, 0, 255)

# SNR inainte de stergerea zgomotului
signal_power = np.mean(X ** 2)
noise_power = np.mean(noise ** 2)
SNR_before = 10 * np.log10(signal_power / noise_power)

sigma_est = np.mean(estimate_sigma(X_noisy, multichannel=False))

denoised_img = denoise_nl_means(X_noisy, h=1.15 * sigma_est, fast_mode=True,
                                patch_size=5, patch_distance=6, multichannel=False)

# SNR dupa stergerea zgomotului
noise_after_denoising = denoised_img - X
noise_power_after_denoising = np.mean(noise_after_denoising ** 2)
SNR_after_denoising = 10 * np.log10(signal_power / noise_power_after_denoising)

plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.imshow(X, cmap=plt.cm.gray)
plt.title("Original Image")
plt.subplot(132)
plt.imshow(X_noisy, cmap=plt.cm.gray)
plt.title("Noisy Image")
plt.subplot(133)
plt.imshow(denoised_img, cmap=plt.cm.gray)
plt.title("Denoised Image")
plt.show()

print("SNR before denoising:", SNR_before)
print("SNR after denoising:", SNR_after_denoising)
