import pygame as pgm
from pygame.locals import *
import vars
from texts import *
from die import gameOver
from time import sleep
from pause import pauseGame
from random import randrange

def create_cobra(tela, lista_cobra):
    for pos in lista_cobra:
        pgm.draw.rect(tela, (110, 0, 150), (pos[0], pos[1], 20, 20))

def runGame(tela, banco):
    global pontos, x_cobra, y_cobra, x_controle, y_controle, x_apple, y_apple, comprimento

    vars.cursor.execute("SELECT * FROM PLAYERS")
    players = vars.cursor.fetchall()
    
    pgm.mixer.music.load(vars.playlist[1])
    pgm.mixer.music.play(-1)   

    pgm.mouse.set_cursor(vars.cursor_seta)         

    run_game = True
    last_direction_change = pgm.time.get_ticks()  # Tempo da última mudança de direção
    cooldown = 0.1  # Tempo em milissegundos para cooldown

    while run_game:
        tela.fill((180, 180, 180))
        vars.clock.tick(vars.FPS)

        pontuacao = f"{pontuacao_text[vars.idioma]} = {vars.pontos}"
        pontuacao_formatada = fonte_50.render(pontuacao, True, vars.branca)

        # BORDAS
        pgm.draw.rect(tela, vars.preta, (0, 0, 1280, 90))
        pgm.draw.rect(tela, vars.preta, (0, 0, 10, 720))
        pgm.draw.rect(tela, vars.preta, (0, 710, 1280, 10))
        pgm.draw.rect(tela, vars.preta, (1270, 0, 10, 720))

        # TEXTOS
        tela.blit(pontuacao_formatada, (12, 10))

        vars.x_cobra += vars.x_controle
        vars.y_cobra += vars.y_controle

        cobra = pgm.draw.rect(tela, (110, 0, 150), (vars.x_cobra, vars.y_cobra, 20, 20))
        apple = pgm.draw.rect(tela, (255, 0, 0), (vars.x_apple, vars.y_apple, 20, 20))

        # COLISÕES
        if vars.x_cobra > 1250:
            vars.x_cobra = 10
        if vars.x_cobra < 10:
            vars.x_cobra = 1250
        if vars.y_cobra < 90:
            vars.y_cobra = 690
        if vars.y_cobra > 690:
            vars.y_cobra = 90
        if cobra.colliderect(apple):
            if vars.sound_on:
                vars.coin.play()
            vars.x_apple = randrange(10, 1250, 20)
            vars.y_apple = randrange(90, 690, 20)
            apple = pgm.draw.rect(tela, (255, 0, 0), (vars.x_apple, vars.y_apple, 20, 20))
            vars.pontos += 1
            vars.comprimento += 1

        lista_head = [vars.x_cobra, vars.y_cobra]
        vars.lista_cobra.append(lista_head)

        if len(vars.lista_cobra) > vars.comprimento:
            del vars.lista_cobra[0]

        create_cobra(tela, vars.lista_cobra)

        # COMANDOS
        for event in pgm.event.get():
            if event.type == QUIT:
                banco.close()
                pgm.quit()
                exit()
            if event.type == KEYDOWN:
                current_time = pgm.time.get_ticks()  # Tempo atual

                if current_time - last_direction_change > cooldown:  # Verifica cooldown
                    if event.key == K_w or event.key == K_UP:
                        if vars.y_controle != vars.velocidade:
                            vars.y_controle = -vars.velocidade
                            vars.x_controle = 0
                            last_direction_change = current_time  # Atualiza o tempo da última mudança
                    if event.key == K_a or event.key == K_LEFT:
                        if vars.x_controle != vars.velocidade:
                            vars.x_controle = -vars.velocidade
                            vars.y_controle = 0
                            last_direction_change = current_time
                    if event.key == K_s or event.key == K_DOWN:
                        if vars.y_controle != -vars.velocidade:
                            vars.y_controle = vars.velocidade
                            vars.x_controle = 0
                            last_direction_change = current_time
                    if event.key == K_d or event.key == K_RIGHT:
                        if vars.x_controle != -vars.velocidade:
                            vars.x_controle = vars.velocidade
                            vars.y_controle = 0
                            last_direction_change = current_time

                # PAUSE
                if event.key == K_p or event.key == K_PAUSE:
                    if vars.volume > 0:
                        pgm.mixer.music.set_volume(vars.volume - 0.25)
                    run_game = pauseGame()

                # SUICÍDIO
                elif event.key == K_BACKSPACE:
                    pgm.mixer.music.stop()

                    if vars.sound_on:
                        vars.death.play()
                        sleep(4)

                    pgm.mixer.music.load(vars.playlist[2])
                    pgm.mixer.music.play(-1)

                    run_game = gameOver(tela, banco, vars.surface, vars.pontos, players, vars.playlist)

        # GAME OVER
        if vars.lista_cobra.count(lista_head) > 1:
            pgm.mixer.music.stop()

            if vars.sound_on:
                vars.death.play()
                sleep(4)

            pgm.mixer.music.load(vars.playlist[2])
            pgm.mixer.music.play(-1)

            run_game = gameOver(tela, banco, vars.surface, vars.pontos, players, vars.playlist)

        pgm.display.flip()
