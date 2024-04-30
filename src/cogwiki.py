# from discord.ext import commands
# import discord
# from configuracoes.local_settings import *
# import mysql.connector
# import pandas as pd
# import asyncio


# class CogWiki(commands.Cog, description='Comandos de wikipedia de carro'):
#     def __init__(self, bot):
#         self.bot = bot
    
#     @commands.command()
#     async def wikicar(self, ctx, car):
#         cur = cnx.cursor(buffered=True)

#         cur.execute(f"SELECT * FROM cars WHERE model LIKE '{car}' OR trim LIKE '{car}'")
#         carros = cur.fetchall()

#         paginas = len(carros)
#         pagina_atual = 1

#         embed=discord.Embed(title=f"Resultados que retornaram do carro pesquisado: **{len(carros)}**", 
#         description=f"Aqui você poderá ver os dados do carro que voc6e pesquisou, modelo por modelo",
#         color=discord.Color.random())
#         embed.add_field(name="Opção:", value=f"Aperte '▶️' para ir para a próxima página e começar a navegar", inline=False)
#         embed.add_field(name="Opção:", value=f"Aperte '◀️' para voltar para as páginas anteriores", inline=False)
#         embed.add_field(name="Terminar interação", value=f"Caso você não clicar em nada, em 20 segundos o comando será encerrado.", inline=False)

#         menssagem = await ctx.send(embed=embed)

#         await menssagem.add_reaction("◀️")
#         await menssagem.add_reaction("▶️")

#         def check(reaction, user):
#             return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        
#         while True:
#             embed1=discord.Embed(title=f"Dados do carro pesquisado", 
#             description=f"Página {pagina_atual} de {len(carros)}",
#             color=discord.Color.random())
#             embed1.add_field(name="Marca:", value=f"{carros[pagina_atual - 1][1]}", inline=True)
#             embed1.add_field(name="Local de fabricação:", value=f":flag_{carros[pagina_atual - 1][26].lower()}: {carros[pagina_atual - 1][2]}", inline=True)
#             embed1.add_field(name="Modelo:", value=f"{carros[pagina_atual - 1][3]}", inline=True)
#             embed1.add_field(name="Versão:", value=f"{carros[pagina_atual - 1][4]}", inline=True)
#             embed1.add_field(name="Ano:", value=f"{carros[pagina_atual - 1][5]}", inline=True)
#             embed1.add_field(name="Posição do motor:", value=f"{carros[pagina_atual - 1][7]}", inline=True)
#             embed1.add_field(name="Litragem do motor:", value=f"{int(carros[pagina_atual - 1][8])/1000}", inline=True)
#             try:
#                 reaction, user = await self.bot.wait_for('reaction_add', timeout=20, check=check)
            
#                 if str(reaction.emoji) == '▶️' and pagina_atual != paginas:
#                     pagina_atual += 1
#                     await menssagem.edit(embed=embed1)
#                     await menssagem.remove_reaction(reaction, user)
#                 elif str(reaction.emoji) == '◀️' and pagina_atual >= 0:
#                     pagina_atual -= 1
#                     await menssagem.edit(embed=embed1)
#                     await menssagem.remove_reaction(reaction, user)
#                 else:
#                     embed2=discord.Embed(title=f"Resultados que retornaram do carro pesquisado: **{len(carros)}**", 
#                     description=f"Aqui você poderá ver os dados do carro que você pesquisou, modelo por modelo",
#                     color=discord.Color.random())
#                     embed2.add_field(name="Opção:", value=f"Aperte ▶️ para ir para a próxima página e começar a navegar", inline=False)
#                     embed2.add_field(name="Opção:", value=f"Aperte ◀️ para voltar para as páginas anteriores", inline=False)
#                     embed2.add_field(name="Terminar interação", value=f"Caso você não clicar em nada, em 20 segundos (ou menos) o comando será encerrado.", inline=False)
#                     await menssagem.edit(embed=embed2)
#                     await menssagem.remove_reaction(reaction, user)
#             except asyncio.TimeoutError:
#                 await menssagem.delete()
#                 break