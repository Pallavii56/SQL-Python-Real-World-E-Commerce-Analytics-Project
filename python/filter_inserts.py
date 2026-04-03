import re

# Tables you WANT
required_tables = [
    "customers",
    "orders",
    "payments",
    "order_items",
    "products"
]

# Read dump file
with open("sql/Dump20260403.sql", "r", encoding="utf-8") as f:
    content = f.read()

# Find all INSERT statements
all_inserts = re.findall(r'INSERT INTO `?(\w+)`?.*?;', content, re.DOTALL)

# Extract only required ones
filtered_inserts = []

for match in re.finditer(r'(INSERT INTO `?(\w+)`?.*?;)', content, re.DOTALL):
    full_query = match.group(1)
    table_name = match.group(2)

    if table_name in required_tables:
        filtered_inserts.append(full_query)

# Save to load_data.sql
with open("sql/load_data.sql", "w", encoding="utf-8") as f:
    f.write("\n\n".join(filtered_inserts))

print("✅ Clean load_data.sql created!")