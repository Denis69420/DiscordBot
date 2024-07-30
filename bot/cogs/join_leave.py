from discord.ext import commands
from db import set_guild_config, get_guild_config

class JoinLeaveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        set_guild_config(guild.id, '!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild_config = get_guild_config(member.guild.id)
        if guild_config and guild_config['join_message']:
            await member.guild.system_channel.send(guild_config['join_message'])

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild_config = get_guild_config(member.guild.id)
        if guild_config and guild_config['leave_message']:
            await member.guild.system_channel.send(guild_config['leave_message'])

def setup(bot):
    bot.add_cog(JoinLeaveCog(bot))
