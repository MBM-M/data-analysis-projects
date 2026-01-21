import pandas as pd

df = pd.read_csv('adult.data.csv')

series_data = df.squeeze('columns')

race_count = df['race'].value_counts()

men = df[df['sex'] == 'Male']
avgAgeMen = round(men['age'].mean(), 1)

bachelors = df[df['education'] == 'Bachelors']
percentBachelors = round(bachelors.shape[0]/df.shape[0]*100, 1)

highEdu = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
lowEdu = df[~df['education'].isin(["Bachelors", "Masters", "Doctorate"])]

highEduOver50k = round(highEdu[highEdu['salary'] == ">50K"].shape[0]/highEdu.shape[0]*100, 1)
lowEduOver50k = round(lowEdu[lowEdu['salary'] == ">50K"].shape[0]/lowEdu.shape[0]*100, 1)

minHours = df['hours-per-week'].min()
minHoursOver50k = df[(df["hours-per-week"] == minHours) & (df["salary"] == ">50K")].shape[0]

# What country has the highest percentage of people that earn >50K and what is that percentage?

# Group by native-country and calculate percentage of >50K
percentages = (df.groupby("native-country")["salary"] .apply(lambda x: (x == ">50K").mean() * 100))

# The max country and percentage:
maxCountry = percentages.idxmax()
maxPercentage = percentages.max()

# Identify the most popular occupation for those who earn >50K in India.

# Filter for India and >50K earners
indiaOver50k = df[(df['native-country'] == 'India') & (df["salary"] == ">50K")]

# Find the most common occupation
mostPopOcc = indiaOver50k["occupation"].value_counts().idxmax()
countOfIndiaOccOver50k = indiaOver50k["occupation"].value_counts().max()

print(f"How many people of each race are represented in this dataset?\n {race_count}")
print(f"The average age of men: {avgAgeMen}")
print(f"The percentage of people who have a Bachelor's degree: {percentBachelors}")
print(f"Percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K: {highEduOver50k}")
print(f"Percentage of people without advanced education make more than 50K: {lowEduOver50k}")
print(f"The minimum number of hours a person works per week: {minHours}")
print(f"percentage of the people who work the minimum number of hours per week have a salary of more than 50K: {minHoursOver50k}")
print(f"Country that has the highest percentage of people that earn >50K and what is that percentage: {maxCountry}, {maxPercentage}")
print(f"The most popular occupation for those who earn >50K in India: {mostPopOcc}, {countOfIndiaOccOver50k}")
