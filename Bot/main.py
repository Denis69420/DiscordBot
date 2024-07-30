import os
import mysql.connector
from mysql.connector import Error
import logging
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.voice_states = True

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
            logger.info("Successfully connected to the database")
            return connection
    except Error as e:
        logger.error(f"Error while connecting to the database: {e}")
        return None

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user}')



def run_bot():
    try:
        bot.run(TOKEN)
    except Exception as e:
        logger.error(f"Error starting the bot: {e}")

if __name__ == "__main__":
    run_bot()
