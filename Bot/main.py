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