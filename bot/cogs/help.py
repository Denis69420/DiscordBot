import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='help', description='Display the help message.')
    async def help_command(self, interaction: discord.Interaction):
        help_text = """
        **Available Commands:**
        `/help` - Display this help message
        `/testdb` - Test the database connection
        `/kick` - Kick a member (Admin only)
        """
        await interaction.response.send_message(help_text)

    async def cog_load(self):
        self.bot.tree.add_command(self.help_command)

async def setup(bot):
    cog = Help(bot)
    await bot.add_cog(cog)
    await cog.cog_load()
