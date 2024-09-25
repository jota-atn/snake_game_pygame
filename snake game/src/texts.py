import pygame as pgm

def reboot_texts(idioma):
    global game_over_formatado, pause_formatado, pause_formatado2
    global titulo_formatado, subtitulo_formatado, autor_formatado 
    global iniciar_formatado, rankings_formatado, sair_formatado, configs_formatado 
    global escape_formatado, escape_formatado_morte, escape_formatado_pause, full_formatado 
    global yes_formatado, no_formatado, music_text_formatado, sound_text_formatado, enter_formatado, please_formatado
    global idioma_disponiveis_text_formatado, idioma_text_formatado
    global facil_formatado, normal_formatado, dificil_formatado, avancado_formatado

    game_over_formatado= fonte_100.render(game_over[idioma], True, branca)
    pause_formatado= fonte_30.render(pause_text[idioma], True, (100, 100, 100))
    pause_formatado2= fonte_30.render(pause_text2[idioma], True, (100, 100, 100))
    titulo_formatado= fonte_100.render(titulo, True, preta)
    subtitulo_formatado= fonte_40.render(subtitulo, True, preta)
    autor_formatado= fonte_20.render(autor[idioma], True, preta)
    iniciar_formatado= fonte_30.render(iniciar[idioma], True, preta)
    rankings_formatado= fonte_30.render(rankings[idioma], True, preta)
    sair_formatado= fonte_30.render(sair[idioma], True, preta)
    configs_formatado= fonte_30.render(configs[idioma], True, preta)
    escape_formatado= fonte_20.render(escape[idioma], True, preta)
    escape_formatado_morte= fonte_20.render(escape[idioma], True, branca)
    escape_formatado_pause= fonte_20.render(escape[idioma], True, (100, 100, 100))
    full_formatado= fonte_30.render(full[idioma], True, preta)
    yes_formatado= fonte_30.render(yes[idioma], True, preta)
    no_formatado= fonte_30.render(no[idioma], True, preta)
    music_text_formatado = fonte_30.render(music_text[idioma], True, preta)
    sound_text_formatado = fonte_30.render(sound_text[idioma], True, preta)
    enter_formatado= fonte_30.render(enter[idioma], True, branca)
    please_formatado= fonte_50.render(please[idioma], True, branca)
    idioma_text_formatado = fonte_30.render(idioma_text[idioma], True, preta)
    idioma_disponiveis_text_formatado = fonte_30.render(idioma_disponiveis_text[idioma], True, preta)
    facil_formatado = fonte_30.render(facil_text[idioma], True, preta)
    normal_formatado = fonte_30.render(normal_text[idioma], True, preta)
    dificil_formatado = fonte_30.render(dificil_text[idioma], True, preta)
    avancado_formatado = fonte_30.render(avancado_text[idioma], True, preta)

pgm.init()

#MENSAGENS

    #CORES
branca= (255, 255, 255)
preta= (0, 0, 0)

    #IDIOMA
idioma = 0

    #FONTES
fonte_20= pgm.font.Font('fonts\\widepixel.ttf', 20)
fonte_25= pgm.font.Font("fonts\\widepixel.ttf", 25)
fonte_30= pgm.font.Font("fonts\\widepixel.ttf", 30)
fonte_40= pgm.font.Font("fonts\\widepixel.ttf", 40)
fonte_50= pgm.font.Font("fonts\\widepixel.ttf", 50)
fonte_100= pgm.font.Font("fonts\\widepixel.ttf", 100)
input_box= pgm.Rect(200, 200, 140, 32)

    #VARIÁVEIS TEXTO
