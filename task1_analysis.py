import pandas as pd
import matplotlib.pyplot as plt

# Purple color palette
PRIMARY_PURPLE = '#8B5CF6'
SECONDARY_PURPLE = '#A855F7'
LIGHT_PURPLE = '#C084FC'
DARK_PURPLE = '#6D28D9'

# ============================================
# 1. LOAD AND CLEAN DATA
# ============================================
print("Loading data...")
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
print(f"Original dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# Data cleaning
df = df.dropna(subset=['Sales', 'Profit', 'Order Date'])
df = df.drop_duplicates()
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Category'] = df['Category'].str.strip().str.title()
df['Region'] = df['Region'].str.strip().str.title()
df['Product Name'] = df['Product Name'].str.strip()
df['YearMonth'] = df['Order Date'].dt.to_period('M')

print(f"Cleaned dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# Save cleaned data
df.to_csv('Sample - Superstore_CLEANED.csv', index=False)
print("✅ Cleaned data saved to 'Sample - Superstore_CLEANED.csv'")

# Prepare data for charts
monthly_sales = df.groupby('YearMonth')['Sales'].sum()
product_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
profit_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

# ============================================
# 2. REVENUE TRENDS OVER TIME
# ============================================
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color=PRIMARY_PURPLE, linewidth=2, markerfacecolor=DARK_PURPLE, markersize=8)
plt.title('Revenue Trends Over Time', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('1_revenue_trends.png', dpi=150)
plt.close()

# ============================================
# 3. TOP 10 SELLING PRODUCTS
# ============================================
plt.figure(figsize=(12, 8))
product_sales.plot(kind='barh', color=PRIMARY_PURPLE, edgecolor=DARK_PURPLE)
plt.title('Top 10 Selling Products', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Total Sales ($)')
plt.ylabel('Product Name')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('2_top_products.png', dpi=150)
plt.close()

# ============================================
# 4. SALES BY CATEGORY
# ============================================
plt.figure(figsize=(10, 6))
colors = [PRIMARY_PURPLE, SECONDARY_PURPLE, LIGHT_PURPLE]
category_sales.plot(kind='bar', color=colors[:len(category_sales)], edgecolor=DARK_PURPLE)
plt.title('Sales by Category', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('3_category_sales.png', dpi=150)
plt.close()

# ============================================
# 5. SALES BY REGION
# ============================================
plt.figure(figsize=(10, 6))
colors = [PRIMARY_PURPLE, SECONDARY_PURPLE, LIGHT_PURPLE, '#E9D5FF']
region_sales.plot(kind='bar', color=colors[:len(region_sales)], edgecolor=DARK_PURPLE)
plt.title('Sales by Region', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('4_region_sales.png', dpi=150)
plt.close()

# ============================================
# 6. PIE CHART: SALES BY CATEGORY
# ============================================
plt.figure(figsize=(8, 8))
category_sales.plot(kind='pie', autopct='%1.1f%%', 
                    colors=[PRIMARY_PURPLE, SECONDARY_PURPLE, LIGHT_PURPLE], 
                    startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.title('Sales Distribution by Category', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.ylabel('')
plt.tight_layout()
plt.savefig('6_pie_category.png', dpi=150)
plt.close()

# ============================================
# 7. DONUT CHART (MODERN STYLE)
# ============================================
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(category_sales, autopct='%1.1f%%', startangle=90,
                                    colors=[PRIMARY_PURPLE, SECONDARY_PURPLE, LIGHT_PURPLE],
                                    wedgeprops={'edgecolor': 'white', 'linewidth': 2})
centre_circle = plt.Circle((0,0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)
plt.title('Sales Distribution by Category (Donut)', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.tight_layout()
plt.savefig('7_donut_category.png', dpi=150)
plt.close()

# ============================================
# 8. PROFIT BY CATEGORY
# ============================================
plt.figure(figsize=(10, 6))
profit_category.plot(kind='bar', color=PRIMARY_PURPLE, edgecolor=DARK_PURPLE)
plt.title('Profit by Category', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Category')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('8_profit_category.png', dpi=150)
plt.close()

# ============================================
# 9. MONTHLY GROWTH RATE (%)
# ============================================
monthly_sales_pct = monthly_sales.pct_change() * 100

plt.figure(figsize=(12, 6))
monthly_sales_pct.plot(kind='line', marker='o', color=PRIMARY_PURPLE, linewidth=2, markerfacecolor=DARK_PURPLE, markersize=8)
plt.title('Month-over-Month Sales Growth (%)', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Month')
plt.ylabel('Growth Rate (%)')
plt.axhline(y=0, color='red', linestyle='--', linewidth=1)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('9_monthly_growth.png', dpi=150)
plt.close()

# ============================================
# 10. SUMMARY STATISTICS
# ============================================
total_revenue = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_profit_margin = (total_profit / total_revenue) * 100

print("\n" + "="*50)
print("SUMMARY STATISTICS")
print("="*50)
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

print("\n✅ Task 1 Complete! Charts and summary saved.")
print("\n📁 Generated files:")
print("  - Sample - Superstore_CLEANED.csv")
print("  - 1_revenue_trends.png")
print("  - 2_top_products.png")
print("  - 3_category_sales.png")
print("  - 4_region_sales.png")
print("  - 5_task1_summary.csv")
print("  - 6_pie_category.png")
print("  - 7_donut_category.png")
print("  - 8_profit_category.png")
print("  - 9_monthly_growth.png")