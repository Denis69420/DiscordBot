from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Help cog initialized")  # Debug print

    @commands.command(name='help')
    async def help_command(self, ctx):
        help_text = """
        **Available Commands:**
        `/help` - Display this help message
        `/testdb` - Test the database connection
        """
        await ctx.send(help_text)

async def setup(bot):
    await bot.add_cog(Help(bot))
    print("Help cog setup called")  # Debug print
