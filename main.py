import discord, os, asyncio
from discord.ext import commands
import logging
# from pretty_help import EmojiMenu, PrettyHelp

from src.coggacto import CogGacto
from src.imagegetter import CogImage
from src.csgostats import CogValve
# from src.slash import CogSlash
# from src.coggarage import CogGarage
# from src.cogpoints import CogPoints
# from src.cogwiki import CogWiki

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# menu = EmojiMenu(page_left='👈', page_right='👉', remove=':nao:1046539066478436462')

bot = commands.Bot(command_prefix='$', intents=intents)
ending_note = 'Comandos do bot {ctx.bot.user.name}\nPara acessar, utilize {help.clean_prefix}{help.invoked_with}'
# bot.help_command = PrettyHelp(menu=menu, color=discord.Color.random(), index_title='Categorias', ending_note=ending_note)

@bot.event
async def on_ready():
    print('Logado como')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')

async def main():
    async with bot:
        await bot.add_cog(CogGacto(bot))
        await bot.add_cog(CogValve(bot))
        await bot.add_cog(CogImage(bot))
        # await bot.add_cog(CogSlash(bot))
        # bot.add_cog(CogGarage(bot))
        # bot.add_cog(CogPoints(bot))
        # bot.add_cog(CogWiki(bot))

        await bot.start(f"{os.environ['AUTH_BOT_KEY']}")

asyncio.run(main())

# bot.add_cog(CogGacto(bot))
# bot.add_cog(CogValve(bot))
# bot.add_cog(CogImage(bot))
# bot.add_cog(CogSlash(bot))
# # bot.add_cog(CogGarage(bot))
# # bot.add_cog(CogPoints(bot))
# # bot.add_cog(CogWiki(bot))

# bot.run(f"{os.environ['AUTH_BOT_KEY']}")