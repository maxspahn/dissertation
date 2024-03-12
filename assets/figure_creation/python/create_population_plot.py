import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


year = sys.argv[1]
# Read data from CSV file
data = pd.read_csv(f'population_data_europe_{year}.csv')

# Set the font family to match LaTeX
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

plt.xkcd(randomness=5, scale=1)

# choose the colormap



group_size = 2
if group_size == 1:
    age_groups_combined = data['Age']
    male_population_combined = data['M']
    female_population_combined = data['F']
elif group_size == 2:
    age_groups_combined = [f"{data['Age'][i].split('-')[0]}-{data['Age'][i+1].split('-')[1]}" for i in range(0, len(data)-1, group_size)]
# Combine age groups by two
    age_groups_combined = [f"{data['Age'][i].split('-')[0]}-{data['Age'][i+1].split('-')[1]}" for i in range(0, len(data)-1, group_size)]
    male_population_combined = [data['M'][i] + data['M'][i+1] for i in range(0, len(data)-1, group_size)]
    female_population_combined = [data['F'][i] + data['F'][i+1] for i in range(0, len(data)-1, group_size)]

# Extract age groups, male population, and female population from the data
#age_groups = data['Age'][::-1]
# Reverse order
#male_population = data['M'][::-1]
#female_population = data['F'][::-1]

age_groups = np.array(age_groups_combined)[::-1]
male_population = np.array(male_population_combined)[::-1] / 10**6
female_population = np.array(female_population_combined)[::-1] / 10**6
# Calculate the positions for the bars on the y-axis
positions = np.arange(len(age_groups))

# Plotting the population pyramid
fig, ax = plt.subplots()
ax.barh(
    positions,
    male_population,
    align='center',
    label='Male',
    facecolor=[0, 156/255, 202/255, 0.8],
    #edgecolor=[0, 156/255, 202/255],
) 
ax.barh(
    positions,
    -female_population,
    align='center',
    label='Female',
    facecolor=[224/255, 118/255, 120/255, 0.8],
    #edgecolor=[224/255, 118/255, 120/255],
) 

# set no borders
ax.spines['top'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Inverting y-axis to have the youngest age group at the bottom
ax.invert_yaxis()

# Adding labels
ax.set_yticks(positions)
ax.set_yticklabels(age_groups)
ax.set_xlabel('Population in Millions')

# Adding a legend
ax.legend()

# Saving the plot as EPS file
plt.savefig(f'population_{year}.png', format='png', bbox_inches='tight')
plt.savefig(f'population_{year}.eps', format='eps', bbox_inches='tight')
#plt.show()


