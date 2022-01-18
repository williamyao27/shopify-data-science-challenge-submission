# This file processes the csv file provided for Q1 and returns various metrics of interest to our
# discussion. It is written by William Yao for the 2022 Shopify Data Science Intern Challenge.

import csv
import pandas as pd


# Load data from the provided .csv file into a DataFrame.
q1_df = pd.read_csv("q1_data.csv")

# Create a new column of price per sneaker in each order, as this metric is not listed in the
# original dataset.
q1_df["sneaker_price"] = round(q1_df["order_amount"] / q1_df["total_items"], 2)

# Print to console a preview of the DataFrame for visual reference.
print("Data preview:\n", q1_df.head())

# Print to console an overview of the DataFrame; in particular, we should calculate the mean order
# value to replicate the AOV problem outlined in q1_df.
print("\nTime period:", q1_df["created_at"].min(), "to", q1_df["created_at"].max())
print("Number of stores:", q1_df["shop_id"].nunique())
print("Any missing entries?", q1_df.isnull().values.any())

# Order amount metrics
print("\nMean order amount: ", round(q1_df["order_amount"].mean(), 2))
print("Median order amount: ", round(q1_df["order_amount"].median(), 2))
print("Range of order amount: ", round(q1_df["order_amount"].min(), 2), "to",
      round(q1_df["order_amount"].max(), 2))
print("Std. deviation of order amount: ", round(q1_df["order_amount"].std()))

# Order size metrics
print("\nMean order size: ", round(q1_df["total_items"].mean(), 2))
print("Range of order size: ", round(q1_df["total_items"].min(), 2), "to",
      round(q1_df["total_items"].max(), 2))
print("Std. deviation of order size: ", round(q1_df["total_items"].std()))

# Sneaker price metrics
print("\nMean sneaker price: ", round(q1_df["sneaker_price"].mean(), 2))
print("Range of sneaker price: ", round(q1_df["sneaker_price"].min(), 2), "to",
      round(q1_df["sneaker_price"].max(), 2))
print("Std. deviation of sneaker price: ", round(q1_df["sneaker_price"].std()))

# To graph the frequency of each order size and sneaker price for all orders, uncomment the line
# corresponding to the desired metric:
# q1_df['total_items'].value_counts().sort_index().plot.bar()
# q1_df['sneaker_price'].value_counts().sort_index().plot.bar()
