from discord.ext import commands
from bot.utils.database import get_db_connection

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("General cog initialized")  # Debug print

    @commands.command(name='testdb')
    async def test_db(self, ctx):
        connection = get_db_connection()
        if connection:
            await ctx.send("Successfully connected to the database!")
            connection.close()
        else:
            await ctx.send("Failed to connect to the database.")

async def setup(bot):
    await bot.add_cog(General(bot))
    print("General cog setup called")  # Debug print
