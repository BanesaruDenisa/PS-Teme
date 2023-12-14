import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


np.random.seed(42)

N = 1000
t = np.arange(N)
trend = 0.02 * t**2
season = 5 * np.sin(2 * np.pi * t / 100) + 3 * np.sin(2 * np.pi * t / 30)
noise = np.random.normal(0, 1, N)
time_series = trend + season + noise

# (b) Generarea modelului MA
q = 5  # Orizontul modelului MA

# Folosim modulul ARIMA pentru a crea și ajusta modelul MA
ma_order = (0, 0, q)  # (p, d, q) = (0, 0, q) pentru un model MA
ma_model = sm.tsa.ARIMA(time_series, order=ma_order)
ma_fit = ma_model.fit()

# Obținem valorile ajustate ale modelului MA
ma_fitted_values = ma_fit.fittedvalues

# Afișăm rezultatele
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Seria de timp')
plt.plot(ma_fitted_values, label=f'Model MA (q={q})', linestyle='dashed')
plt.legend()
plt.title('Seria de timp și modelul MA')
plt.show()
