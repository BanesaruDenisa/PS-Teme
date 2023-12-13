import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# (a) Generarea seriei de timp
np.random.seed(42)

N = 1000
t = np.arange(N)

#trend (ecuație de grad 2)
trend = 0.02 * t**2

# Două componente de sezon cu frecvențe diferite
season = 5 * np.sin(2 * np.pi * t / 100) + 3 * np.sin(2 * np.pi * t / 30)

# Variatii mici folosind zgomot alb gaussian
noise = np.random.normal(0, 1, N)

# Seria de timp
time_series = trend + season + noise


plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(time_series, label='Seria de timp')
plt.legend()
plt.title('Seria de timp')

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

# (b) Calcularea vectorului de autocorelație
autocorrelation = sm.tsa.acf(time_series, nlags=40, fft=False)


plt.figure(figsize=(10, 6))
plt.stem(autocorrelation)
plt.title('Vectorul de autocorelație')
plt.show()

# (c) Calcularea modelului AR de dimensiune p
p = 20
model = sm.tsa.AutoReg(time_series, lags=p)
results = model.fit()

# Afișarea seriei de timp originală și predicțiile
plt.figure(figsize=(10, 6))
plt.plot(time_series, label='Seria de timp originală')
plt.plot(results.fittedvalues, label='Predictii AR(p)')
plt.legend()
plt.title('Seria de timp originală și predicțiile AR(p)')
plt.show()

# (d) Tunarea hyperparametrilor pentru a găsi cea mai bună performanță de predicție
best_aic = np.inf
best_order = None
best_m = None

for p in range(1, 21):
    for m in range(1, 21):
        model = sm.tsa.AutoReg(time_series, lags=p)
        results = model.fit()
        aic = results.aic
        if aic < best_aic:
            best_aic = aic
            best_order = p
            best_m = m

print(f'Cea mai bună performanță de predicție: AR({best_order}), orizontul m = {best_m}, AIC = {best_aic}')