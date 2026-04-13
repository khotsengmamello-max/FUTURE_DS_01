import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better looking charts
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Define purple color palette
PRIMARY_PURPLE = '#8B5CF6'     # Vivid Purple
SECONDARY_PURPLE = '#A855F7'   # Light Purple
LIGHT_PURPLE = '#C084FC'       # Soft Purple
DARK_PURPLE = '#6D28D9'        # Deep Purple
PALE_PURPLE = '#E9D5FF'        # Pale Purple

# ============================================
# 1. LOAD THE DATA
# ============================================
print("Loading data...")
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ============================================
# 2. DATA CLEANING
# ============================================
print("\n--- Data Cleaning ---")

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Year-Month column for trends
df['YearMonth'] = df['Order Date'].dt.to_period('M')

# Remove any rows with missing Sales
df = df.dropna(subset=['Sales'])

print(f"Data cleaned. Rows remaining: {df.shape[0]}")

# ============================================
# 3. REVENUE TRENDS OVER TIME
# ============================================
print("\n--- Analyzing Revenue Trends ---")

monthly_sales = df.groupby('YearMonth')['Sales'].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color=PRIMARY_PURPLE, linewidth=2, markerfacecolor=DARK_PURPLE, markersize=8)
plt.title('Revenue Trends Over Time', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('1_revenue_trends.png', dpi=150)
plt.show()

print(f"Highest sales month: {monthly_sales.idxmax()} (${monthly_sales.max():,.2f})")
print(f"Lowest sales month: {monthly_sales.idxmin()} (${monthly_sales.min():,.2f})")

# ============================================
# 4. TOP-SELLING PRODUCTS
# ============================================
print("\n--- Analyzing Top Products ---")

product_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 8))
product_sales.plot(kind='barh', color=PRIMARY_PURPLE, edgecolor=DARK_PURPLE)
plt.title('Top 10 Selling Products', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Total Sales ($)', fontsize=12)
plt.ylabel('Product Name', fontsize=12)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('2_top_products.png', dpi=150)
plt.show()

print(f"Top product: {product_sales.index[0]}")
print(f"Top product sales: ${product_sales.iloc[0]:,.2f}")

# ============================================
# 5. HIGH-VALUE CATEGORIES
# ============================================
print("\n--- Analyzing Categories ---")

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
colors = [PRIMARY_PURPLE, SECONDARY_PURPLE, LIGHT_PURPLE]
category_sales.plot(kind='bar', color=colors[:len(category_sales)], edgecolor=DARK_PURPLE)
plt.title('Sales by Category', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('3_category_sales.png', dpi=150)
plt.show()

for i, (cat, sales) in enumerate(category_sales.items(), 1):
    print(f"{i}. {cat}: ${sales:,.2f}")

# ============================================
# 6. REGIONAL PERFORMANCE
# ============================================
print("\n--- Analyzing Regions ---")

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
colors = [PRIMARY_PURPLE, SECONDARY_PURPLE, LIGHT_PURPLE, PALE_PURPLE]
region_sales.plot(kind='bar', color=colors[:len(region_sales)], edgecolor=DARK_PURPLE)
plt.title('Sales by Region', fontsize=16, fontweight='bold', color=DARK_PURPLE)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('4_region_sales.png', dpi=150)
plt.show()

for i, (region, sales) in enumerate(region_sales.items(), 1):
    print(f"{i}. {region}: ${sales:,.2f}")

# ============================================
# 7. SUMMARY STATISTICS & INSIGHTS
# ============================================
print("\n" + "="*50)
print("SUMMARY STATISTICS")
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

# ============================================
# 8. ACTIONABLE RECOMMENDATIONS
# ============================================
print("\n" + "="*50)
print("ACTIONABLE RECOMMENDATIONS")
print("="*50)

print(f"\n1. FOCUS ON TOP CATEGORY: {category_sales.index[0]}")
print(f"   - This category generates ${category_sales.iloc[0]:,.2f} in revenue")
print(f"   - Recommend increasing marketing budget for this category")

print(f"\n2. EXPAND IN TOP REGION: {region_sales.index[0]}")
print(f"   - This region generates ${region_sales.iloc[0]:,.2f} in revenue")
print(f"   - Consider opening new locations or increasing inventory here")

print(f"\n3. PROMOTE TOP PRODUCT: {product_sales.index[0][:50]}...")
print(f"   - This product alone generates ${product_sales.iloc[0]:,.2f}")
print(f"   - Feature it prominently in marketing campaigns")

print(f"\n4. SEASONAL TREND OBSERVATION:")
print(f"   - Peak sales month: {monthly_sales.idxmax()} (${monthly_sales.max():,.2f})")
print(f"   - Increase inventory and staffing during this period")

print(f"\n5. PROFIT MARGIN IMPROVEMENT:")
print(f"   - Current profit margin: {avg_profit_margin:.2f}%")
print(f"   - Review discount strategies and supplier costs to improve margins")

# ============================================
# 9. EXPORT RESULTS
# ============================================

# Create a summary DataFrame
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
print("\n✅ Summary exported to '5_task1_summary.csv'")

print("\n" + "="*50)
print("✅ TASK 1 COMPLETED SUCCESSFULLY!")
print("="*50)
print("\n📁 Generated files:")
print("  - 1_revenue_trends.png")
print("  - 2_top_products.png")
print("  - 3_category_sales.png")
print("  - 4_region_sales.png")
print("  - 5_task1_summary.csv")