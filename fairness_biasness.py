import os
import json5
import pandas as pd
import matplotlib.pyplot as plt



data_dir = './dump_data'

all_files = os.listdir(data_dir)
print(f"All files: {all_files}")



# Verify the content and structure of the files
data_entries = []
file_count = 0

for file_name in all_files:
    if file_name.startswith('sdgIndicatorData__') and file_name.endswith('.json5'):
        file_path = os.path.join(data_dir, file_name)
        file_count += 1
        with open(file_path, 'r') as f:
            try:
                data = json5.load(f)
                print(f"Loaded data from {file_name}: {data.keys()}")  # Print the keys to verify structure
                if 'data' in data:
                    data_entries.extend(data['data'])
            except Exception as e:
                print(f"Error loading {file_path}: {e}")

print(f"Total files processed: {file_count}")
print(f"Total data entries loaded: {len(data_entries)}")
if len(data_entries) > 0:
    print(json5.dumps(data_entries[0], indent=2))
else:
    print("No data entries loaded.")


for d in data_entries:
    print("\n\n\n\n\n data_entries: ", d)

# Convert to DataFrame
df = pd.DataFrame(data_entries)

# Convert 'value' column to numeric
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Display the DataFrame
print("\n\n\n\n\n\n\n data frame",df)

print("\n\n\n\n\n data_entries: ", data_entries)

# # Visualize the distribution of values by geoAreaName and series
# plt.figure(figsize=(12, 8))
# sns.boxplot(x='geoAreaName', y='value', hue='series', data=df)
# plt.xticks(rotation=90)
# plt.title('Distribution of Poverty Data by Geo Area and Series')
# plt.show()


# from scipy.stats import ks_2samp

# # Function to compare distributions
# def compare_distributions(group1, group2):
#     stat, p_value = ks_2samp(group1, group2)
#     return p_value

# # Compare distributions across 'Sex'
# male_values = df[df['dimensions.Sex'] == 'MALE']['value']
# female_values = df[df['dimensions.Sex'] == 'FEMALE']['value']

# p_value = compare_distributions(male_values, female_values)
# print(f'P-value for comparing male and female distributions: {p_value}')




# # Distribution of 'value' across different 'geoAreaName'
# plt.figure(figsize=(14, 7))
# sns.boxplot(data=df, x='geoAreaName', y='value')
# plt.xticks(rotation=90)
# plt.title('Distribution of Values Across Different Geo Areas')
# plt.show()

# # Distribution of 'value' across different 'Sex'
# plt.figure(figsize=(14, 7))
# sns.boxplot(data=df, x=df['dimensions.Sex'], y='value')
# plt.title('Distribution of Values Across Different Sex')
# plt.show()