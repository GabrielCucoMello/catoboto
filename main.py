import discord, os, asyncio
from discord.ext import commands
from pretty_help import PrettyHelp

from src.coggacto import CogGacto
from src.imagegetter import CogImage

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=PrettyHelp())

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
        await bot.start(os.environ['AUTH_BOT_KEY'])

asyncio.run(main())