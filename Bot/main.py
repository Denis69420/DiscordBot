import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up discord intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Database connection function
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

# Event when the bot is ready
@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user}')

# Example command to test database connection
@bot.command(name='testdb')
async def test_db(ctx):
    connection = get_db_connection()
    if connection:
        await ctx.send("Successfully connected to the database!")
        connection.close()
    else:
        await ctx.send("Failed to connect to the database.")

# Function to run the bot
def run_bot():
    try:
        bot.run(TOKEN)
    except Exception as e:
        logger.error(f"Error starting the bot: {e}")

if __name__ == "__main__":
    run_bot()
