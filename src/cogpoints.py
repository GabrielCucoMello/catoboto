from discord.ext import commands
import discord
from configuracoes.local_settings import *
import mysql.connector
from datetime import datetime, timedelta
import pandas as pd
import random


class CogPoints(commands.Cog, description='Comandos de pontos para a garagem de carro'):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def daily(self, ctx):
        agora = datetime.now()
        futuro = agora + timedelta(days=1)
        futuro2 = futuro.strftime("%Y-%m-%d %H:%M:%S")
        autor_id = int(ctx.message.author.id)
        autor_nome = str(ctx.message.author)
        autor_guilda = int(ctx.message.guild.id)

        cnx = mysql.connector.connect(
        host = hostip,
        user = usuario,
        password = senha,
        database = databasename
        )

        cur = cnx.cursor(buffered=True)


        cur.execute(f'SELECT user_daily FROM users WHERE user_discord_id = {autor_id}')
        verifica = cur.fetchall()
        if verifica:
            if verifica[0][0] == None:
                cur.execute(f'SELECT user_points FROM users WHERE user_discord_id = {autor_id}')
                variavel = cur.fetchall()
                daily = random.randint(1000, 5000) 
                variavel_2 = variavel[0][0] + daily
                cur.execute(f'UPDATE users SET user_points = %s, user_daily = %s WHERE user_discord_id = %s', (variavel_2, futuro2, autor_id))
                await ctx.send(f'Daily de {daily} pontos resgatado com sucesso!')
                cnx.commit()
                cur.close()
                cnx.close()
                return
            if agora >= verifica[0][0]:
                cur.execute(f'SELECT USER_POINTS FROM users WHERE user_discord_id = {autor_id}')
                variavel = cur.fetchall()
                daily = random.randint(1000, 5000)
                variavel_2 = variavel[0][0] + daily
                cur.execute(f'UPDATE users SET user_points = %s, user_daily = %s WHERE user_discord_id = %s', (variavel_2, futuro2, autor_id))
                cnx.commit()
                cur.close()
                cnx.close()
                await ctx.send(f'Daily de {daily} pontos resgatado com sucesso!')
                return
            else:
                await ctx.send('Daily ainda não está disponível D:')