import os
from dotenv import load_dotenv, dotenv_values
import sqlalchemy as sa

load_dotenv()

print(os.getenv("DATABASE_URL"))

engine = sa.create_engine(os.getenv("DATABASE_URL"))

try:
    connection = engine.connect()
    print("Database connection successful!")

except Exception as excep:
    print(f"Connection failed: {excep}")

metadata = sa.MetaData()



