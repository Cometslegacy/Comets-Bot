from discord.ext import commands
import discord

class Horse(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

                @commands.command()
                async def horse(self, ctx):


        
async def setup(bot):
    await bot.add_cog(Horse(bot))
