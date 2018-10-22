import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.utils import datetimes_to_durations
from matplotlib import pyplot as plt

data = pd.read_csv('durations.csv')
data['Duration'] = data['Duration'] / (60 * 60 * 24) 
data = data[data['Duration'] < 2500]

company1 = (data['Company'] == 'sulake')
company2 = (data['Company'] == 'paypal')
company3 = (data['Company'] == 'alibaba')

kmf = KaplanMeierFitter()

kmf.fit(data[company1]['Duration'], data[company1]['Observed'])
ax = kmf.plot()

kmf.fit(data[company2]['Duration'], data[company2]['Observed'])
ax = kmf.plot(ax=ax)

kmf.fit(data[company3]['Duration'], data[company3]['Observed'])
ax = kmf.plot(ax=ax)

plt.show()

