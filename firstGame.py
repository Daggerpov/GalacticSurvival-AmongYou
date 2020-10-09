import pygame
pygame.init()

GUI = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

green = (0, 255, 0)
blue = (0, 0, 128)
count = 0
font = pygame.font.Font('freesansbold.ttf', 16)
posText = (0, 0)
running = "True"
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            count+=1
            GUI.fill((0, 0, 0))
            text = font.render('Count = ' + str(count), True, green)
            GUI.blit(text, posText)
            pygame.display.update()
        if event.type == pygame.QUIT:
            running = False

pygame.quit()