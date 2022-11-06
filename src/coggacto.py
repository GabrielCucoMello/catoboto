import discord, random
import requests
from discord.ext import commands
from deep_translator import GoogleTranslator

class CogGacto(commands.Cog, description='Comandos gerais do bot, aleatórios'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Comando para definir o quão gay você é', description='Comando para definir o quão gay você é')
    async def gay(self, ctx):
        porcentogay = random.randint(0, 100)
        if porcentogay == 69:
            await ctx.send(f'100%, VOCÊ É O MAIOR GAY DE TODOS {ctx.author.mention}')
        else:
            await ctx.send(f'Você é {porcentogay}% gay, {ctx.author.mention}')
    @commands.command(brief='Comando pra você gerar piadas muito engraçadas', description='Comando pra você gerar piadas muito engraçadas')
    async def piada(self, ctx):
        piada = requests.get('https://icanhazdadjoke.com', headers={'Accept':'Application/json'}).json()['joke']
        traduzir = GoogleTranslator(source='en', target='pt')
        piada_traduzida = traduzir.translate(piada)
        await ctx.send(f'{piada_traduzida}')
    
    @commands.command(brief='Comando para você poder jogar jokenpô contra os amigos', description='Comando para você poder jogar jokenpô contra os amigos')
    async def jokenpo(self, ctx):
        escolha = random.randint(0, 2)
        if escolha == 0:
            await ctx.send(f'Pedra')
        if escolha == 1:
            await ctx.send(f'Papel')
        if escolha == 2:
            await ctx.send(f'Tesoura')

    @commands.command(brief='Comando pra você ver o quão calvo você é', description='Comando pra você ver o quão calvo você é')
    async def calvo(self, ctx):
        porcentocalvo = random.randint(0, 100)
        if porcentocalvo == 100:
            await ctx.send(f'VOCÊ É 100% CALVO, MEUDEUS {ctx.author.mention}')
        else:
            await ctx.send(f'Você é {porcentocalvo}% calvo, {ctx.author.mention}')