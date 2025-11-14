# Importing Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("employee_attrition.csv")

# Convert Attrition column to numeric (Yes = 1, No = 0)
data['Attrition'] = data['Attrition'].map({'Yes': 1, 'No': 0})

# Create Age Groups for visualization
bins = [18, 30, 40, 50, 60]
labels = ['<30', '31–40', '41–50', '51+']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, include_lowest=True)

# 1. ATTRITION BY AGE (Bar Chart)
plt.figure(figsize=(8, 5))
age_attrition = data.groupby('AgeGroup')['Attrition'].mean()

age_attrition.plot(kind='bar', color=['gray', 'black', 'gray', 'black'])
plt.title("Attrition by Age", fontsize=14)
plt.ylabel("Attrition Rate")
plt.xlabel("Age Groups")
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()

# 2. ATTRITION BY MONTHLY INCOME (Box Plot)
plt.figure(figsize=(8, 5))
sns.boxplot(x=data['MonthlyIncome'], y=data['Attrition'])
plt.title("Attrition by Monthly Income", fontsize=14)
plt.xlabel("Monthly Income")
plt.ylabel("Attrition")
plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.show()

# 3. CORRELATION HEATMAP (Age, MonthlyIncome, JobSatisfaction, YearsAtCompany)
corr_columns = ['Age', 'MonthlyIncome', 'JobSatisfaction', 'YearsAtCompany', 'Attrition']
corr_matrix = data[corr_columns].corr()

plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="Greys", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()