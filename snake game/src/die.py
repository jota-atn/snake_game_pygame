from vars import *
from save import saveScore
from texts import *
from pygame.locals import *

def gameOver(tela, banco, surface, pontos, players, playlist):
    
    pontuacao= f"{pontuacao_text[idioma]} = {pontos}"
    pontuacao_morte_formatado= fonte_30.render(pontuacao, True, branca)
    
    while True:
        tela.fill((255, 0, 0))
        tela.blit(surface, (0, 0))
        pgm.draw.rect(surface, (100, 0, 0, 30), (0, 0, largura, altura))

        #TEXTOS MORTE
        surface.blit(game_over_formatado, Retangulo(game_over_formatado, -250).getRect())                                    
        surface.blit(pontuacao_morte_formatado, Retangulo(pontuacao_morte_formatado, -150).getRect())
        surface.blit(escape_formatado_morte, Retangulo(escape_formatado_morte, 320).getRect())
        surface.blit(enter_formatado, Retangulo(enter_formatado, 75).getRect())

        for event in pgm.event.get():
            if event.type == QUIT:  
                banco.close()    
                pgm.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_r:
                    pgm.mixer.music.stop()
                    surface.fill(branca)
                    reboot()
                    pgm.mixer.music.load(playlist[1])
                    pgm.mixer.music.play(-1)
                    
                if event.key== K_ESCAPE:
                    pgm.mixer.music.stop()
                    surface.fill(Color(0,0,0,0))
                    reboot()
                    
                    return False
                
                if event.key== K_KP_ENTER or event.key== K_SPACE or event.key == K_RETURN:                                               
                    pgm.mixer.music.stop()
                    return saveScore(tela, surface, banco, players, pontos)
                                 
        pgm.display.update()