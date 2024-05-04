import numpy as np
import pandas
import pandas as pd
import matplotlib.pyplot as plt
import pgeocode
import seaborn as sns


data_2016 = pandas.read_excel("2016 Season.xlsx")
data_2017 = pandas.read_excel("2017 Season.xlsx")
data_2018 = pandas.read_excel("2018 Season.xlsx")
data_2019 = pandas.read_excel("2019 Season.xlsx")
data_2020 = pandas.read_excel("2020 Season.xlsx")
data_2021 = pandas.read_excel("2021 Season.xlsx")
data_2022 = pandas.read_excel("2022 Season.xlsx")
data_2023 = pandas.read_excel("2023 Season.xlsx")

# print(data_2016.to_string())
# print(data_2017.describe())
# print(data_2018.describe())
# print(data_2019.describe())
# print(data_2020.describe())
# print(data_2021.describe().to_string())
# print(data_2022.describe().to_string())
# print(data_2023.describe().to_string())

frames = [data_2016, data_2017, data_2018, data_2019, data_2020, data_2021, data_2022, data_2023]

# result = pandas.concat(frames)

# print(result.describe().to_string())
# print(list(data_2016))
# print(list(data_2017))
data_2019 = data_2019.drop(['Unnamed: 11', 'Unnamed: 12'], axis=1)
data_2018 = data_2018.drop(['Unnamed: 11'], axis=1)
data_2021 = data_2021.drop(['Unnamed: 12', 'Unnamed: 13'], axis=1)
# data_2021= data_2021.drop(['Unnamed: 12', 'Unnamed: 13'], axis=1)
# data_2018 = data_2018.drop(['Unnamed: 11'], axis=1)
# data_2021 = data_2021.drop(['Unnamed: 11'], axis=1)
# data_2021 = data_2021.drop(['Unnamed: 12', 'Unnamed: 13'], axis=1)

# data_2020 = data_2020.drop(['Unnamed: 11'], axis=1)

# data_2022 = data_2022.drop(['Unnamed: 11'], axis=1)
# data_2023 = data_2023.drop(['Unnamed: 11'], axis=1)

# print(data_2018.to_string())
# print(list(data_2019))
# print(list(data_2020))
# print(list(data_2021))
# print(list(data_2022))
# print(list(data_2023))

data_2016.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
data_2017.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
data_2018.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
data_2019.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
data_2020.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status', 'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
data_2021.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status', 'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
data_2022.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status', 'Occupied','Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
data_2023.columns = ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status', 'Occupied',  'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']

# print(data_2016.columns)
# print(data_2017.columns)
# print(data_2018.columns)
# print(data_2019.columns)
# print(data_2020.columns)
# print(data_2021.columns)
# print(data_2022.columns)
# print(data_2023.columns)


# data_2016.columns = []
# what is unnamed 11?

# data_2016.dropna(subset=['Lat', 'Long'], inplace=True)
# na_numbers = data_2016.isna().sum()/len(data_2016)
# print(na_numbers)
# print(data_2016)


frames = [data_2016, data_2017, data_2018, data_2019, data_2020, data_2021, data_2022, data_2023]

result = pandas.concat(frames, ignore_index=True)
# print(result.describe())

# graph = sns.pairplot(result)
# plt.show()

# corr_df = result[['Latitude', 'Longitude', 'Hatched', 'Fledged', 'Perished']].dropna().corr()
#
# corr_map = sns.heatmap(corr_df)
# plt.show()


# county_graph = result['County'].value_counts().plot(kind='bar', title='Times Each County Mentioned in Data Set')
#
# county_graph.set_xlabel('County')
# county_graph.set_ylabel('number per county')
# plt.show()

# print(result.to_string())

# substrate_graph = result['Substrate'].value_counts().plot(kind='bar', title='Frequency of Substrate')
# substrate_graph.set_xlabel('Substrate')
# substrate_graph.set_ylabel('Frequency')

# scatter_plot = result['Latitude', 'Longitude'].plot(kind='scatt', title='Lat and Longitude')


# survival_graph = result['Hatched'].value_counts().plot(kind='bar', title='Hatched')
#
# survival_graph.set_xlabel('Condition')
# survival_graph.set_ylabel('Frequency')

# survival_graph = result['Fledged'].value_counts().plot(kind='bar', title='Fledged ')
# survival_graph = result['Perished'].value_counts().plot(kind='bar', title='Perished ')

plt.show()