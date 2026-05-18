# Online Retail Data Analysis (EDA)

Week 1 Internship Task (AnalystLab Africa) – Exploratory Data Analysis of Online Retail dataset to uncover sales trends, customer behavior, product performance, and revenue insights using Python (Pandas, Matplotlib, Seaborn).

---

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on an Online Retail dataset to uncover insights about:

- Sales performance  
- Customer behavior  
- Product trends  
- Revenue distribution across countries  

The goal is to transform raw transactional data into meaningful business insights using Python.

---

## Objectives
- Clean and prepare raw e-commerce data  
- Analyze sales patterns and customer behavior  
- Identify top-performing products and markets  
- Generate actionable business insights  

---

## Tools & Libraries
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## Dataset
This project uses the Online Retail dataset containing transactional data for a UK-based online store.

- **Source:** Kaggle – https://www.kaggle.com/datasets/vijayuv/onlineretail  

---

## Project Workflow

### 1. Data Import
Loaded dataset using Pandas with proper encoding to handle special characters.

### 2. Data Cleaning
- Removed missing values (CustomerID, Description)  
- Removed duplicates  
- Converted data types (InvoiceDate, CustomerID)  
- Removed cancelled transactions  
- Filtered invalid quantities and unit prices  

### 3. Feature Engineering
Created new variables:
- Revenue = Quantity × UnitPrice  
- Year  
- Month  

---

## Exploratory Data Analysis (EDA)

### Top Selling Products
Identified top 10 products based on quantity sold.

### Revenue by Country
Analyzed top 10 countries contributing highest revenue.

### Monthly Revenue Trend
Explored seasonal patterns and revenue fluctuations over time.

### Top Customers
Identified top 10 customers contributing highest revenue.

---

## Key Insights

- The United Kingdom is the dominant market in terms of revenue.  
- A small group of customers contributes a large portion of total sales.  
- Sales show seasonal fluctuations across months.  
- Product demand is highly concentrated in a few top items.  
- Most transactions are small-scale retail purchases.  

---

## Output
After data cleaning and feature engineering, the final processed dataset was saved for further analysis and reuse:
- **File Name:** `OnlineRetail_Cleaned.csv`
