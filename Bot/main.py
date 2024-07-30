import os
import mysql.connector
import requests
from dotenv import load_dotenv
from discord.ext import commands, tasks


load_dotenv()
TOKEN = os.getenv(DISCORD_TOKEN)


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.voice_states = True


bot = commands.Bot(command_prefix='/', intents=intents)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME')
    )


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


def run_bot():
    bot.run(TOKEN)