import discord, random, requests
from discord.ext import commands

class CogImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gato(self, ctx):
        gato = requests.get('https://api.thecatapi.com/v1/images/search', headers={'Accept':'Application/json'}).json()[0]['url']
        await ctx.send(gato)