# from discord.ext import commands
# import discord
# from configuracoes.local_settings import *
# import mysql.connector
# import pandas as pd


# class CogGarage(commands.Cog, description='Comandos de garagem de carro'):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command()
#     async def garagem(self, ctx, tipo=None, *, nome=None):
#         autor_id = int(ctx.message.author.id)
#         autor_nome = str(ctx.message.author)
#         autor_guilda = int(ctx.message.guild.id)

#         cnx = mysql.connector.connect(
#         host = hostip,
#         user = usuario,
#         password = senha,
#         database = databasename
#         )

#         cur = cnx.cursor(buffered=True)

#         if tipo == None:
#             cur.execute(f'SELECT * FROM USERS WHERE USER_DISCORD_ID = {autor_id};')
#             stats = cur.fetchall()
#             if len(stats) == 0:
#                 await ctx.send('Você não tem uma garagem.')
#                 return
#             else:
#                 pass
#             embed=discord.Embed(title=f"Garagem do usuário: **{autor_nome}**", 
#             color=discord.Color.random())
#             embed.add_field(name="Nome:", value=f"{stats[0][5]}", inline=True)
#             embed.add_field(name="Pontos:", value=f"{stats[0][2]}", inline=True)
#             await ctx.send(embed=embed)
#             return
#         cur.execute(f'SELECT * FROM USERS WHERE USER_DISCORD_ID = {autor_id};')
#         veref = cur.fetchall()
#         print(veref)
#         if veref:
#             if autor_guilda == veref[0][4]:
#                     await ctx.send('Garagem já criada caralho!')
#                     return
#             else:
#                 pass
#         if tipo == 'criar':
#             cur.execute('INSERT INTO USERS (user_discord_id, user_name, user_guild_id, garage_name, user_points) VALUES (%s, %s, %s, %s, %s)', [autor_id, autor_nome, autor_guilda, nome, 0])
#             cnx.commit()
#             cnx.close()
#             print('Enviado')
#             await ctx.send('completo?')