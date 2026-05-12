# config.gemini/migration_helpers/db_connections.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_engine(db_type='old'):
    """
    Returns a SQLAlchemy engine for the specified database.
    'db_type' can be 'old' or 'new'.
    """
    if db_type == 'old':
        db_host = os.getenv("OLD_DB_HOST")
        db_user = os.getenv("OLD_DB_USER")
        db_password = os.getenv("OLD_DB_PASSWORD")
        db_name = os.getenv("OLD_DB_NAME")
    elif db_type == 'new':
        db_host = os.getenv("NEW_DB_HOST")
        db_user = os.getenv("NEW_DB_USER")
        db_password = os.getenv("NEW_DB_PASSWORD")
        db_name = os.getenv("NEW_DB_NAME")
    else:
        raise ValueError("db_type must be 'old' or 'new'")

    if not all([db_host, db_user, db_password, db_name]):
        raise ValueError(f"Missing environment variables for {db_type} database connection.")

    connection_str = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    return create_engine(connection_str)

if __name__ == '__main__':
    # Example usage and test:
    print("Testing old DB connection...")
    try:
        old_engine = get_db_engine('old')
        with old_engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).scalar()
            print(f"Old DB connected successfully: {result}")
    except Exception as e:
        print(f"Error connecting to old DB: {e}")

    print("
Testing new DB connection...")
    try:
        new_engine = get_db_engine('new')
        with new_engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).scalar()
            print(f"New DB connected successfully: {result}")
    except Exception as e:
        print(f"Error connecting to new DB: {e}")
