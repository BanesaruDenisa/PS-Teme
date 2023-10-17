import numpy as np
import matplotlib.pyplot as plt

##### ex1
# #a,b)
# t = np.arange(0, 0.03, 0.0005)
#
# x = np.cos(520*np.pi*t + np.pi/3)
# y = np.cos(280*np.pi*t - np.pi/3)
# z = np.cos(120*np.pi*t + np.pi/3)
#
# plt.figure(figsize=(16, 14))
# plt.subplot(3, 1, 1)
# plt.plot(t, x, color='blue')
# plt.title('xn(tn)')
# plt.xlabel('t')
# plt.ylabel('x(t)')
# plt.subplot(3, 1, 2)
# plt.plot(t, y, color='green')
# plt.title('yn(tn)')
# plt.xlabel('t')
# plt.ylabel('y(t)')
# plt.subplot(3, 1, 3)
# plt.plot(t, z, color='black')
# plt.title('zn(tn)')
# plt.xlabel('t')
# plt.ylabel('z(t)')
#
# #c)
# nt= np.arange(0, 0.03, 1/200)
#
# xn = np.cos(520*np.pi*nt + np.pi/3)
# yn = np.cos(280*np.pi*nt - np.pi/3)
# zn = np.cos(120*np.pi*nt + np.pi/3)
#
# plt.figure(figsize=(16, 14))
# plt.subplot(3, 1, 1)
# plt.stem(nt, xn, markerfmt='or')
# plt.plot(t, x, color='blue')
# plt.subplot(3, 1, 2)
# plt.stem(nt, yn, markerfmt='or')
# plt.plot(t, y, color='green')
# plt.subplot(3, 1, 3)
# plt.stem(nt, zn, markerfmt='or')
# plt.plot(t, z, color='black')
#
# plt.show()

##### ex2

t_a = np.linspace(0, 1, 1600)
t_b = np.linspace(0, 3, 500)
t_c = np.linspace(0, 1, 500)
t_d = np.linspace (0, 1, 100)

x_a = np.sin(2*np.pi*400*t_a )
x_b = np.sin(2*np.pi*800*t_b)
x_c = 2*(t_c*240 - np.floor(t_c * 240 + 0.5))
x_d = np.sign(np.sin(2*np.pi*300*t_d))

plt.figure(figsize=(16, 14))
plt.subplot(4, 1, 1)
plt.plot(t_a, x_a)
plt.title('(a)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(4, 1, 2)
plt.plot(t_b, x_b)
plt.title('(b)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(4, 1, 3)
plt.plot(t_c, x_c)
plt.title('(c)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(4, 1, 4)
plt.plot(t_d, x_d)
plt.title('(d)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.show()