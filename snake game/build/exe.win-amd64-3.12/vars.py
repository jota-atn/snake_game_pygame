import sqlite3
import pygame as pgm
from random import randrange

def reboot():
    global pontos, comprimento, x_cobra, y_cobra, x_apple, y_apple, lista_cobra,  die, musica
    pontos = 0
    comprimento = 3
    x_cobra = largura//2 - 20//2
    y_cobra = altura//2 - 20//2
    x_apple = randrange(10, 1250, 20)
    y_apple = randrange(90, 690, 20)
    lista_cobra = []
    pgm.mixer.music.load(playlist[0])
    pgm.mixer.music.play(-1)

def add_player(nome, record, id):
    cursor.execute("INSERT INTO PLAYERS (Nome, Record, ID) VALUES (?, ?, ?)", (nome, record, id))
    return

def update_player(nome, record, id):
    cursor.execute("UPDATE PLAYERS SET Nome = ?, Record = ? WHERE Nome = ?", (nome, record, nome))
    return

def clear_data_base():
    cursor.execute("DELETE FROM PLAYERS")
    return 

class Retangulo():
    def __init__(self, texto_formatado, y_adicional = 0):
        self.texto_formatado = texto_formatado
        self.largura = 1280
        self.altura = 720
        self.y_adicional = y_adicional

    def getRect(self):
        rect_texto_formatado = self.texto_formatado.get_rect() # type: ignore
        rect_texto_formatado.center = (largura//2, altura//2 + self.y_adicional) # type: ignore
        
        return rect_texto_formatado
    
def desenha_icone_python(mouse_icon):
    if mouse_icon:
        tela.blit(python_icon_hover, (20, 636))
    else:
        tela.blit(python_icon, (20, 636))

def desenha_icone_github(mouse_icon):
    if mouse_icon:
        tela.blit(github_icon_hover, (1190, 636))
    
    else:
        tela.blit(github_icon, (1196, 636))

#BANCO DE DADOS
banco= sqlite3.connect("Banco_de_Dados.db")
cursor= banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS PLAYERS(Nome text, Record integer, ID integer)")

id= 0

#CORES
branca= (255, 255, 255)
preta= (0, 0, 0)
vermelha=(255, 0, 0)
verde= (0, 255, 0)
azul= (0, 0, 255)
cinza= (75, 75, 75)

#INICIANDO
pgm.init()

#VARIÁVEIS
largura= 1280
altura= 720
altura_tri= 365
option = 0
options_clicked = False

x_cobra= largura//2 - 20//2
y_cobra= altura//2 - 20//2

x_apple= randrange(10, 1250, 20)
y_apple= randrange(90, 690, 20)

velocidade= 20
x_controle= velocidade
y_controle= 0

pontos= 0
lista_cobra= []
comprimento= 3
FPS= 15
clock= pgm.time.Clock()
die= False
pause= False
linha= True

#MUSICA
playlist= ["soundtrack\\Mr. Spastic - tEh (r0x!).mp3", "soundtrack\\FNSP.mp3","soundtrack\\GameOverMusic.mp3", "soundtrack\\Gumbel - Levels.mp3", "soundtrack\\Return to Dreamland.mp3"]
volume = 0.5
coin = pgm.mixer.Sound("soundtrack\\smw_coin.wav")
death = pgm.mixer.Sound("soundtrack\\GameOverSound.wav") 

#CONFIGURAÇÕES
dificuldade = 1
idioma = 0
screen_full = False
music_on = True
sound_on = True

#TELA
tela= pgm.display.set_mode((largura, altura), pgm.RESIZABLE)
pgm.display.set_caption("Cobrinha S2")

python_icon = pgm.image.load("images\\Python_Icon.png")
python_icon_hover = pgm.image.load("images\\Python_Icon_Hover.png")

github_icon = pgm.image.load("images\\GitHub_Icon.png")
github_icon_hover = pgm.image.load("images\\GitHub_Icon_Hover.png")

icone_python_rect = python_icon.get_rect()
icone_python_rect.topleft = (20, 636)

icone_github_rect = github_icon.get_rect()
icone_github_rect.topleft = (1196, 636)

mouse_icon_python = False
mouse_icon_github = True

icone = pgm.image.load("images\\cobra_icon.png")

pgm.display.set_icon(icone)

surface= pgm.Surface((largura, altura), pgm.SRCALPHA)

cursor_mao = pgm.cursors.Cursor(pgm.SYSTEM_CURSOR_HAND)
cursor_seta = pgm.cursors.Cursor(pgm.SYSTEM_CURSOR_ARROW)

#WEB

URL_PYTHON = "https://www.python.org"
URL_GITHUB = "https://github.com/jota-atn"