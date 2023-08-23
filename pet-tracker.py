import os
from src.helpers import create_database
from src.config import SQL_FILEPATH, DB_FILEPATH


if not os.path.exists(DB_FILEPATH) and os.path.exists(SQL_FILEPATH):
    create_database(DB_FILEPATH, SQL_FILEPATH)
    print("New database successfully created")
else:
    print("Database exists")

