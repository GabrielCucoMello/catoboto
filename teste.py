from configuracoes.local_settings import *
import mysql.connector

cnx = mysql.connector.connect(
host = hostip,
user = usuario,
password = senha,
database = databasename
)

cur = cnx.cursor(buffered=True)

cur.execute('SELECT * FROM states')
estados = cur.fetchall()

cur.execute('SELECT * FROM cars')
carros = cur.fetchall()

loop = 0
loop2 = 0
while loop != len(carros):
  if carros[loop][2] in estados[loop2][1]:
    cur.execute(f"UPDATE cars SET alpha2 = '{estados[loop2][2]}' where id = {carros[loop][0]}")
    cnx.commit()
    print('pais encontrado')
    loop += 1
    loop2 = 0
  if carros[loop][2] not in estados[loop2][1]:
    loop2 += 1
    print(loop2)
    print('pais nao encontrado, repetindo')
cnx.close()