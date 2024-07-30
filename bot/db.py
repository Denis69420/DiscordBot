import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def create_table_if_not_exists():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guild_config (
            guild_id BIGINT PRIMARY KEY,
            prefix VARCHAR(10) DEFAULT '!',
            join_message TEXT DEFAULT NULL,
            leave_message TEXT DEFAULT NULL,
            bot_message TEXT DEFAULT NULL
        );
    """)
    db.commit()
    cursor.close()
    db.close()

def get_guild_config(guild_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM guild_config WHERE guild_id = %s", (guild_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def set_guild_config(guild_id, prefix, join_message=None, leave_message=None, bot_message=None):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("""
        REPLACE INTO guild_config (guild_id, prefix, join_message, leave_message, bot_message)
        VALUES (%s, %s, %s, %s, %s)
    """, (guild_id, prefix, join_message, leave_message, bot_message))
    db.commit()
    cursor.close()
    db.close()

def update_guild_message(guild_id, message_type, message):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(f"UPDATE guild_config SET {message_type} = %s WHERE guild_id = %s", (message, guild_id))
    db.commit()
    cursor.close()
    db.close()
