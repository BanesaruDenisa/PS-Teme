import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.random.random(N)

for i in range(4):
    x = np.convolve(x,x)
    plt.subplot(4, 2, i+1)
    plt.plot(x)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Convolutie')

plt.show()



