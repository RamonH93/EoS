import pandas as pd
from lifelines import CoxPHFitter
from matplotlib import pyplot as plt

data = pd.read_csv('durations.csv')
data['duration'] = data['duration'] / (60 * 60 * 24)
data = data[data['duration'] < 2500]

company_data = pd.read_csv('companies.csv', keep_default_na=False, na_values=[''])
data = data.set_index('company').join(company_data.set_index('company'))


branch_data = data[['duration', 'observed', 'branch']]
branch_data = branch_data[branch_data['branch'].notnull()]
branch_data = branch_data.sample(frac=0.05, replace=True)
branch_data['branch'] = branch_data['branch'].apply(lambda x: 1 if x == 'F' else 0)

fph = CoxPHFitter()
res = fph.fit(branch_data, duration_col='duration', event_col='observed')

branch_summary = res.summary

roundf = lambda x: format(x, '.4f')

branch_summary['coef'] = branch_summary['coef'].apply(roundf)
branch_summary['exp(coef)'] = branch_summary['exp(coef)'].apply(roundf)
branch_summary['se(coef)'] = branch_summary['se(coef)'].apply(roundf)
branch_summary['z'] = branch_summary['z'].apply(roundf)
branch_summary['p'] = branch_summary['p'].apply(roundf)
branch_summary['lower 0.95'] = branch_summary['lower 0.95'].apply(roundf)
branch_summary['upper 0.95'] = branch_summary['upper 0.95'].apply(roundf)

print(branch_summary)

# continent
for continent in ['NA', 'SA', 'EU', 'AF', 'AS', 'OC']:
    continent_data = data[['duration', 'observed', 'continent']]
    continent_data = continent_data[continent_data['continent'].notnull()]
    continent_data = continent_data.sample(frac=0.05, replace=True)
    continent_data['continent'] = continent_data['continent'].apply(lambda x: 1 if x == continent else 0)

    fph = CoxPHFitter()
    res = fph.fit(continent_data, duration_col='duration', event_col='observed')

    print(continent)

    continent_summary = res.summary
    continent_summary['continent'] = continent
    continent_summary.set_index('continent', inplace = True)

    if continent_res is None:
        continent_res = continent_summary
    else:
        continent_res = pd.concat([continent_res, continent_summary], axis=0)


roundf = lambda x: format(x, '.4f')

continent_res['coef'] = continent_res['coef'].apply(roundf)
continent_res['exp(coef)'] = continent_res['exp(coef)'].apply(roundf)
continent_res['se(coef)'] = continent_res['se(coef)'].apply(roundf)
continent_res['z'] = continent_res['z'].apply(roundf)
continent_res['p'] = continent_res['p'].apply(roundf)
continent_res['lower 0.95'] = continent_res['lower 0.95'].apply(roundf)
continent_res['upper 0.95'] = continent_res['upper 0.95'].apply(roundf)

print(continent_res)

