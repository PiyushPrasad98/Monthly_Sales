import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")





print(df.head())


df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract month
df["Month"] = df["Order Date"].dt.month

# Calculate monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

# Best and worst months
best_month = monthly_sales.idxmax()
worst_month = monthly_sales.idxmin()

print("\nMonthly Sales:\n", monthly_sales)
print("\nBest Month:", best_month)
print("Worst Month:", worst_month)


plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.grid(True)
plt.show()


plt.figure()
monthly_sales.plot(kind="bar")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Comparison")
plt.show()
