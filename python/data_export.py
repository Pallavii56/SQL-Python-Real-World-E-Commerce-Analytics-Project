from sqlalchemy import create_engine
import pandas as pd

# Use your real database
engine = create_engine("mysql+mysqlconnector://root:data2026analytics@localhost/sql_python_analytics")

# Example: get all tables automatically
tables_query = "SHOW TABLES;"
tables = pd.read_sql(tables_query, engine).iloc[:, 0].tolist()

# Export all tables to CSV
dfs = {table: pd.read_sql(f"SELECT * FROM {table}", engine) for table in tables}

for table, df in dfs.items():
    df.to_csv(f"../data/{table}.csv", index=False)
