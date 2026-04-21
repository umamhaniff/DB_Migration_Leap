import os
from dotenv import load_dotenv

load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'database_old': os.getenv('DB_OLD'),
        'database_new': os.getenv('DB_NEW')
    }