import numpy as np
import matplotlib.pyplot as plt
import scipy
import skimage
from scipy import misc
from scipy.fft import dctn, idctn
from skimage import color


def rgb_to_ycbcr(rgb_image):
    ycbcr_image = color.rgb2ycbcr(rgb_image)
    return ycbcr_image

def ycbcr_to_rgb(ycbcr_image):
    rgb_image = color.ycbcr2rgb(ycbcr_image)
    return rgb_image

def jpeg_compression_color(rgb_image):
    # Transformarea din RGB în Y'CbCr
    ycbcr_image = rgb_to_ycbcr(rgb_image)

    # Parametri pentru calitatea JPEG
    Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                       [12, 12, 14, 19, 26, 28, 60, 55],
                       [14, 13, 16, 24, 40, 57, 69, 56],
                       [14, 17, 22, 29, 51, 87, 80, 62],
                       [18, 22, 37, 56, 68, 109, 103, 77],
                       [24, 35, 55, 64, 81, 104, 113, 92],
                       [49, 64, 78, 87, 103, 121, 120, 101],
                       [72, 92, 95, 98, 112, 100, 103, 99]])

    # Dimensiunile imaginii
    height, width, _ = rgb_image.shape

    # Pregătirea imaginii pentru compresie
    compressed_image = np.zeros_like(rgb_image)

    # Parcurge blocurile de 8x8 pixeli și aplică compresia JPEG
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            block = ycbcr_image[i:i+8, j:j+8, :]
            for k in range(3):
                y = dctn(block[:, :, k], norm='ortho')
                y_jpeg = Q_jpeg * np.round(y / Q_jpeg)
                compressed_image[i:i+8, j:j+8, k] = idctn(y_jpeg, norm='ortho')

    # Transformarea înapoi din Y'CbCr în RGB
    compressed_rgb_image = ycbcr_to_rgb(compressed_image)

    # Cliparea imaginii pentru a asigura că valorile sunt în intervalul [0, 255]
    compressed_rgb_image = np.clip(compressed_rgb_image, 0, 255).astype(np.uint8)

    return compressed_rgb_image

# Imaginea color originală
rgb_face = misc.face()

# Aplicarea compresiei JPEG pe imaginea color
compressed_rgb_face = jpeg_compression_color(rgb_face)

# Afișarea rezultatelor
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(rgb_face)
plt.title('Imaginea Color Originală')

plt.subplot(1, 2, 2)
plt.imshow(compressed_rgb_face)
plt.title('Imaginea Color Compresată JPEG')
plt.show()
