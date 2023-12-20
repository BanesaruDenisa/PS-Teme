import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# (a) Generarea seriei de timp
np.random.seed(42)

N = 1000
t = np.arange(N)
trend = 0.02 * t**2
season = 5 * np.sin(2 * np.pi * t / 100) + 3 * np.sin(2 * np.pi * t / 30)
noise = np.random.normal(0, 1, N)
time_series = trend + season + noise

# (b) Generarea modelului ARMA
p = 3  # Orizontul AR (auto-regresie)
q = 5  # Orizontul MA (medie mobilă)

arma_order = (p, 0, q)
arma_model = sm.tsa.ARIMA(time_series, order=arma_order)
arma_fit = arma_model.fit()

#valorile ajustate ale modelului ARMA
arma_fitted_values = arma_fit.fittedvalues

plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Seria de timp')
plt.plot(arma_fitted_values, label=f'Model ARMA (p={p}, q={q})', linestyle='dashed')
plt.legend()
plt.title('Seria de timp și modelul ARMA')
plt.show()


print(arma_fit.summary())
