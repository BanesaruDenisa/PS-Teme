import numpy as np
import matplotlib.pyplot as plt



# Parametrii distribuției unidimensionale
medie = 5
varianta = 2

data_unidimensionala = np.random.normal(medie, np.sqrt(varianta), 1000)

plt.hist(data_unidimensionala, bins=30, density=True, alpha=0.6, color='g')
plt.title('Distribuție Gaussiană Unidimensională')
plt.xlabel('Valoare')
plt.ylabel('Densitate de probabilitate')
plt.grid()
plt.show()



# Parametrii distribuției bidimensionale
medie = np.array([2, 3])
covarianta = np.array([[1, 0.5], [0.5, 2]])

data_bidimensionala = np.random.multivariate_normal(medie, covarianta, 1000)

plt.scatter(data_bidimensionala[:, 0], data_bidimensionala[:, 1], alpha=0.6, color='b')
plt.title('Distribuție Gaussiană Bidimensională')
plt.xlabel('Valoare pe axa X')
plt.ylabel('Valoare pe axa Y')
plt.axis('equal')
plt.grid()
plt.show()
