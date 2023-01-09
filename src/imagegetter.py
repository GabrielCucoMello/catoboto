import requests, discord
from discord.ext import commands
from deep_translator import GoogleTranslator
from serpapi import GoogleSearch

class CogImage(commands.Cog, description='Comandos para gerar imagens diversas.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Comando para você pegar imagens aleatórias de gato', description='Comando para você pegar imagens aleatórias de gato')
    async def gato(self, ctx):
        gato = requests.get('https://api.thecatapi.com/v1/images/search', headers={'Accept':'Application/json'}).json()[0]['url']
        await ctx.reply(gato)
    
    @commands.command(brief='Comando pra você pegar imagens aleatórias amaldiçoadas.', description='Comando pra você pegar imagens aleatórias amaldiçoadas.')
    async def cursed(self, ctx):
        cursed = requests.get('https://cursedimg.herokuapp.com/api').json()['image']
        await ctx.reply(cursed)
    
    @commands.command(brief='Comando pra você pegar imagens aleatórias amaldiçoadas.', description='Comando pra você pegar imagens aleatórias amaldiçoadas.')
    async def raposa(self, ctx):
        raposa = requests.get('https://randomfox.ca/floof/').json()['image']
        await ctx.reply(raposa)
    
    @commands.command(brief='Comando pra você pegar imagens aleatórias amaldiçoadas.', description='Comando pra você pegar imagens aleatórias amaldiçoadas.')
    async def cachorro(self, ctx):
        cachorro = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']
        await ctx.reply(cachorro)
    
    @commands.command(brief='Comando pra você pegar frases de anime foda', description='Comando pra você pegar frase de animes fodas')
    async def animefrase(self, ctx):
        animequote = requests.get('https://animechan.vercel.app/api/random').json()
        personagem = animequote['character']
        anime = animequote['anime']
        # if  ' 'in anime:
        #     anime = anime.replace(' ','+')
        if ' ' in personagem:
            personagem = personagem.replace(' ','+')
        personagem = personagem+f'+{anime}'
        # params = {
        # "device": "desktop",
        # "engine": "google",
        # "ijn": "0",
        # "q": {personagem},
        # "google_domain": "google.com",
        # "tbm": "isch",
        # "api_key": "a51d6b9021fb05eedebf8a2ab8411581d4bccf11d17d07026b358c1821547dd1"
        # }
        # search = GoogleSearch(params)
        # results = search.get_dict()
        frase = animequote['quote']
        traduzir_frase = GoogleTranslator(source='en', target='pt')
        frase_traduzida = traduzir_frase.translate(frase)
        embed=discord.Embed(title=f"Frase de anime foda",
        color=discord.Color.random())
        # embed.set_thumbnail(url=results['images_results'][0]['original'])
        embed.add_field(name='Anime', value=animequote['anime'], inline=False)
        embed.add_field(name='Personagem', value=animequote['character'], inline=False)
        embed.add_field(name='Frase', value=frase_traduzida, inline=False)
        await ctx.reply(embed=embed)