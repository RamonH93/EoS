import pandas as pd
from lifelines.statistics import pairwise_logrank_test
from lifelines import KaplanMeierFitter
from lifelines.utils import datetimes_to_durations
from lifelines.statistics import logrank_test
from matplotlib import pyplot as plt
import itertools

data = pd.read_csv('durations.csv')
companies = pd.read_csv('companies.csv',keep_default_na=False,na_values=[''])

data['Duration'] = data['Duration'] / (60 * 60 * 24) 
data = data[data['Duration'] < 2500]
merged = data.set_index('Company').join(companies.set_index('company'))

NA = merged[merged['continent'] == 'NA']
SA = merged[merged['continent'] == 'SA']
AF = merged[merged['continent'] == 'AF']
OC = merged[merged['continent'] == 'OC']
EU = merged[merged['continent'] == 'EU']
AS = merged[merged['continent'].isin(['AS','ME'])]

financial = merged[merged['branch'] == 'F']
other = merged[merged['branch'] == 'O']

results = logrank_test(financial['Duration'], other['Duration'],financial['Observed'], other['Observed'],alpha=.95)
print('P value for Financial and \'Other\'= ' ,results.p_value)

countries = [NA, SA, AF, OC, EU, AS]

# kmf = KaplanMeierFitter()

# kmf.fit(financial['Duration'], financial['Observed'],label='Financial')
# ax = kmf.plot()

# kmf.fit(other['Duration'], other['Observed'],label='Other')
# ax = kmf.plot(ax=ax)
# ax.set_xscale('log')
# plt.show()

combinations = itertools.combinations(countries, 2)

for i in combinations:
    f,s = i
    print('Comparing ',f['continent'].iloc[0],' with ', s['continent'].iloc[0])
    results = logrank_test(f['Duration'], s['Duration'],f['Observed'], s['Observed'],alpha=.95)
    print('P value = ' ,results.p_value)

kmf = KaplanMeierFitter()
kmf.fit(AF['Duration'], AF['Observed'],label='AF')
ax = kmf.plot()

kmf.fit(EU['Duration'], EU['Observed'],label='EU')
ax = kmf.plot(ax=ax)

kmf.fit(AS['Duration'], AS['Observed'],label='AS')
ax = kmf.plot(ax=ax)

kmf.fit(OC['Duration'], OC['Observed'],label='OC')
ax = kmf.plot(ax=ax)

kmf.fit(NA['Duration'], NA['Observed'],label='NA')
ax = kmf.plot(ax=ax)

kmf.fit(SA['Duration'], SA['Observed'],label='SA')
ax = kmf.plot(ax=ax)
# ax.set_xscale('log')
plt.show()