import discord, os, asyncio
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp

from src.coggacto import CogGacto
from src.imagegetter import CogImage
from src.csgostats import CogValve

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
discord.utils.setup_logging()

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

async def main():
    async with bot:
        await bot.add_cog(CogGacto(bot))
        await bot.add_cog(CogImage(bot))
        await bot.add_cog(CogValve(bot))
        await bot.start(os.environ['AUTH_BOT_KEY'])

asyncio.run(main())