import sqlite3
from pathlib import Path

# Connect to the database
db_path = Path(__file__).parent / "ecom.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL query
query = """
SELECT
    oi.order_id,
    o.order_date,
    c.first_name || ' ' || c.last_name AS customer_name,
    p.product_name,
    oi.quantity,
    oi.price_per_item,
    (oi.quantity * oi.price_per_item) AS line_total,
    c.country AS customer_country
FROM order_items AS oi
JOIN orders AS o
    ON oi.order_id = o.order_id
JOIN customers AS c
    ON o.customer_id = c.customer_id
JOIN products AS p
    ON oi.product_id = p.product_id
ORDER BY o.order_date DESC;
"""

# Execute query and fetch results
cursor.execute(query)
results = cursor.fetchall()

# Get column names
column_names = [description[0] for description in cursor.description]

# Print header
print("=" * 120)
print("Order Items with Customer and Product Details")
print("=" * 120)
print()

# Print column headers
header = " | ".join(f"{col:20}" for col in column_names)
print(header)
print("-" * 120)

# Print rows
for row in results:
    formatted_row = " | ".join(f"{str(val):20}" for val in row)
    print(formatted_row)

print()
print(f"Total rows: {len(results)}")

# Close connection
conn.close()

