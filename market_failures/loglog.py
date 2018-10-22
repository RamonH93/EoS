import pandas as pd
from lifelines import CoxPHFitter, KaplanMeierFitter
from matplotlib import pyplot as plt


data = pd.read_csv('durations.csv')
data['duration'] = data['duration'] / (60 * 60 * 24)
data = data[data['duration'] < 2500]

companies = pd.read_csv('companies.csv',keep_default_na=False,na_values=[''])

merged = data.set_index('company').join(companies.set_index('company'))

data_not_empty = merged.copy()
data_not_empty = data_not_empty.dropna()

countries = ['NA', 'SA', 'AF', 'OC', 'EU', 'ME']

fig = plt.figure(figsize=(10,12))
plt.subplots_adjust(hspace=0.4)

for i, continent in enumerate(countries):
    continent_data = data_not_empty[data_not_empty['continent'] == continent]
    other_data = data_not_empty[data_not_empty['continent'] != continent]

    kmf_continent = KaplanMeierFitter()
    kmf_continent.fit(continent_data['duration'], continent_data['observed'])

    kmf_other = KaplanMeierFitter()
    kmf_other.fit(other_data['duration'], other_data['observed'])

    ax = fig.add_subplot(3, 2, i+1)
    ax.set_title('{} vs other'.format(continent))
    kmf_continent.plot_loglogs(ax=ax, label=continent)
    kmf_other.plot_loglogs(ax=ax, label='other')

fig.show()

data_financial = merged[merged['branch'] == 'F']
data_other = merged[merged['branch'] == 'O']

kmf_financial = KaplanMeierFitter()
kmf_financial.fit(data_financial['duration'], data_financial['observed'])

kmf_other = KaplanMeierFitter()
kmf_other.fit(data_other['duration'], data_other['observed'])

fig, axes = plt.subplots()
kmf_financial.plot_loglogs(ax=axes)
kmf_other.plot_loglogs(ax=axes)

axes.legend(['Financial', 'Other'])

plt.show()
