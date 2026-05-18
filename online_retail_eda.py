# =====================================================
# ONLINE RETAIL DATA ANALYSIS (EDA)
# =====================================================

# Objective:
# Clean and analyze e-commerce data to uncover insights

# =====================================================
# 1. IMPORT LIBRARIES
# =====================================================
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create folder for saving visuals
os.makedirs("visuals", exist_ok=True)

# =====================================================
# 2. LOAD DATA
# =====================================================
df = pd.read_csv("OnlineRetail.csv", encoding="latin1")

print(df.head())
print("Shape:", df.shape)

# =====================================================
# 3. DATA CLEANING
# =====================================================

# Remove missing values
df = df.dropna(subset=["CustomerID", "Description"])

# Remove duplicates
df = df.drop_duplicates()

# Convert data types
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["CustomerID"] = df["CustomerID"].astype(str).str.replace(".0", "", regex=False)

# Remove cancelled and invalid transactions
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# =====================================================
# 4. FEATURE ENGINEERING
# =====================================================
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.to_period("M")

# =====================================================
# 5. VISUALIZATION STYLE
# =====================================================
sns.set_style("whitegrid")

# Helper function to save charts
def save_plot(filename):
    plt.tight_layout()
    plt.savefig(f"visuals/{filename}", bbox_inches="tight")
    plt.show()

# =====================================================
# 6. TOP SELLING PRODUCTS
# =====================================================
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=top_products.values, y=top_products.index)

plt.title("Top 10 Selling Products")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")

# Add values inside bars
ax.bar_label(ax.containers[0], fmt="%.0f")

# Fix layout issues (IMPORTANT)
plt.tight_layout()
plt.subplots_adjust(left=0.35)

save_plot("top_selling_Products.png")

# =====================================================
# 7. REVENUE BY COUNTRY
# =====================================================
country_sales = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=country_sales.values, y=country_sales.index)

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Country")

# Add values inside bars
for i, v in enumerate(country_sales.values):
    plt.text(v, i, f"{v:,.0f}", va="center", fontsize=10)

save_plot("country_revenue.png")

# =====================================================
# 8. MONTHLY REVENUE TREND
# =====================================================
monthly_sales = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(12, 6))
monthly_sales.sort_index().plot(marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid()

save_plot("monthly_trend.png")

# =====================================================
# 9. TOP CUSTOMERS
# =====================================================
top_customers = df.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=top_customers.values, y=top_customers.index)

plt.title("Top Customers by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Customer ID")

# Add values inside bars
for i, v in enumerate(top_customers.values):
    plt.text(v, i, f"{v:,.0f}", va="center", fontsize=10)

save_plot("top_customers.png")

# =====================================================
# 10. SAVE CLEANED DATASET
# =====================================================
df.to_csv("OnlineRetail_Cleaned.csv", index=False)

print("Analysis complete. Cleaned dataset and visuals saved!")