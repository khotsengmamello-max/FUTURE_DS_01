import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Purple color
PRIMARY_PURPLE = '#8B5CF6'
DARK_PURPLE = '#6D28D9'

# ============================================
# STEP 1: LOAD RAW DATA
# ============================================
print("Loading raw data...")
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
print(f"Original: {df.shape[0]} rows, {df.shape[1]} columns")

# ============================================
# STEP 2: DATA CLEANING
# ============================================
print("\n--- Cleaning Data ---")

# 2.1 Remove missing values
df = df.dropna(subset=['Sales', 'Profit', 'Order Date'])

# 2.2 Remove duplicates
df = df.drop_duplicates()

# 2.3 Fix data types
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 2.4 Standardize text columns
df['Category'] = df['Category'].str.strip().str.title()
df['Region'] = df['Region'].str.strip().str.title()
df['Product Name'] = df['Product Name'].str.strip()

# 2.5 Create useful columns
df['YearMonth'] = df['Order Date'].dt.to_period('M')
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

print(f"Cleaned: {df.shape[0]} rows, {df.shape[1]} columns")

# 2.6 Save cleaned data
df.to_csv('Sample - Superstore_CLEANED.csv', index=False)
print("✅ Cleaned data saved to 'Sample - Superstore_CLEANED.csv'")

# ============================================
# STEP 3: PREPARE DATA FOR CHARTS
# ============================================
print("\n--- Preparing Charts ---")

monthly_sales = df.groupby('YearMonth')['Sales'].sum()
product_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

# ============================================
# STEP 4: GENERATE CHARTS FROM CLEANED DATA
# ============================================

# Chart 1: Revenue Trends
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color=PRIMARY_PURPLE, linewidth=2)
plt.title('Revenue Trends Over Time (Cleaned Data)', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('1_revenue_trends.png', dpi=150)
plt.close()

# Chart 2: Top Products
plt.figure(figsize=(12, 8))
product_sales.plot(kind='barh', color=PRIMARY_PURPLE)
plt.title('Top 10 Selling Products (Cleaned Data)', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Total Sales ($)')
plt.ylabel('Product Name')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('2_top_products.png', dpi=150)
plt.close()

# Chart 3: Categories
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color=PRIMARY_PURPLE)
plt.title('Sales by Category (Cleaned Data)', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('3_category_sales.png', dpi=150)
plt.close()

# Chart 4: Regions
plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color=PRIMARY_PURPLE)
plt.title('Sales by Region (Cleaned Data)', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('4_region_sales.png', dpi=150)
plt.close()

# ============================================
# STEP 5: SUMMARY STATISTICS
# ============================================
print("\n" + "="*50)
print("SUMMARY STATISTICS (FROM CLEANED DATA)")
print("="*50)

total_revenue = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_profit_margin = (total_profit / total_revenue) * 100

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Profit Margin: {avg_profit_margin:.2f}%")
print(f"Number of Orders: {df['Order ID'].nunique():,}")
print(f"Number of Products: {df['Product Name'].nunique():,}")
print(f"Number of Customers: {df['Customer ID'].nunique():,}")

# Save summary
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

print("\n✅ Task 1 Complete! Charts regenerated from CLEANED data.")
print("\n📁 Generated files:")
print("  - Sample - Superstore_CLEANED.csv (cleaned dataset)")
print("  - 1_revenue_trends.png (from cleaned data)")
print("  - 2_top_products.png (from cleaned data)")
print("  - 3_category_sales.png (from cleaned data)")
print("  - 4_region_sales.png (from cleaned data)")
print("  - 5_task1_summary.csv")