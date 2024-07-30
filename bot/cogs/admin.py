from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='Kick a member from the server. Usage: /kick @member [reason]')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
