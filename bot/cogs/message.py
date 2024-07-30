from discord.ext import commands
from db import get_guild_config

class MessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        guild_config = get_guild_config(message.guild.id)
        prefix = guild_config['prefix'] if guild_config else '!'

        if message.content.startswith(prefix):
            await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(MessageCog(bot))
