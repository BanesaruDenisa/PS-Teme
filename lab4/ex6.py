import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft

frecventa_esantionare, semnal = wavfile.read('inregistrare_vocale.wav')

proc_grup = 0.01
N = len(semnal)
lungime_grup =int( N * proc_grup)
suprapunere = int(lungime_grup / 2)


grupuri = [semnal[i:i+lungime_grup] for i in range(0, N - lungime_grup, lungime_grup - suprapunere)]

fft_grupuri = [fft(grup) for grup in grupuri]

matrice = np.abs(np.column_stack(fft_grupuri))

plt.imshow(matrice, aspect='auto', extent=[0, 100, 0, frecventa_esantionare/2])
plt.colorbar(label='Intensitate')
plt.xlabel('Timp')
plt.ylabel('Frecvență')
plt.title('Spectrogramă')
plt.show()
