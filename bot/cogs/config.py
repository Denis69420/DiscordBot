from discord.ext import commands
from db import set_guild_config, get_guild_config

class ConfigCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setprefix')
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix: str):
        set_guild_config(ctx.guild.id, prefix)
        await ctx.send(f'Prefix set to: {prefix}')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        set_guild_config(guild.id, '!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        guild_config = get_guild_config(message.guild.id)
        prefix = guild_config['prefix'] if guild_config else '!'

        if message.content.startswith(prefix):
            await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(ConfigCog(bot))
