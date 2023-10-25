import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile

t_a = np.linspace(0, 1, 1600)
t_b = np.linspace(0, 3, 500)
t_c = np.linspace(0, 1, 500)
t_d = np.linspace (0, 1, 100)

x_a = np.sin(2*np.pi*400*t_a )
x_b = np.sin(2*np.pi*800*t_b)
x_c = 2*(t_c*240 - np.floor(t_c * 240 + 0.5))
x_d = np.sign(np.sin(2*np.pi*300*t_d))

x_a = x_a.astype('float32')
sd.play(x_a, 1600)
x_b = x_b.astype('float32')
#sd.play(x_b, 800)
sd.wait()

f_semnal_a = 'semnal_a.wav'
wavfile.write(f_semnal_a, 1600, x_a)
semnal_citit = wavfile.read(f_semnal_a)

