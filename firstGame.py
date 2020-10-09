import pygame
pygame.init()

GUI = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Mumbo Jumbo', True, green)
text.center = (500//2, 500//2)
running = "True"
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            GUI.blit(text, posText)
            pygame.display.update()
        if event.type == pygame.QUIT:
            running = False

pygame.quit()