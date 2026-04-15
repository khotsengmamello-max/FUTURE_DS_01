# 📊 Task 1: Business Sales Performance Analytics

**Intern:** Noliyolo Mamello Khotseng
**CIN ID:** FIT/APR26/DS16358
**Tools Used:** Python (Pandas, Matplotlib), Power BI, HTML/CSS/JavaScript

---

## 📊 Overview

This project focuses on analyzing business sales performance using a retail dataset. The goal was to transform raw sales data into meaningful insights that support strategic decision-making.

The project involved:

* Cleaning and preprocessing raw data using Python (Pandas)
* Performing exploratory data analysis (EDA)
* Creating visualizations with Matplotlib
* Building interactive dashboards using Power BI and HTML

The final solution provides a clear view of revenue trends, profitability, and regional performance.

---

## 🎯 Objectives

* Analyse overall business performance
* Identify top-performing categories and regions
* Detect seasonal sales trends
* Evaluate profitability and discount impact
* Present findings using dashboards and visualizations

---

## 📁 Files

| File                              | Description                                       |
| --------------------------------- | ------------------------------------------------- |
| `task1_analysis.py`               | Python script for data cleaning and visualization |
| `dashboard.html`                  | Interactive HTML dashboard                        |
| `Task1_PowerBI_Dashboard.pbix`    | Power BI dashboard file                           |
| `Sample - Superstore_CLEANED.csv` | Cleaned dataset used for analysis                 |

---

## 🧹 Data Preparation

The dataset was cleaned and prepared using the following steps:

* Removed missing and duplicate values
* Converted data types (e.g., dates and numeric fields)
* Created calculated fields such as profit margin
* Filtered irrelevant or inconsistent records

---

## 📈 Key Insights

| Metric                   | Value         |
| ------------------------ | ------------- |
| Total Revenue            | $2,297,200.86 |
| Total Profit             | $286,397.02   |
| Profit Margin            | 12.47%        |
| Best Performing Category | Technology    |
| Best Performing Region   | West          |

---

## 📊 Key Findings

* The **Technology** category generates the highest revenue and profit
* The **West** region consistently outperforms other regions
* Sales increase significantly during **November and December**
* High discount levels reduce overall profitability

---

## 💡 Recommendations

* Increase marketing investment in the **Technology** category
* Expand operations in the **West** region
* Improve inventory planning for peak sales periods (Nov–Dec)
* Re-evaluate discount strategies to protect profit margins

---

## 📊 Dashboard Preview

*(Add screenshots here for higher marks)*

Example:

```markdown
![Dashboard Screenshot](<img width="1419" height="798" alt="image" src="https://github.com/user-attachments/assets/24cccd79-f7d4-4148-843f-d18cb4584be7" />
)
```

---

## 🛠 How to Run

1. Install required libraries:

   ```bash
   pip install pandas matplotlib
   ```

2. Run the Python script:

   ```bash
   python task1_analysis.py
   ```

3. View the dashboard:

   * Open `dashboard.html` in your web browser

---

## ⚠️ Challenges Faced

1. **Data Quality Issues:** The raw dataset had missing values, duplicates, and inconsistent text formatting. Solved by using Pandas `dropna()`, `drop_duplicates()`, and `str.strip().str.title()`.

2. **Power BI Data Type Errors:** Sales and Profit columns were not recognized as numbers due to decimal separators. Fixed by replacing commas with periods and changing data type to Decimal.

3. **KPI Card Errors:** Power BI showed "Too many values" because it tried to display every row. Fixed by changing aggregation from raw field to **Sum**.

4. **Python Environment Issues:** VS Code couldn't find Python and showed red squiggly lines under imports. Fixed by installing Python 3.14.4, adding it to PATH, and selecting the correct interpreter in VS Code.

5. **Git Push Conflicts:** Had issues pushing to GitHub. Fixed by resetting the branch with `git reset --hard` and force pushing.

---

## 🚀 Future Improvements

* Add real-time data integration
* Enhance dashboard interactivity
* Include predictive analytics (sales forecasting)
* Deploy the dashboard as a web application

---

## 📫 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Noliyolo%20Khotseng-blue?style=for-the-badge\&logo=linkedin)]([https://www.linkedin.com/](https://www.linkedin.com/in/noliyolo-khotseng-318873233/))

---

⭐ *Future Interns Program – Data Science & Analytics Internship (April 2026)*
