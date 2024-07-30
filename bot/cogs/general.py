import discord
from discord.ext import commands
from discord import app_commands
from bot.utils.database import get_db_connection

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='testdb', description='Test the database connection.')
    async def test_db(self, interaction: discord.Interaction):
        connection = get_db_connection()
        if connection:
            await interaction.response.send_message("Successfully connected to the database!")
            connection.close()
        else:
            await interaction.response.send_message("Failed to connect to the database.")

    async def cog_load(self):
        self.bot.tree.add_command(self.test_db)

async def setup(bot):
    cog = General(bot)
    await bot.add_cog(cog)
    await cog.cog_load()
