import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'Train.csv'
data = pd.read_csv(file_path)

data['Datetime'] = pd.to_datetime(data['Datetime'])

monday_start_index = data.loc[(data['Datetime'].dt.dayofweek == 0) & (data.index > 1010)].index[0]

one_month_from_monday = data.iloc[monday_start_index:monday_start_index + 24*30]

plt.figure(figsize=(15, 6))
plt.plot(one_month_from_monday['Datetime'], one_month_from_monday['Count'], color='green')
plt.title('O luna de trafic ')
plt.xlabel('Date')
plt.ylabel('Count')
plt.grid()
plt.tight_layout()
plt.show()
