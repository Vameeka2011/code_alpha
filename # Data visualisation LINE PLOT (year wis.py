import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Revenue': [12000, 13500, 12500, 15000, 17000],
    'Profit': [1200, 1500, 1000, 1800, 2000],
    'Expenses': [10800, 12000, 11500, 13200, 15000]
}

df = pd.DataFrame(data)   

#line plot yearly
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Revenue'], marker='o', label='Revenue', color='blue')
plt.plot(df['Year'], df['Profit'], marker='o', label='Profit', color='green')
plt.plot(df['Year'], df['Expenses'], marker='o', label='Expenses', color='red')
plt.title('Revenue, Profit, and Expenses Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount (in Crores)')
plt.legend()
plt.grid(True)
plt.show()


 # bar chart Revenue and profit 
df.plot(x='Year', y=['Revenue', 'Profit'], kind='bar', figsize=(8,6))
plt.title('Year-wise Revenue and Profit Comparison')
plt.ylabel('Amount (in Crores)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# profit margin 
df['Profit Margin (%)'] = (df['Profit'] / df['Revenue']) * 100

plt.figure(figsize=(8, 5))
sns.barplot(x='Year', y='Profit Margin (%)', data=df, palette='viridis')
plt.title('Profit Margin Over Years')
plt.ylabel('Profit Margin (%)')
plt.show()

#correlation Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(df[['Revenue', 'Profit', 'Expenses']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
