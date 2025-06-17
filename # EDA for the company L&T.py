# EDA for the company L&T
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample L&T Data
data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Revenue_Cr": [110000, 125000, 119000, 135000, 145000],
    "Net_Profit_Cr": [8000, 9500, 8700, 10200, 10800],
    "EPS": [45, 50, 48, 52, 55],
    "Debt_Cr": [30000, 32000, 34000, 31000, 29500],
    "ROE_Percent": [12.5, 13.2, 11.8, 14.0, 14.5],
    "Employee_Count": [42000, 43000, 41500, 44000, 45500]
}

df = pd.DataFrame(data)

#  Ask meaningful questions
print("Top-level EDA Questions:")
print("- Is profit increasing with revenue?")
print("- Has debt reduced over the years?")
print("- What is the trend in ROE and EPS?")

#  Explore structure
print("\nData Types and Structure:")
print(df.info())

#  Identify trends, patterns
print("\nStatistical Summary:")
print(df.describe())

#  Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

#  Line Plot for Trends
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Revenue_Cr'], marker='o', label='Revenue')
plt.plot(df['Year'], df['Net_Profit_Cr'], marker='o', label='Net Profit')
plt.title('Revenue and Profit Trend')
plt.xlabel('Year')
plt.ylabel('Amount (Cr)')
plt.legend()
plt.grid(True)
plt.show()

#  Debt Trend Analysis
plt.figure(figsize=(10, 4))
sns.barplot(x='Year', y='Debt_Cr', data=df, palette='viridis')
plt.title('Debt Trend Over Years')
plt.ylabel('Debt (in Crores)')
plt.show()

#(example)
# Hypothesis: Increase in Revenue leads to increase in Profit
correlation = df['Revenue_Cr'].corr(df['Net_Profit_Cr'])
print(f"\nCorrelation between Revenue and Profit: {correlation:.2f} (Strong Positive)" if correlation > 0.7 else "Weak correlation.")

#  Detect data issues
print("\nChecking for missing values:")
print(df.isnull().sum()) 