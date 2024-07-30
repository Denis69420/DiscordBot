import os
import mysql.connector
from mysql.connector import Error
import requests
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to the database: {e}")
        return None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


def run_bot():
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Error starting the bot: {e}")

if __name__ == "__main__":
    run_bot()
