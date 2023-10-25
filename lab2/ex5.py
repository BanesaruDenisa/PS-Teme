import numpy as np
import sounddevice as sd

f1 = 320
amp1 = 1
t1 = np.linspace(0, 1, 1000)
x1 = amp1*np.sin(2 * np.pi * f1 * t1)

f2 = 240
amp2 = 1
t2 = np.linspace(0, 1, 1000)
x2 = amp2*np.sin(2 * np.pi * f2 * t2)

x1_x2 = np.concatenate((x1, x2))

sd.play(x1_x2, 1000)
sd.wait()
