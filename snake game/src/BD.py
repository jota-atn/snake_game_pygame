import sqlite3

def add_player(nome, pontuacao, id):
    cursor.execute("INSERT INTO PLAYERS VALUES(?,?,?)", (nome, pontuacao, id,))
    return

banco= sqlite3.connect("Banco_de_Dados.db")
cursor= banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS PLAYERS(NOME TEXT, RECORD INTEGER, ID INTEGER)")

nome= "CAIO"
pontos= 8
id= 3

# add_player(nome, pontos, id)
cursor.execute("SELECT * FROM PLAYERS")
players= cursor.fetchall()
# print(players)

if players== []:
    id=1
    # print(id)
else:
    id= players[len(players)-1][2]
    # print(id)

cursor.execute("SELECT * FROM PLAYERS")
comparison= cursor.fetchall()


dicty= {}

print(comparison)
for i in range(len(comparison)):
    dicty[f"{comparison[i][0]}"]= comparison[i][1]
    print(dicty)


dicty= dict(sorted(dicty.items(), key= lambda item: item[1], reverse= True))
print(dicty)
# for chave in dicty:
#     id= chave
#     # print(chave, ordem[id])
#     # print(id)
# # for i in range(len(dicty)):
lista= list(dicty.items())
for i in range(len(dicty)):
    numero= lista[i][1]
    print(numero)

ordem= list(dicty.items())
print(ordem[0])




banco.commit()
banco.close()