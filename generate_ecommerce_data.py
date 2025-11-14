import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

output_dir = Path(".")
output_dir.mkdir(parents=True, exist_ok=True)

first_names = [
    "Olivia",
    "Liam",
    "Emma",
    "Noah",
    "Ava",
    "Elijah",
    "Sophia",
    "Mateo",
    "Isabella",
    "Lucas",
    "Mia",
    "Ethan",
    "Amelia",
    "Logan",
    "Harper",
    "James",
    "Luna",
    "Aiden",
    "Evelyn",
    "Sebastian",
]
last_names = [
    "Smith",
    "Johnson",
    "Brown",
    "Taylor",
    "Lee",
    "Martinez",
    "Garcia",
    "Wilson",
    "Anderson",
    "Thomas",
    "Moore",
    "Martin",
    "Jackson",
    "Thompson",
    "White",
    "Harris",
    "Sanchez",
    "Clark",
    "Lewis",
    "Young",
]
countries = [
    "United States",
    "Canada",
    "United Kingdom",
    "Germany",
    "France",
    "Australia",
    "Spain",
    "Italy",
    "Netherlands",
    "Brazil",
]

product_categories = {
    "Electronics": [
        "Noise-Canceling Headphones",
        "Smartphone Stand",
        "Wireless Charger",
        "Bluetooth Speaker",
        "USB-C Hub",
        "4K Streaming Stick",
        "Smart Home Hub",
        "Portable SSD Drive",
        "Mechanical Keyboard",
        "Wi-Fi 6 Router",
    ],
    "Home & Kitchen": [
        "Ceramic Coffee Mug Set",
        "Bamboo Cutting Board",
        "Aroma Diffuser",
        "Stainless Steel Kettle",
        "Memory Foam Pillow",
        "Cast Iron Skillet",
        "Glass Meal Prep Containers",
        "Electric Hand Mixer",
        "Herb Garden Kit",
        "Air Purifier Filter",
    ],
    "Fitness": [
        "Non-Slip Yoga Mat",
        "Adjustable Dumbbells",
        "Resistance Band Kit",
        "Foam Roller",
        "Fitness Tracker Strap",
        "Jump Rope Set",
        "Kettlebell Pair",
        "Balance Trainer",
        "Exercise Dice Game",
        "Hydration Backpack",
    ],
    "Beauty": [
        "Vitamin C Serum",
        "Moisturizing Face Cream",
        "Organic Shampoo",
        "Aloe Vera Gel",
        "Lip Care Kit",
        "Detox Clay Mask",
        "Overnight Repair Oil",
        "Charcoal Tooth Powder",
        "Reusable Makeup Pads",
        "Spa Headband Trio",
    ],
    "Outdoors": [
        "Insulated Water Bottle",
        "Camping Lantern",
        "Portable Hammock",
        "Compact Binoculars",
        "Trail Backpack",
        "Solar Power Bank",
        "Multi-tool Knife",
        "Trail Running Poles",
        "Foldable Camp Table",
        "Waterproof Dry Bag",
    ],
    "Books": [
        "Leadership Workbook",
        "Healthy Recipes Guide",
        "Mindfulness Journal",
        "Photography Basics",
        "Travel Bucket List",
        "Creative Writing Prompts",
        "30-Day Budget Planner",
        "Startup Playbook",
        "Minimalist Living Guide",
        "DIY Home Repair Manual",
    ],
}

review_phrases = [
    "Exceeded expectations and arrived quickly.",
    "Quality is solid for the price.",
    "Packaging could be better but works great.",
    "Would definitely recommend to friends.",
    "Satisfied overall, plan to buy again.",
    "Color was slightly different than pictured.",
    "Great value and easy to use.",
    "Customer support was very helpful.",
    "Instructions were unclear but figured it out.",
    "Sturdy build and looks premium.",
]


def random_date(start_years_ago: int = 3) -> datetime.date:
    end = datetime.now()
    start = end - timedelta(days=365 * start_years_ago)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).date()


NUM_CUSTOMERS = 85
NUM_ORDERS = 70
NUM_REVIEWS = 65

customers = []
for cid in range(1, NUM_CUSTOMERS + 1):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first.lower()}.{last.lower()}{cid}@example.com"
    signup = random_date()
    country = random.choice(countries)
    customers.append(
        {
            "customer_id": cid,
            "first_name": first,
            "last_name": last,
            "email": email,
            "signup_date": signup.isoformat(),
            "country": country,
        }
    )

products = []
product_prices = {}
pid = 1
for category, names in product_categories.items():
    for name in names:
        price = round(random.uniform(12.5, 249.99), 2)
        stock = random.randint(20, 500)
        products.append(
            {
                "product_id": pid,
                "product_name": name,
                "category": category,
                "price": price,
                "stock_quantity": stock,
            }
        )
        product_prices[pid] = price
        pid += 1

orders = []
order_items = []
order_totals = {}
order_item_id = 1
order_id = 1
for _ in range(NUM_ORDERS):
    customer = random.choice(customers)
    order_date = random_date()
    orders.append(
        {
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "order_date": order_date.isoformat(),
            "total_amount": 0,
        }
    )
    line_count = random.choice([1, 1, 1, 2])
    chosen_products = random.sample(products, k=line_count)
    total = 0
    for product in chosen_products:
        quantity = random.randint(1, 4)
        price_per_item = round(product["price"] * random.uniform(0.9, 1.05), 2)
        total += quantity * price_per_item
        order_items.append(
            {
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": product["product_id"],
                "quantity": quantity,
                "price_per_item": price_per_item,
            }
        )
        order_item_id += 1
    order_totals[order_id] = round(total, 2)
    order_id += 1

for order in orders:
    order["total_amount"] = order_totals[order["order_id"]]

reviews = []
review_id = 1
for _ in range(NUM_REVIEWS):
    product = random.choice(products)
    customer = random.choice(customers)
    review_date = random_date()
    reviews.append(
        {
            "review_id": review_id,
            "product_id": product["product_id"],
            "customer_id": customer["customer_id"],
            "rating": random.randint(3, 5),
            "review_date": review_date.isoformat(),
            "review_text": random.choice(review_phrases),
        }
    )
    review_id += 1

schemas = [
    (
        "Customers.csv",
        ["customer_id", "first_name", "last_name", "email", "signup_date", "country"],
        customers,
    ),
    (
        "Products.csv",
        ["product_id", "product_name", "category", "price", "stock_quantity"],
        products,
    ),
    (
        "Orders.csv",
        ["order_id", "customer_id", "order_date", "total_amount"],
        orders,
    ),
    (
        "OrderItems.csv",
        ["order_item_id", "order_id", "product_id", "quantity", "price_per_item"],
        order_items,
    ),
    (
        "Reviews.csv",
        ["review_id", "product_id", "customer_id", "rating", "review_date", "review_text"],
        reviews,
    ),
]

for filename, headers, rows in schemas:
    with (output_dir / filename).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

print("Generated files:")
for filename, _, _ in schemas:
    path = output_dir / filename
    with path.open(encoding="utf-8") as f:
        row_count = sum(1 for _ in f) - 1
    print(f"{filename}: {row_count} rows")

