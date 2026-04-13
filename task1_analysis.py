import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Purple color palette
PRIMARY_PURPLE = '#8B5CF6'
DARK_PURPLE = '#6D28D9'

# Load data
print("Loading data...")
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['YearMonth'] = df['Order Date'].dt.to_period('M')
df = df.dropna(subset=['Sales'])

# Prepare data for charts
monthly_sales = df.groupby('YearMonth')['Sales'].sum()
product_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

# Save all charts as files (so they exist for the dashboard)
print("Generating charts...")

# Chart 1: Revenue Trends
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color=PRIMARY_PURPLE, linewidth=2)
plt.title('Revenue Trends Over Time', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('1_revenue_trends.png', dpi=150)
plt.close()

# Chart 2: Top Products
plt.figure(figsize=(12, 8))
product_sales.plot(kind='barh', color=PRIMARY_PURPLE)
plt.title('Top 10 Selling Products', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Total Sales ($)')
plt.ylabel('Product Name')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('2_top_products.png', dpi=150)
plt.close()

# Chart 3: Categories
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color=PRIMARY_PURPLE)
plt.title('Sales by Category', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('3_category_sales.png', dpi=150)
plt.close()

# Chart 4: Regions
plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color=PRIMARY_PURPLE)
plt.title('Sales by Region', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('4_region_sales.png', dpi=150)
plt.close()

# Create summary CSV
total_revenue = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_profit_margin = (total_profit / total_revenue) * 100

summary = pd.DataFrame({
    'Metric': ['Total Revenue', 'Total Profit', 'Profit Margin', 'Best Category', 'Best Region', 'Top Product'],
    'Value': [
        f"${total_revenue:,.2f}",
        f"${total_profit:,.2f}",
        f"{avg_profit_margin:.2f}%",
        f"{category_sales.index[0]} (${category_sales.iloc[0]:,.2f})",
        f"{region_sales.index[0]} (${region_sales.iloc[0]:,.2f})",
        f"{product_sales.index[0][:50]} (${product_sales.iloc[0]:,.2f})"
    ]
})
summary.to_csv('5_task1_summary.csv', index=False)

print("✅ All charts saved to files!")
print("\n" + "="*50)
print("SUMMARY STATISTICS")
print("="*50)
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Profit Margin: {avg_profit_margin:.2f}%")
print(f"Best Category: {category_sales.index[0]} (${category_sales.iloc[0]:,.2f})")
print(f"Best Region: {region_sales.index[0]} (${region_sales.iloc[0]:,.2f})")
print(f"Top Product: {product_sales.index[0][:50]}...")

print("\n" + "="*50)
print("✅ TASK 1 COMPLETED SUCCESSFULLY!")
print("="*50)
print("\n📁 Generated files:")
print("  - 1_revenue_trends.png")
print("  - 2_top_products.png")
print("  - 3_category_sales.png")
print("  - 4_region_sales.png")
print("  - 5_task1_summary.csv")