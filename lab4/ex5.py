import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt


durata_inregistrarii = 5
frecventa_esantionare = 44100


print("Începeți înregistrarea...")
audio_inregistrat = sd.rec(int(durata_inregistrarii * frecventa_esantionare), samplerate=frecventa_esantionare, channels=2)
sd.wait()
print("Înregistrare finalizată!")

audio_in_array = np.array(audio_inregistrat)

nume_fisier = "inregistrare_vocale.wav"
wavfile.write(nume_fisier, frecventa_esantionare, audio_inregistrat)

f, t, Sxx = spectrogram(audio_in_array[:,0], frecventa_esantionare)

plt.pcolormesh(t, f, 10 * np.log10(Sxx))
plt.ylabel('Frecvență')
plt.xlabel('Timp')
plt.title('Spectrogramă')
plt.colorbar(label='Intensitate [dB]')
plt.show()
