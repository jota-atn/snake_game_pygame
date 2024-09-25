import pygame as pgm
from pygame import *
import vars
from texts import *


def pauseGame():
    while True:                   
        vars.tela.blit(vars.surface, (0, 0))
        pgm.draw.rect(vars.surface, (150, 150, 150, 15), (0, 0, vars.largura, vars.altura))
        vars.surface.blit(pause_formatado, vars.Retangulo(pause_formatado).getRect())
        vars.surface.blit(pause_formatado2, vars.Retangulo(pause_formatado2, 100).getRect())
        vars.surface.blit(escape_formatado_pause, vars.Retangulo(escape_formatado_pause, 320).getRect())
                        
        for event in pgm.event.get():
            if event.type== QUIT:
                vars.banco.close()    
                pgm.quit()
                exit()
            if event.type== KEYDOWN:
                if event.key== K_p or event.key== K_PAUSE:
                    pgm.mixer.music.set_volume(vars.volume)
                    return True

                if event.key== K_ESCAPE:                                            
                    vars.surface.fill(Color(0,0,0,0))

                    if vars.music_on:
                        vars.volume = 0.5
                        pgm.mixer_music.set_volume(vars.volume)

                    pgm.mixer.music.stop()
                    vars.reboot()
                    return False
        pgm.display.update()