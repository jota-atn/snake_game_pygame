import pygame

# Inicializa o Pygame
pygame.init()

# Resolução base
base_width, base_height = 800, 600

# Cria a janela

python_icon = pygame.image.load("Python_Icon.png")

screen = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)
pygame.display.set_caption("Proporcionalidade no Pygame")

# Posição original do objeto (proporcional ao tamanho base)
original_x, original_y = 400, 300  # Centro da tela na resolução base

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtém as dimensões atuais da tela
    current_width, current_height = screen.get_size()

    # Calcula as proporções
    x_ratio = current_width / base_width
    y_ratio = current_height / base_height

    # Ajusta a posição do objeto de acordo com as proporções
    adjusted_x = int(original_x * x_ratio)
    adjusted_y = int(original_y * y_ratio)

    # Preenche a tela com uma cor de fundo
    screen.fill((255, 255, 255))

    # Blita a imagem na posição ajustada
    screen.blit(python_icon, (adjusted_x, adjusted_y))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()