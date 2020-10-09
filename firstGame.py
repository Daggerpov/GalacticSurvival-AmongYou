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
    pygame.time.delay(1000)
    for event in pygame.event.get():
        count+=1
        GUI.fill((0, 0, 0))
        text = font.render('Count = ' + str(count), True, green)
        GUI.blit(text, posText)
        #if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()