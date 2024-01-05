import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage
from scipy.fft import dctn, idctn

X = misc.ascent()
plt.imshow(X, cmap=plt.cm.gray)
plt.show()

Q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]]

# Encoding
x = X[:8, :8]
y = dctn(x)
y_jpeg = Q_jpeg*np.round(y/Q_jpeg)

# Decoding
x_jpeg = idctn(y_jpeg)

# Results
y_nnz = np.count_nonzero(y)
y_jpeg_nnz = np.count_nonzero(y_jpeg)

plt.subplot(121).imshow(x, cmap=plt.cm.gray)
plt.title('Original')
plt.subplot(122).imshow(x_jpeg, cmap=plt.cm.gray)
plt.title('JPEG')
plt.show()

print('Componente în frecvență:' + str(y_nnz) +
      '\nComponente în frecvență după cuantizare: ' + str(y_jpeg_nnz))


####### ex 1

def jpeg_compression(image):
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
    height, width = image.shape

    # Pregătirea imaginii pentru compresie
    compressed_image = np.zeros_like(image)

    # Parcurge blocurile de 8x8 pixeli și aplică compresia JPEG
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            block = image[i:i+8, j:j+8]
            y = dctn(block)
            y_jpeg = Q_jpeg * np.round(y / Q_jpeg )
            compressed_image[i:i+8, j:j+8] = idctn(y_jpeg)
            

    return compressed_image

# Imaginea originală
X = misc.ascent()

# Aplicarea compresiei JPEG pe toată imaginea
compressed_image = jpeg_compression(X)

# Afișarea rezultatelor
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(X, cmap=plt.cm.gray)
plt.title('Imaginea Originală')

plt.subplot(1, 2, 2)
plt.imshow(compressed_image, cmap=plt.cm.gray)
plt.title('Imaginea Compresată JPEG')
plt.show()



