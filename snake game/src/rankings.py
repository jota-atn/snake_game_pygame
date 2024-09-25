from pygame.locals import *
import pygame as pgm
import vars
import texts

def runDeleteDB(tela, banco, players):

    if vars.volume > 0:
        pgm.mixer.music.set_volume(vars.volume - 0.25)

    while True:
        tela.blit(vars.surface, (0, 0))
        pgm.draw.rect(vars.surface, (150, 150, 150, 75), (0, 0, vars.largura, vars.altura))
        vars.surface.blit(texts.delete_db_text_formatado, vars.Retangulo(texts.delete_db_text_formatado).getRect())
        vars.surface.blit(texts.delete_confirmation_formatado, vars.Retangulo(texts.delete_confirmation_formatado, 240).getRect())
        vars.surface.blit(texts.escape_formatado, vars.Retangulo(texts.escape_formatado, 300).getRect())

        for event in pgm.event.get():
            if event.type== QUIT:
                banco.close()    
                pgm.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    vars.clear_data_base()
                    banco.commit()

                    tela.fill(vars.cinza)
                    
                    pgm.draw.rect(tela,(50, 50, 50), (20, 50, 1240, 630))
                    pgm.draw.line(tela, vars.cinza, (vars.largura//2, 50), (vars.largura//2, 680), 10)
                    vars.surface.fill(Color(0,0,0,0))

                    return []

                
                if event.key == K_ESCAPE:
                    vars.surface.fill(Color(0,0,0,0))
                    pgm.mixer.music.set_volume(vars.volume)
                    
                    return players
                
        pgm.display.update()

def runRankings(tela, banco, players): 

    pgm.mixer.music.load(vars.playlist[3])
    pgm.mixer.music.play(-1)

    dicty= {}
    for i in range(len(players)):
        dicty[f"{players[i][0]}"]= players[i][1]
    dicty= dict(sorted(dicty.items(), key= lambda item: item[1],  reverse= True))
    lista= list(dicty.items())

    while True:
        tela.fill(vars.cinza)
        tela.blit(texts.rankings_formatado, (20, 10))
        tela.blit(texts.escape_formatado, vars.Retangulo(texts.escape_formatado, 340).getRect())
        pgm.draw.rect(tela,(50, 50, 50), (20, 50, 1240, 630))
        pgm.draw.line(tela, vars.cinza, (vars.largura//2, 50), (vars.largura//2, 680), 10)

        altura_numero= 70
        for i in range(len(players)):
            if i<=8:
                numero= f"0{i+1}- {lista[i][0]}"
                pontos_aux= f"{lista[i][1]}"
                numero_formatado= texts.fonte_25.render(numero, True, vars.preta)
                pontos_formatado= texts.fonte_25.render(pontos_aux, True, vars.preta)                                 
                tela.blit(numero_formatado, (60, altura_numero))
                tela.blit(pontos_formatado, (300, altura_numero))
            elif i>8 and i<10:
                numero= f"{i+1}- {lista[i][0]}"
                pontos_aux= f"{lista[i][1]}"
                numero_formatado= vars.fonte_25.render(numero, True, vars.preta)
                pontos_formatado= vars.fonte_25.render(pontos_aux, True, vars.preta)                                 
                tela.blit(numero_formatado, (60, altura_numero))
                tela.blit(pontos_formatado, (300, altura_numero))
            elif i==10:
                altura_numero= 70
                numero= f"{i+1}- {lista[i][0]}"
                pontos_aux= f"{lista[i][1]}"
                numero_formatado= vars.fonte_25.render(numero, True, vars.preta)
                pontos_formatado= vars.fonte_25.render(pontos_aux, True, vars.preta)                                 
                tela.blit(numero_formatado, ((vars.largura//2)+50, altura_numero))
                tela.blit(pontos_formatado, ((vars.largura//2)+290, altura_numero))                       
            elif i>10 and i<20:
                numero= f"{i+1}- {lista[i][0]}"
                pontos_aux= f"{lista[i][1]}"
                numero_formatado= vars.fonte_25.render(numero, True, vars.preta)
                pontos_formatado= vars.fonte_25.render(pontos_aux, True, vars.preta)                                 
                tela.blit(numero_formatado, ((vars.largura//2)+50, altura_numero))
                tela.blit(pontos_formatado, ((vars.largura//2)+290, altura_numero))

            altura_numero+= 61
            
        for event in pgm.event.get():
            if event.type== QUIT:
                banco.close()    
                pgm.quit()
                exit()
            if event.type== KEYDOWN:
                if event.key== K_ESCAPE:

                    pgm.mixer.music.load(vars.playlist[0])
                    pgm.mixer.music.play(-1)

                    return 
                
                if event.key == K_r:
                    players = runDeleteDB(tela, banco, players)
                    
                    
        pgm.display.flip()
