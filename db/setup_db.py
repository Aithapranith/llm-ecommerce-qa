import pandas as pd
import sqlite3
import os

# Path to the CSV files
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# Load the CSV files
ad_sales = pd.read_csv(os.path.join(DATA_DIR, 'ad_sales.csv'))
eligibility = pd.read_csv(os.path.join(DATA_DIR, 'eligibility.csv'))
total_sales = pd.read_csv(os.path.join(DATA_DIR, 'total_sales.csv'))

# Create SQLite database
conn = sqlite3.connect('ecommerce.db')

# Save DataFrames as SQL tables
ad_sales.to_sql('ad_sales_metrics', conn, if_exists='replace', index=False)
eligibility.to_sql('eligibility_table', conn, if_exists='replace', index=False)
total_sales.to_sql('total_sales_metrics', conn, if_exists='replace', index=False)

conn.close()
print("✅ ecommerce.db created successfully with 3 tables.")
