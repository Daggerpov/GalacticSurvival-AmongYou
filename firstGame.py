import pygame
pygame.init()

GUI = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()