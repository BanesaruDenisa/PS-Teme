import numpy as np
from numpy.fft import fft, ifft


def direct_multiplication(p, q):
    # Inițializăm r(x) cu zerouri
    r = np.zeros(len(p) + len(q) - 1)
    # Calculăm fiecare termen al produsului
    for i in range(len(p)):
        for j in range(len(q)):
            r[i + j] += p[i] * q[j]
    return r


def fft_multiplication(p, q):
    # Extindem polinoamele
    p_extended = np.append(p, np.zeros(len(p) - 1))
    q_extended = np.append(q, np.zeros(len(q) - 1))

    # Aplicăm FFT
    p_fft = fft(p_extended)
    q_fft = fft(q_extended)

    # Înmulțirea în spațiul frecvențelor
    r_fft = p_fft * q_fft

    # Aplicăm FFT inversă și rotunjim pentru a obține coeficienții întregi
    r = np.round(ifft(r_fft)).real
    return r


# gradul maxim N
N = 5

# Generăm coeficienții aleator pentru p(x) și q(x) cu valori între -10 și 10
p = np.random.randint(-10, 11, N)
q = np.random.randint(-10, 11, N)

r_direct = direct_multiplication(p, q)
r_fft = fft_multiplication(p, q)

print("p(x):", p)
print("q(x):", q)
print("Produs prin inmultire directa:", r_direct)
print("Produs prin FFT:", r_fft)
