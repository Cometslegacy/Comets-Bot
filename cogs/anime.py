import discord
from discord.ext import commands
import aiohttp

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="anime")
    async def anime(self, ctx, *, tags=""):
        tags+=" rating:g,s score:>25"
        
        # Format the random endpoint with the given tags
        url = f"https://danbooru.donmai.us/posts/random.json?tags={tags}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    await ctx.send("Error fetching image from Danbooru.")
                    return

                data = await resp.json()
                image_url = data.get("file_url")

                if not image_url:
                    await ctx.send("No image found or file is missing.")
                    return

                embed = discord.Embed(
                        color=discord.Color.green()
                )
                embed.set_image(url=image_url)
                
                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Anime(bot))
