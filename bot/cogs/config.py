from discord.ext import commands
from db import set_guild_config, update_guild_message

class ConfigCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setprefix')
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix: str):
        set_guild_config(ctx.guild.id, prefix)
        await ctx.send(f'Prefix set to: {prefix}')

    @commands.command(name='setjoinmessage')
    @commands.has_permissions(administrator=True)
    async def setjoinmessage(self, ctx, *, message: str):
        update_guild_message(ctx.guild.id, 'join_message', message)
        await ctx.send('Join message set.')

    @commands.command(name='setleavemessage')
    @commands.has_permissions(administrator=True)
    async def setleavemessage(self, ctx, *, message: str):
        update_guild_message(ctx.guild.id, 'leave_message', message)
        await ctx.send('Leave message set.')

    @commands.command(name='setbotmessage')
    @commands.has_permissions(administrator=True)
    async def setbotmessage(self, ctx, *, message: str):
        update_guild_message(ctx.guild.id, 'bot_message', message)
        await ctx.send('Bot message set.')

def setup(bot):
    bot.add_cog(ConfigCog(bot))
