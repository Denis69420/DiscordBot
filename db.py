import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

def get_guild_config(guild_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM guild_config WHERE guild_id = %s", (guild_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def set_guild_config(guild_id, prefix):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("REPLACE INTO guild_config (guild_id, prefix) VALUES (%s, %s)", (guild_id, prefix))
    db.commit()
    cursor.close()
    db.close()
