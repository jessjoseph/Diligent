import sqlite3
from pathlib import Path

import pandas as pd


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    db_path = base_dir / "ecom.db"

    csv_to_table = {
        "Customers.csv": "customers",
        "Products.csv": "products",
        "Orders.csv": "orders",
        "OrderItems.csv": "order_items",
        "Reviews.csv": "reviews",
    }

    with sqlite3.connect(db_path) as conn:
        for csv_name, table_name in csv_to_table.items():
            csv_path = base_dir / csv_name
            if not csv_path.exists():
                raise FileNotFoundError(f"Missing CSV file: {csv_path}")

            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Loaded {len(df)} rows into table '{table_name}'.")

    print(f"SQLite database created at: {db_path}")


if __name__ == "__main__":
    main()

