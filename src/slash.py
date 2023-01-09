import random
import requests
import discord
from discord.ext import commands
from deep_translator import GoogleTranslator
from discord.utils import get

class CogSlash(commands.Cog, description='Comandos de barra para o bot.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(brief='Comando para definir o quão gay você é', description='Comando para definir o quão gay você é', guild_ids=[982783169206054994])
    async def gay(self, ctx):
        porcentogay = random.randint(0, 100)
        if porcentogay == 69:
            await ctx.respond(f'100%, VOCÊ É O MAIOR GAY DE TODOS {ctx.author.mention}')
        else:
            await ctx.respond(f'Você é {porcentogay}% gay, {ctx.author.mention}')