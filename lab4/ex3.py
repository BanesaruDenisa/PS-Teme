import numpy as np
import matplotlib.pyplot as plt

f = 100
t = np.linspace(0, 0.03, 100)
x = np.sin(2*np.pi*f*t)

f_esant = 250
t_esant = np.arange(0, 0.03, 1/f_esant)
x_esant = np.sin(2*np.pi*f*t_esant)

f_ref1 = 90
f_ref2 = 50
x_ref1 = np.sin(2*np.pi*f_ref1*t)
x_ref2 = np.sin(2*np.pi*f_ref2*t)
x_ref1_es = np.sin(2*np.pi*f_ref1*t_esant)
x_ref2_es = np.sin(2*np.pi*f_ref2*t_esant)

plt.subplot(4, 1, 1)
plt.plot(t, x)
plt.title("Semnal continuu f=100")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.axhline(0, color='black', linewidth=1)

plt.subplot(4, 1, 2)
plt.stem(t_esant, x_esant, markerfmt='or')
plt.plot(t, x)
plt.title("Semnal esantionat")
plt.axhline(0, color='black', linewidth=1)

plt.subplot(4, 1, 3)
plt.stem(t_esant, x_ref1_es, markerfmt='or')
plt.plot(t, x_ref1, color='yellow')
plt.subplot(4, 1, 4)
plt.stem(t_esant, x_ref2_es, markerfmt='or')
plt.plot(t, x_ref2, color='green')

plt.show()