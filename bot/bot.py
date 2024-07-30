import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents for bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Bot setup
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for guild in bot.guilds:
        print(f'Connected to {guild.name} (id: {guild.id})')

# Load cogs
bot.load_extension('cogs.config')

# Run the bot
bot.run(TOKEN)
