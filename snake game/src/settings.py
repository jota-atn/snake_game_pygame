import vars
import texts
from pygame.locals import *
import pygame as pgm

def openSettings(tela, banco, playlist):

    vars.config_choice = 0

    pgm.mouse.set_cursor(vars.cursor_seta)

    pgm.mixer.music.load(playlist[4])
    pgm.mixer.music.play(-1)

    while True:
        tela.fill(vars.cinza)
        tela.blit(texts.configs_formatado, (20, 10))
        tela.blit(texts.escape_formatado, vars.Retangulo(texts.escape_formatado, 340).getRect())
        pgm.draw.rect(tela, (50, 50, 50), (20, 50, 1240, 630))
        tela.blit(texts.full_formatado, (80, 70))
        tela.blit(texts.music_text_formatado, (80, 120))
        tela.blit(texts.sound_text_formatado, (80, 170))
        tela.blit(texts.idioma_text_formatado, (80, 220))
        tela.blit(texts.dificuldade_formatado, (80, 270))
        
        if vars.screen_full:
            tela.blit(texts.yes_formatado, (400, 70))
        else:
            tela.blit(texts.no_formatado, (400, 70))

        if vars.music_on:
            tela.blit(texts.yes_formatado, (400, 120))
        else:
            tela.blit(texts.no_formatado, (400, 120))

        if vars.sound_on:
            tela.blit(texts.yes_formatado, (400, 170))
        else:
            tela.blit(texts.no_formatado, (400, 170))
        
        tela.blit(texts.idioma_disponiveis_text_formatado, (400, 220))

        match vars.dificuldade:
            case 0:
                vars.FPS = 5
                tela.blit(texts.facil_formatado, (400, 270))
            case 1:
                vars.FPS = 15
                tela.blit(texts.normal_formatado, (400, 270))
            case 2: 
                vars.FPS = 30
                tela.blit(texts.dificil_formatado, (400, 270))
            case 3:
                vars.FPS = 45
                tela.blit(texts.avancado_formatado, (400, 270))

        if vars.config_choice > 6:
            vars.config_choice = 1
        elif vars.config_choice < 0:
            vars.config_choice = 6

        match vars.config_choice:
            case 1:
                pgm.draw.polygon(tela, vars.branca, ((35, 75), (35, 95), (60, 85)))
            case 2:
                pgm.draw.polygon(tela, vars.branca, ((35, 125), (35, 145), (60, 135)))
            case 3:
                pgm.draw.polygon(tela, vars.branca, ((35, 175), (35, 195), (60, 185)))
            case 4:
                pgm.draw.polygon(tela, vars.branca, ((35, 225), (35, 245), (60, 235)))
            case 5:
                pgm.draw.polygon(tela, vars.branca, ((35, 275), (35, 295), (60, 285)))
            case 6:
                pgm.draw.polygon(tela, vars.branca, ((35, 325), (35, 345), (60, 335)))

        for event in pgm.event.get():
            if event.type == QUIT:
                banco.close()    
                pgm.quit()
                exit()
            if event.type == KEYDOWN:
                match vars.config_choice:
                    case 1: 
                        if not vars.screen_full and (event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN):
                            pgm.display.set_mode((vars.largura, vars.altura), pgm.FULLSCREEN)
                            vars.screen_full = True
                        elif vars.screen_full and (event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN):
                            pgm.display.set_mode((vars.largura, vars.altura))
                            vars.screen_full = False

                    case 2:
                        if not vars.music_on and (event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN):
                            vars.volume = 0.5
                            pgm.mixer.music.set_volume(vars.volume)
                            vars.music_on = True

                        elif vars.music_on and (event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN):
                            vars.volume = 0
                            pgm.mixer.music.set_volume(vars.volume)
                            vars.music_on = False
                        
                    case 3:
                        if not vars.sound_on and (event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN):
                            vars.sound_on = True
                        
                        elif vars.sound_on and (event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN):
                            vars.sound_on = False

                    case 4:
                        if event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN:
                            texts.idioma += 1

                        if texts.idioma > 2:
                            texts.idioma = 0         
                            
                        texts.reboot_texts(texts.idioma)
                    
                    case 5:
                        if event.key == K_SPACE or event.key == K_KP_ENTER or event.key == K_RETURN:
                            vars.dificuldade += 1
                            if vars.dificuldade > 3:
                                vars.dificuldade = 0

                if event.key == K_ESCAPE:
                    pgm.mixer.music.load(playlist[0])
                    pgm.mixer.music.play(-1)
                    return
                if event.key == K_s or event.key == K_DOWN:
                    vars.config_choice += 1
                if event.key == K_w or event.key == K_UP:
                    vars.config_choice -= 1

        pgm.display.flip()
