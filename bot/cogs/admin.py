import discord
from discord.ext import commands
from discord import app_commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='kick', description='Kick a member from the server. Usage: /kick @member [reason]')
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member} has been kicked.")

    async def cog_load(self):
        self.bot.tree.add_command(self.kick)

async def setup(bot):
    await bot.add_cog(Admin(bot))
