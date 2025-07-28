
# 📊 Sales Data EDA with Python

# 🔹 Step 1: Import Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For better visuals
sns.set(style='whitegrid')

# 🔹 Step 2: Generate Dummy Sales Data

np.random.seed(42)

dates = pd.date_range(start='2023-01-01', periods=180, freq='D')
categories = ['Furniture', 'Technology', 'Office Supplies']
regions = ['East', 'West', 'Central', 'South']

data = {
    'Order Date': np.random.choice(dates, 1000),
    'Category': np.random.choice(categories, 1000),
    'Region': np.random.choice(regions, 1000),
    'Sales': np.random.gamma(2, 100, 1000),
    'Discount': np.random.choice([0, 0.1, 0.2, np.nan], 1000, p=[0.6, 0.2, 0.1, 0.1])
}

df = pd.DataFrame(data)

# 🔹 Step 3: Basic Exploration

print("📌 First 5 Rows:\n", df.head(), "\n")
print("📌 Data Info:\n")
print(df.info())
print("\n📌 Summary Statistics:\n", df.describe())
print("\n📌 Missing Values:\n", df.isnull().sum())

# 🔹 Step 4: Handle Missing Values

df['Discount'].fillna(0, inplace=True)


# 🔹 Step 5: Feature Engineering

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')


# 🔹 Step 6: Monthly Sales Trend (Line Plot)

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='steelblue')
plt.title('📈 Monthly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 🔹 Step 7: Sales by Product Category (Bar Plot)

category_sales = df.groupby('Category')['Sales'].sum().sort_values()

plt.figure(figsize=(8, 5))
category_sales.plot(kind='barh', color='mediumseagreen')
plt.title('🛒 Sales by Product Category')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.show()


# 🔹 Step 8: Outlier Detection (Boxplot)

plt.figure(figsize=(8, 5))
sns.boxplot(x='Category', y='Sales', data=df, palette='Set2')
plt.title('📦 Sales Distribution by Category (Outlier Detection)')
plt.show()


# 🔹 Step 9: Save CSV (Optional)

df.to_csv('sales_data.csv', index=False)
from google.colab import files
files.download('sales_data.csv')

