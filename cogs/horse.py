from discord.ext import commands
import discord

class Horse(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.command(name = "horse")
        async def horse(self, ctx):
                image = discord.File("resources\horse.png", filename="horse.png")
                await ctx.send(file=image)
        
async def setup(bot):
    await bot.add_cog(Horse(bot))
