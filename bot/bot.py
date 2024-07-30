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

    def load_cog(self, cog_name):
        try:
            self.load_extension(f"bot.cogs.{cog_name}")
            logger.info(f"Loaded cog: {cog_name}")
        except Exception as e:
            logger.error(f"Failed to load cog {cog_name}: {e}")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = MyBot(command_prefix='/', intents=intents)
