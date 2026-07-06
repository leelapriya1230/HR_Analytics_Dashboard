
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Excel file
df = pd.read_excel("dataset/HR_Employee_Attrition_Sample.xlsx")

# Show first 5 rows
print(df.head())

# Total employees
total = len(df)
print("\nTotal Employees:", total)

# Employees who left
left = len(df[df["Attrition"] == "Yes"])
print("Employees Left:", left)

# Attrition Rate
attrition_rate = (left / total) * 100
print("Attrition Rate:", round(attrition_rate, 2), "%")

# Retention Rate
retention_rate = 100 - attrition_rate
print("Retention Rate:", round(retention_rate, 2), "%")

# Department-wise Attrition Chart
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Department", hue="Attrition")
plt.title("Department-wise Attrition")
plt.xticks(rotation=15)
plt.show()

# Gender-wise Attrition Chart
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender", hue="Attrition")
plt.title("Gender-wise Attrition")
plt.show()

# Salary Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["MonthlyIncome"], bins=20)
plt.title("Salary Distribution")
plt.show()