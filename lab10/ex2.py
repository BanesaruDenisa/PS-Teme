import numpy as np
import matplotlib.pyplot as plt

# Dimensiunea spațiului
d = 100

# Intervalul de lucru pentru x și y
x_range = np.linspace(-1, 1, d)
y_range = np.linspace(-1, 1, d)

# Calcularea matricei de covarianță C
C = np.zeros((d, d))
for i, x in enumerate(x_range):
    for j, y in enumerate(y_range):
        C[i, j] = np.dot(x, y)

# Eșantionarea din distribuția Gaussiană cu matricea de covarianță C și medie 0
np.random.seed(0)  # Fixăm seed-ul pentru reproducibilitate
z = np.random.multivariate_normal(np.zeros(d), C)

# Afișarea valorilor lui z în funcție de x
plt.plot(x_range, z)
plt.xlabel('x')
plt.ylabel('Valoarea lui z')
plt.title('Proces Gaussian cu funcția de covarianță liniară și medie 0')
plt.show()