titulo= 'Snake Game'
subtitulo= '(Pygame)'
autor= ['por Jota', "by Jota", "por Jota"]
iniciar = ["Iniciar", "Start", "Iniciar"]
rankings = ["Rankings", "Rankings", "Clasificaciones"]
sair = ["Sair", "Quit", "Salir"]
configs = ["Configurações", "Configurations", "Configuraciones"]
game_over = ["GAME OVER", "GAME OVER", "GAME OVER"]
pause_text = ["JOGO PAUSADO!", "PAUSE", "¡JUEGO EN PAUSA!"]
pause_text2 = ["Aperte P para voltar", "Press P to get back to the game", "Presiona P para volver"]
escape = ["Pressione ESC para sair", "Press ESC to get back to quit", "Presiona ESC para salir"]
full = ["Fullscreen:", "Fullscreen:", "Fullscreen:"]
yes = ["Sim", "Yes", "Sí"]
no = ["Não", "No", "No"]
music_text = ["Música:", "Music:", "Música:"]
sound_text = ["Som:", "Sound:", "Sonido:"]
enter = ["ENTER para salvar seu recorde!", "ENTER to save your points!", "¡ENTER para guardar tus puntos!"]
please = ["COLOQUE SEU NOME:", "INSERT YOUR NAME:", "INTRODUCE TU NOMBRE:"]
idioma_text = ["Idioma:", "Language:", "Idioma:"]
idioma_disponiveis_text = ["Português", "English", "Español"]
pontuacao_text = ["Pontuação", "Pontuation", "Pontuacion"]
delete_db_text = ["Resetar placar?", "Reset score?", "Restablecer puntuación"]
delete_confirmation_text = ["ENTER para confirmar", "ENTER to confirm", "Enter para confirmar"]
dificuldade_text = ["Dificuldade:", "Difficulty:", "Dificuldad:"]
facil_text = ["Fácil", "Easy", "Fácil"]
normal_text = ["Normal", "Normal", "Normal"]
dificil_text = ["Difícil", "Hard", "Difícil"]
avancado_text = ["Avançado", "Advanced", "Avanzado"]

    #FORMATAÇÕES
game_over_formatado= fonte_100.render(game_over[idioma], True, branca)
pause_formatado= fonte_30.render(pause_text[idioma], True, (100, 100, 100))
pause_formatado2= fonte_30.render(pause_text2[idioma], True, (100, 100, 100))
titulo_formatado= fonte_100.render(titulo, True, preta)
subtitulo_formatado= fonte_40.render(subtitulo, True, preta)
autor_formatado= fonte_20.render(autor[idioma], True, preta)
iniciar_formatado= fonte_30.render(iniciar[idioma], True, preta)
rankings_formatado= fonte_30.render(rankings[idioma], True, preta)
sair_formatado= fonte_30.render(sair[idioma], True, preta)
configs_formatado= fonte_30.render(configs[idioma], True, preta)
escape_formatado= fonte_20.render(escape[idioma], True, preta)
escape_formatado_morte= fonte_20.render(escape[idioma], True, branca)
escape_formatado_pause= fonte_20.render(escape[idioma], True, (100, 100, 100))
full_formatado= fonte_30.render(full[idioma], True, preta)
yes_formatado= fonte_30.render(yes[idioma], True, preta)
no_formatado= fonte_30.render(no[idioma], True, preta)
music_text_formatado = fonte_30.render(music_text[idioma], True, preta)
sound_text_formatado = fonte_30.render(sound_text[idioma], True, preta)
enter_formatado= fonte_30.render(enter[idioma], True, branca)
please_formatado= fonte_50.render(please[idioma], True, branca)
idioma_text_formatado = fonte_30.render(idioma_text[idioma], True, preta)
idioma_disponiveis_text_formatado = fonte_30.render(idioma_disponiveis_text[idioma], True, preta)
delete_db_text_formatado = fonte_50.render(delete_db_text[idioma], True, preta)
delete_confirmation_formatado = fonte_20.render(delete_confirmation_text[idioma], True, preta)
dificuldade_formatado = fonte_30.render(dificuldade_text[idioma], True, preta)
facil_formatado = fonte_30.render(facil_text[idioma], True, preta)
normal_formatado = fonte_30.render(normal_text[idioma], True, preta)
dificil_formatado = fonte_30.render(dificil_text[idioma], True, preta)
avancado_formatado = fonte_30.render(avancado_text[idioma], True, preta)
