import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

def get_db_connection():
    load_dotenv()
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        if connection.is_connected():
            logger.info("Successfully connected to the database")
            return connection
    except Error as e:
        logger.error(f"Error while connecting to the database: {e}")
    return None
