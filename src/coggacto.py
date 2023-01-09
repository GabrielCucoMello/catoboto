import random
import requests
import discord
from discord.ext import commands
from deep_translator import GoogleTranslator

class CogGacto(commands.Cog, description='Comandos gerais do bot, aleatórios'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Comando para definir o quão gay você é', description='Comando para definir o quão gay você é')
    async def gay(self, ctx):
        porcentogay = random.randint(0, 100)
        if porcentogay == 69:
            await ctx.reply(f'100%, VOCÊ É O MAIOR GAY DE TODOS {ctx.author.mention}')
        else:
            await ctx.reply(f'Você é {porcentogay}% gay, {ctx.author.mention}')
    @commands.command(brief='Comando pra você gerar piadas muito engraçadas', description='Comando pra você gerar piadas muito engraçadas')
    async def piada(self, ctx):
        piada = requests.get('https://icanhazdadjoke.com', headers={'Accept':'Application/json'}).json()['joke']
        traduzir = GoogleTranslator(source='en', target='pt')
        piada_traduzida = traduzir.translate(piada)
        await ctx.reply(f'{piada_traduzida}')
    
    @commands.command(brief='Comando para você poder jogar jokenpô contra os amigos', description='Comando para você poder jogar jokenpô contra os amigos')
    async def jokenpo(self, ctx):
        escolha = random.randint(0, 2)
        if escolha == 0:
            await ctx.reply(f'Pedra')
        if escolha == 1:
            await ctx.reply(f'Papel')
        if escolha == 2:
            await ctx.reply(f'Tesoura')

    @commands.command(brief='Comando pra você ver o quão calvo você é', description='Comando pra você ver o quão calvo você é')
    async def calvo(self, ctx):
        porcentocalvo = random.randint(0, 100)
        if porcentocalvo == 100:
            await ctx.reply(f'VOCÊ É 100% CALVO, MEUDEUS {ctx.author.mention}')
        else:
            await ctx.reply(f'Você é {porcentocalvo}% calvo, {ctx.author.mention}')

    @commands.command(brief='Comando pra você gerar frases do Kanye West muito engraçadas', description='Comando pra você gerar falas do Kanye West')
    async def kanye(self, ctx):
        fala = requests.get('https://api.kanye.rest', headers={'Accept':'Application/json'}).json()['quote']
        traduzir_fala = GoogleTranslator(source='en', target='pt')
        fala_traduzida = traduzir_fala.translate(fala)
        await ctx.reply(f'{fala_traduzida}')
    
    @commands.command()
    async def avatar(self, ctx, *, member:discord.Member=None):
        if member == None:
            member = ctx.message.author
        avatar = member.avatar
        await ctx.send(avatar)