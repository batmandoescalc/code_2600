import pandas as pd
import numpy as np


Credit = pd.read_csv('data/Credit.csv')
print("First 5 rows of the data:\n", Credit.head(), "\n")


print("Feature names:", list(Credit.columns), "\n")


print("Data types:\n", Credit.dtypes, "\n")


mean_age = Credit['Age'].mean()
median_age = Credit['Age'].median()
mode_age = Credit['Age'].mode()[0]

print("Mean Age:", mean_age)
print("Median Age:", median_age)
print("Mode Age:", mode_age, "\n")


Subset = Credit[['Age', 'Region', 'Income']]
print("Subset (first 5 rows):\n", Subset.head(), "\n")

Younger = Subset[Subset['Age'] < 50]
Older = Subset[Subset['Age'] >= 50]

print("Number of records with Age < 50:", Younger.shape[0])
print("Number of records with Age >= 50:", Older.shape[0], "\n")


mean_young = Younger['Income'].mean()
mean_old = Older['Income'].mean()
median_young = Younger['Income'].median()
median_old = Older['Income'].median()

print("Mean Income (Age < 50):", mean_young)
print("Mean Income (Age >= 50):", mean_old)
print("Median Income (Age < 50):", median_young)
print("Median Income (Age >= 50):", median_old, "\n")


print("Observation: If the median is less than the mean, then we have that the distribution is right-skewed.")
print("If the median is larger than the mean, then the distribution is left-skewed.\n")


regions = Credit['Region'].unique()
print("Possible values for Region:", regions, "\n")


region_counts = Credit['Region'].value_counts()
print("Frequency table for Region:\n", region_counts, "\n")


income_student = Credit[Credit['Student'] == 'Yes']['Income'].mean()
income_nonstudent = Credit[Credit['Student'] == 'No']['Income'].mean()
print("Average Income for Students:", income_student)
print("Average Income for Non-Students:", income_nonstudent, "\n")


Credit['Utilization'] = Credit['Balance'] / Credit['Limit']
print("First 5 rows with Utilization:\n", Credit[['Balance', 'Limit', 'Utilization']].head(), "\n")


max_util = Credit['Utilization'].max()
print("Maximum utilization value:", max_util)
