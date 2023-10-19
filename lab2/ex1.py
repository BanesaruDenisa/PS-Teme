import numpy as np
import matplotlib.pyplot as plt


amp = 2
f = 20
faza = np.pi/3
t = np.arange(0, 1, 0.00005)

x = amp*np.sin(2*f*np.pi*t + faza)
y = amp*np.sin(2*f*np.pi*t + faza + np.pi/2)

plt.figure(figsize=(16, 14))
plt.subplot(3, 1, 1)
plt.plot(t, x, color='blue')
plt.title('xn(tn)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.subplot(3, 1, 2)
plt.plot(t, y, color='black')
plt.title('yn(tn)')
plt.xlabel('t')
plt.ylabel('y(t)')

plt.show()