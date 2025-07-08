import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('sales_data.csv')

# Check data
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Handle missing
df['Discount'].fillna(0, inplace=True)

# Create month
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Line plot
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar plot
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
plt.figure(figsize=(8,5))
category_sales.plot(kind='barh', color='teal')
plt.title('Sales by Product Category')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.show()

# Boxplot
sns.boxplot(x='Category', y='Sales', data=df)
plt.title('Sales Distribution by Category')
plt.show()
