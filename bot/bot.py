import os
import logging
import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def setup_hook(self):
        # This is a new method recommended by discord.py for async setup
        await self.load_extension('bot.cogs.general')
        await self.load_extension('bot.cogs.admin')
        await self.load_extension('bot.cogs.help')

    async def on_ready(self):
        logger.info(f'Logged in as {self.user}')
        print(f'Logged in as {self.user}')  # Print statement for debugging

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = MyBot(command_prefix='/', intents=intents)
