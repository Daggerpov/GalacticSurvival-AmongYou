import pygame
pygame.init()

GUI = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Galactic Survival: Among You")

green = (0, 255, 0)
count = 0
font = pygame.font.SysFont('arial', 32)
posText = (0, 0)
running = "True"
while running:
    pygame.time.delay(75)
    for event in pygame.event.get():
        #if event.type == pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                count-=1 
            elif event.key == pygame.K_RIGHT:
                count+=1 
        GUI.fill((0, 0, 0))
        text = font.render('Count = ' + str(count), True, green)
        GUI.blit(text, posText)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()