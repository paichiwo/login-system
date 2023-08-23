from src.helpers import create_database
from src.config import sql_file_path, db_file_path
import os

if not os.path.exists(db_file_path) and os.path.exists(sql_file_path):
    create_database('db/db.db', 'db/db.sql')
    print("New database successfully created")
else:
    print("Database already exists")

