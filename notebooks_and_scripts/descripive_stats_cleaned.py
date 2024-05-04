import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define file paths for data input and output
input_path = "../Data/Raw Data/"
output_path_data = "../Data/Concatenated Data/"
output_path_figures = "../Figures & Images/"

# Load data for different years and rename columns appropriately
data_files = {
    "2016 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished'],
    "2017 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished'],
    "2018 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished'],
    "2019 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished'],
    "2020 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished'],
    "2021 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished'],
    "2022 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished'],
    "2023 Season.xlsx": ['NestID', 'County', 'Substrate', 'Latitude', 'Longitude', 'Status',
                         'Occupied', 'Active', 'Successful', 'Hatched', 'Fledged', 'Perished']
}

data_frames = []
for file_name, columns in data_files.items():
    df = pd.read_excel(input_path + file_name)
    df.columns = columns
    data_frames.append(df)

# Concatenate all DataFrames into one
combined_data = pd.concat(data_frames, ignore_index=True)

# Save concatenated DataFrame to CSV
combined_data.to_csv(output_path_data + "concatenated_data.csv", index=False)


# PLOTTING 
# Pairplot
sns.pairplot(combined_data)
plt.savefig(output_path_figures + "pairplot.png")
plt.show()

# Correlation heatmap
corr_df = combined_data[['Latitude', 'Longitude', 'Hatched', 'Fledged', 'Perished']].dropna().corr()
sns.heatmap(corr_df, annot=True)
plt.savefig(output_path_figures + "correlation_heatmap.png")
plt.show()

# Bar plot of 'County' occurrences
county_graph = combined_data['County'].value_counts().plot(kind='bar', title='Counts per County')
county_graph.set_xlabel('County')
county_graph.set_ylabel('Number per County')
plt.savefig(output_path_figures + "county_bar_plot.png")
plt.show()