import pygame as pgm
from pygame.locals import *
from sys import exit
from random import randrange
import webbrowser
import texts
from vars import *
from run import runGame
from settings import openSettings
from rankings import runRankings

run = True

pgm.mixer.music.set_volume(volume)                
pgm.mixer.music.load(playlist[0])
pgm.mixer.music.play(-1)

while run:
    #TELA INICIAL
    tela.fill(branca)
    tela.fill(cinza)
    
    #OPTIONS
    tela.blit(texts.titulo_formatado, Retangulo(texts.titulo_formatado, -200).getRect())
    tela.blit(texts.subtitulo_formatado, Retangulo(texts.subtitulo_formatado, -140).getRect())
    tela.blit(texts.autor_formatado, Retangulo(texts.autor_formatado, 340).getRect())
    tela.blit(texts.iniciar_formatado, Retangulo(texts.autor_formatado).getRect())
    tela.blit(texts.rankings_formatado, Retangulo(texts.autor_formatado, 40).getRect())
    tela.blit(texts.sair_formatado, Retangulo(texts.autor_formatado, 120).getRect())
    tela.blit(texts.configs_formatado, Retangulo(texts.autor_formatado, 80).getRect())
    desenha_icone_python(mouse_icon_python)
    desenha_icone_github(mouse_icon_github)

    if options_clicked:
        if option >= 5:
            option = 1

        if option <= 0:
            option = 4

    match option:
        case 1:
            pgm.draw.polygon(tela, preta, ((480, altura_tri-10), (480, altura_tri+10), (500, altura_tri)))
        case 2:
            pgm.draw.polygon(tela, preta, ((480, altura_tri+30), (480, altura_tri+50), (500, altura_tri+40)))
        case 3:
           pgm.draw.polygon(tela, preta, ((480, altura_tri+70), (480, altura_tri+90), (500, altura_tri+80)))
        case 4:
            pgm.draw.polygon(tela, preta, ((480, altura_tri+110), (480, altura_tri+130), (500, altura_tri+120)))

    for event in pgm.event.get():
        if event.type== pgm.QUIT:
            banco.close()    
            pgm.quit()
            exit()

        if event.type == pgm.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos_mouse = event.pos
                if icone_python_rect.collidepoint(pos_mouse):
                    webbrowser.open(URL_PYTHON)

                if icone_github_rect.collidepoint(pos_mouse):
                    webbrowser.open(URL_GITHUB)

                if Retangulo(texts.iniciar_formatado).getRect().collidepoint(pos_mouse):
                    runGame(tela, banco)

                if Retangulo(texts.rankings_formatado, 40).getRect().collidepoint(pos_mouse):
                    cursor.execute("SELECT * FROM PLAYERS")
                    players = cursor.fetchall()

                    if players == []:
                        id= 1  
                    else:
                        id = players[len(players)-1][2] + 1
        
                    runRankings(tela, banco, players)

                if Retangulo(texts.configs_formatado, 80).getRect().collidepoint(pos_mouse):
                    openSettings(tela, banco, playlist)

                if Retangulo(texts.sair_formatado, 120).getRect().collidepoint(pos_mouse):
                    banco.close()
                    pgm.quit()
                    exit()
                    
        if event.type == pgm.MOUSEMOTION:
            pos_mouse = event.pos
            if icone_python_rect.collidepoint(pos_mouse):
                mouse_icon_python = True
                pgm.mouse.set_cursor(cursor_mao)

            elif icone_github_rect.collidepoint(pos_mouse):
                mouse_icon_github = True
                pgm.mouse.set_cursor(cursor_mao)

            elif Retangulo(texts.iniciar_formatado).getRect().collidepoint(pos_mouse):
                pgm.mouse.set_cursor(cursor_mao)
            
            elif Retangulo(texts.rankings_formatado, 40).getRect().collidepoint(pos_mouse):
                pgm.mouse.set_cursor(cursor_mao)

            elif Retangulo(texts.configs_formatado, 80).getRect().collidepoint(pos_mouse):
                pgm.mouse.set_cursor(cursor_mao)

            elif Retangulo(texts.sair_formatado, 120).getRect().collidepoint(pos_mouse):
                pgm.mouse.set_cursor(cursor_mao)

            else:
                mouse_icon_python = False
                mouse_icon_github = False
                pgm.mouse.set_cursor(cursor_seta)
            

        if event.type== pgm.KEYDOWN:
            if event.key == pgm.K_DOWN or event.key == pgm.K_s:
                option += 1
                if not options_clicked:
                    options_clicked = True

            if event.key == pgm.K_UP or event.key == pgm.K_w:
                option -= 1
                if not options_clicked:
                    options_clicked = True
                
            #GAME RUN    
            if option==1 and (event.key == pgm.K_SPACE or event.key == pgm.K_KP_ENTER or event.key == pgm.K_RETURN):
                #MUSICA
                runGame(tela, banco)
            
            #RANKINGS
            if option == 2 and (event.key == pgm.K_SPACE or event.key == pgm.K_KP_ENTER or event.key == pgm.K_RETURN):
                cursor.execute("SELECT * FROM PLAYERS")
                players = cursor.fetchall()

                if players == []:
                    id= 1  
                else:
                    id = players[len(players)-1][2] + 1
    
                runRankings(tela, banco, players)

            #SAIR
            if option == 4 and (event.key == pgm.K_SPACE or event.key == pgm.K_KP_ENTER or event.key == pgm.K_RETURN):
                banco.close()    
                pgm.quit()
                exit()
        
            #CONFIGURAÇÕES
            if option == 3 and (event.key == pgm.K_SPACE or event.key == pgm.K_KP_ENTER or event.key == pgm.K_RETURN):
                openSettings(tela, banco, playlist)

    #UPDATE    
    pgm.display.flip()
banco.close()        
