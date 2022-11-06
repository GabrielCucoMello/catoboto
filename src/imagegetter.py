import requests, discord
from discord.ext import commands

class CogImage(commands.Cog, description='Comandos para gerar imagens diversas.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Comando para você pegar imagens aleatórias de gato', description='Comando para você pegar imagens aleatórias de gato')
    async def gato(self, ctx):
        gato = requests.get('https://api.thecatapi.com/v1/images/search', headers={'Accept':'Application/json'}).json()[0]['url']
        await ctx.send(gato)
    
    @commands.command(brief='Comando pra você pegar imagens aleatórias amaldiçoadas.', description='Comando pra você pegar imagens aleatórias amaldiçoadas.')
    async def cursed(self, ctx):
        cursed = requests.get('https://cursedimg.herokuapp.com/api').json()['image']
        await ctx.send(cursed)
    