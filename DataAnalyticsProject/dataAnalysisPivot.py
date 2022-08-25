import pandas as pd

import matplotlib.pyplot as plt



df_gdp = pd.read_csv('Data/gdp.csv', encoding = 'latin1')

print(df_gdp.pivot('year', 'country', 'gdppc'))

df_sales = pd.read_excel('Data/supermarket_sales.xlsx')
print(df_sales.pivot_table('Total', 'Gender', 'Customer type', 'sum'))


df_population_raw = pd.read_csv('Data/population_total.csv')

df_population_raw = df_population_raw.dropna()

df_pop_pivot = df_population_raw.pivot('year', 'country', 'population')

df_pop_pivot_sorted = df_pop_pivot[['United States', 'India', 'China']]

df_pop_pivot_sorted.plot(kind='line', xlabel='Year', ylabel='Population', title='Population 1955-2020', figsize=(8,4))

df_pop_pivot_filtered = df_pop_pivot_sorted[df_pop_pivot_sorted.index.isin([2020])].T

df_pop_pivot_filtered.plot(kind='bar')
plt.show()