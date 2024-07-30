import discord
from discord.ext import commands
from discord import app_commands
from bot.utils.database import get_db_connection

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree

    @app_commands.command(name='testdb', description='Test the database connection.')
    async def test_db(self, interaction: discord.Interaction):
        connection = get_db_connection()
        if connection:
            await interaction.response.send_message("Successfully connected to the database!")
            connection.close()
        else:
            await interaction.response.send_message("Failed to connect to the database.")

    async def cog_load(self):
        self.tree.add_command(self.test_db)

async def setup(bot):
    await bot.add_cog(General(bot))
