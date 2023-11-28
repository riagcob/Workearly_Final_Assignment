import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/Ria/Desktop/finance_liquor_sales.csv'
df= pd.read_csv(file_path)
print(df)
print(df.columns)
print(df.dtypes)

# Group by 'zip_code' and 'item_number', calculate the total sales for each combination
grouped_data = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()

# Find the most popular item sold based on zip code
most_popular_item = grouped_data.groupby('zip_code')['bottles_sold'].idxmax()
most_popular_items_df = grouped_data.loc[most_popular_item]

# Calculate the total sales per store
total_sales_per_store = df.groupby('store_name')['bottles_sold'].sum()

# Calculate the percentage of sales per store
percentage_sales_per_store = total_sales_per_store / total_sales_per_store.sum() * 100

# Display the results
print("Most Popular Item Sold Based on Zip Code:")
print(most_popular_items_df)

print("\nPercentage of Sales Per Store:")
print(percentage_sales_per_store)

plt.legend()
for zip_code in grouped_data['zip_code'].unique():
    subset = grouped_data[grouped_data['zip_code'] == zip_code]
    plt.bar(subset['item_description'], subset['bottles_sold'], label=f'Zip Code {zip_code}')

# Adding labels and title
plt.xlabel('Item Description')
plt.ylabel('Total Bottles Sold')
plt.title('Total Bottles Sold by Item Description and Zip Code')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adding legend
plt.legend()

# Show the plot
plt.show()