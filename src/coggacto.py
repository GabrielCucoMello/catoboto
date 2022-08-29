import discord, random
import requests
from discord.ext import commands
from deep_translator import GoogleTranslator


class CogGacto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gay(self, ctx):
        porcentogay = random.randint(0, 100)
        if porcentogay == 69:
            await ctx.send(f'MAIOR GAY DE TODOS: {porcentogay}% {ctx.author.mention}')
        else:
            await ctx.send(f'Você é {porcentogay}% gay, {ctx.author.mention}')
    @commands.command()
    async def piada(self, ctx):
        piada = requests.get('https://icanhazdadjoke.com', headers={'Accept':'Application/json'}).json()['joke']
        traduzir = GoogleTranslator(source='en', target='pt')
        piada_traduzida = traduzir.translate(piada)
        await ctx.send(f'{piada_traduzida}')