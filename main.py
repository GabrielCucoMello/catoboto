import discord, os, asyncio
from discord.ext import commands
import logging
from pretty_help import DefaultMenu, PrettyHelp

from src.coggacto import CogGacto
from src.imagegetter import CogImage
from src.csgostats import CogValve
from src.slash import CogSlash

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

menu = DefaultMenu(page_left='👈', page_right='👉', remove=':reverse:685626195005800449')

bot = commands.Bot(command_prefix='$', intents=intents)
ending_note = 'Comandos do bot {ctx.bot.user.name}\nPara acessar, utilize {help.clean_prefix}{help.invoked_with}'
bot.help_command = PrettyHelp(menu=menu, color=discord.Color.random(), index_title='Categorias', ending_note=ending_note)

@bot.event
async def on_ready():
    print('Logado como')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')

bot.add_cog(CogGacto(bot))
bot.add_cog(CogValve(bot))
bot.add_cog(CogImage(bot))
bot.add_cog(CogSlash(bot))

bot.run(f"{os.environ['AUTH_BOT_KEY']}")