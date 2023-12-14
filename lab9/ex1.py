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

model = sm.tsa.ExponentialSmoothing(time_series)

fit_model = model.fit()

# Obținem seria rezultată din medierea exponențială
smoothed_series = fit_model.fittedvalues

plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(time_series, label='Seria de timp')
plt.plot(smoothed_series, label='Seria mediată exponențial', linestyle='dashed')
plt.legend()
plt.title('Seria de timp și seria mediată exponențial')

plt.subplot(3, 1, 2)
plt.plot(trend, label='Trend', color='orange')
plt.legend()
plt.title('Trend')

plt.subplot(3, 1, 3)
plt.plot(season, label='Sezon', color='green')
plt.legend()
plt.title('Sezon')

plt.tight_layout()
plt.show()
