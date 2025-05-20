import psycopg2
from config.app_config import get_config

def db_connection():
    """
    Create and return a PostgreSQL database connection
    """
    HOST = get_config().DB_HOST
    USER = get_config().DB_USER
    PASS = get_config().DB_PASSWORD
    DATABASE = get_config().DB_NAME
    
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASS,
        dbname=DATABASE
    )
    
    return connection 