import os
import logging
import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        logger.info(f'Logged in as {self.user}')

    def load_cogs(self):
        for filename in os.listdir("./bot/cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                try:
                    self.load_extension(f"bot.cogs.{filename[:-3]}")
                    logger.info(f"Loaded cog: {filename[:-3]}")
                except Exception as e:
                    logger.error(f"Failed to load cog {filename}: {e}")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = MyBot(command_prefix='/', intents=intents)
bot.load_cogs()
