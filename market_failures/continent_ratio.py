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

NA_F = NA[NA['branch'] == 'F']['Duration']
NA_O = NA[NA['branch'] == 'O']['Duration']

print('NA Financial/Other')
print(float(NA_F.count())/float(NA_O.count()))


EU_F = EU[EU['branch'] == 'F']['Duration']
EU_O = EU[EU['branch'] == 'O']['Duration']

print('EU Financial/Other')
print(float(EU_F.count())/float(EU_O.count()))

AS_F = AS[AS['branch'] == 'F']['Duration']
AS_O = AS[AS['branch'] == 'O']['Duration']

print('AS Financial/Other')
print(float(AS_F.count())/float(AS_O.count()))

AF_F = AF[AF['branch'] == 'F']['Duration']
AF_O = AF[AF['branch'] == 'O']['Duration']

print('AF Financial/Other')
print(float(AF_F.count())/float(AF_O.count()+1))

SA_F = SA[SA['branch'] == 'F']['Duration']
SA_O = SA[SA['branch'] == 'O']['Duration']

print('SA Financial/Other')
print(float(SA_F.count())/float(SA_O.count()+1))