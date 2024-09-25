import pygame as pgm
from pygame.locals import *
from texts import *
from vars import *

conjunto= [K_SPACE, K_LSHIFT, K_RSHIFT, K_LALT, K_RALT, K_LCTRL, K_RCTRL, K_CAPSLOCK, K_TAB, K_ESCAPE, K_BACKQUOTE, K_BACKSLASH, 
           K_F1, K_F2, K_F3, K_F4, K_F5, K_F6, K_F7, K_F8, K_F9, K_F10, K_F11, K_F12, K_PRINTSCREEN, K_SCROLLOCK, K_PAUSE, K_INSERT,
           K_HOME, K_PAGEUP, K_PAGEDOWN, K_END, K_UP, K_LEFT, K_DOWN, K_RIGHT, K_NUMLOCK, K_COMMA, K_PLUS, K_MINUS, K_ASTERISK,
           K_PERIOD, K_KP_DIVIDE, K_KP_MINUS, K_KP_PLUS, K_SEMICOLON, K_COLON, K_LEFTBRACKET, K_RIGHTBRACKET, K_MENU, K_SLASH, K_QUOTE,
           K_QUOTEDBL, K_KP_ENTER, K_RETURN]

x_linha= largura//2
y_linha= altura//2 + 15

linha_controle= 0

pos_linha_inicial= [
    (x_linha - 12, y_linha),
    (x_linha + 12, y_linha),
    (x_linha + 25, y_linha),
    (x_linha + 37, y_linha),
    (x_linha + 50, y_linha),
    (x_linha + 63, y_linha),
    (x_linha + 63, y_linha),
    ]

pos_linha_final= [
    (x_linha + 8, y_linha),
    (x_linha + 32, y_linha),
    (x_linha + 45, y_linha),
    (x_linha + 57, y_linha),
    (x_linha + 70, y_linha),
    (x_linha + 83, y_linha),
    (x_linha + 77, y_linha)
    ]

def saveScore(tela, surface, banco, players, pontos):
    global linha_controle

    nome = ""

    while True:                                                      
        tela.blit(surface, (0, 0))
        surface.fill(preta)
        surface.blit(please_formatado, Retangulo(please_formatado, -250).getRect())                                                  
                                                            
        for event in pgm.event.get():
            if event.type== QUIT:
                banco.close()    
                pgm.quit()
                exit()     
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(nome)== 0:
                        pass
                    else:
                        nome = nome[:-1]
                        linha_controle-=1
                        if linha_controle<0:
                            linha_controle=0  
                elif (event.key== K_KP_ENTER or event.key == K_RETURN) and len(nome)<=6 and len(nome)!=0: 
                    linha_controle= 0
                    
                    cursor.execute("")

                    if any(nome in sublista for sublista in players):
                        update_player(nome, pontos, id)

                    else:
                        add_player(nome, pontos, id)

                    banco.commit() 
                    reboot() 
                    surface.fill(Color(0,0,0,0))

                    return False
                else:
                    if event.key in conjunto:
                        pass    
                    else:
                        if linha_controle>6:
                            linha_controle=5
                        elif len(nome)<6:
                            nome += event.unicode
                            linha_controle+=1                                                               
                                                                
        if linha and linha_controle<6:
            pgm.draw.line(surface, branca, (pos_linha_inicial[linha_controle],), (pos_linha_final[linha_controle]), 5)

        nome_formatado= fonte_30.render(nome, True, branca)
        surface.blit(nome_formatado, Retangulo(nome_formatado).getRect())  
        pgm.display.flip() 