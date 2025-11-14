# E-Commerce Synthetic Data Project

This project demonstrates a simple data engineering workflow using synthetic e-commerce data, SQLite, and basic SQL queries, all developed and executed in Cursor IDE.

## Project Structure

- **CSV files**: Synthetic data for an online store  
  - `Customers.csv`
  - `Products.csv`
  - `Orders.csv`
  - `OrderItems.csv`
  - `Reviews.csv`
- **Ingestion Script**:  
  - `load_ecommerce_to_sqlite.py` — Loads all CSVs into corresponding tables in a SQLite database (`ecom.db`).
- **SQL Query Script**:  
  - `query_order_items.py` — Runs a complex SQL join query and prints (and/or saves) the result.

## Steps to Reproduce

1. **Clone the repository**

   ```bash
   git clone https://github.com/jessjoseph/Diligent.git
   cd Diligent
   ```

2. **[Optional] Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install pandas
   ```

4. **Place CSV files**  
   Ensure your CSV files are named:
   - `Customers.csv`
   - `Products.csv`
   - `Orders.csv`
   - `OrderItems.csv`
   - `Reviews.csv`
   and are located in the root of the project folder.

5. **Ingest data into SQLite**

   ```bash
   python load_ecommerce_to_sqlite.py
   ```
   This will create (or overwrite) `ecom.db` in the project directory.

6. **Run the SQL query and display results**

   ```bash
   python query_order_items.py
   ```
   This will print the output DataFrame to the terminal and, if implemented, save it as `query_results.csv`.

## SQL Join Query Used

The key SQL query performed (see `query_order_items.py`):

```sql
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
JOIN orders AS o ON oi.order_id = o.order_id
JOIN customers AS c ON o.customer_id = c.customer_id
JOIN products AS p ON oi.product_id = p.product_id
ORDER BY o.order_date DESC;
```

## Output

- Prints a table for each order item showing order ID, date, customer name, product, quantity, price per item, total price, and country.

## Notes

- This project was developed and tested in [Cursor IDE](https://cursor.so/).
- You can open and explore the SQLite database (`ecom.db`) in GUI tools like [DB Browser for SQLite](https://sqlitebrowser.org/).
- All code and data is synthetic.

---

**Author:** Jessica Joseph  
**Repository:** [github.com/jessjoseph/Diligent](https://github.com/jessjoseph/Diligent)
