import pygame

pygame.init()

gui = pygame.display.set_mode((1000, 1500)) 
pygame.display.set_caption("Galactic Survival: Among You") #Title of Window

while running:
    pygame.time.delay(75) 
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        
        
        if event.type == pygame.QUIT: #The close window function
            running = False
    pygame.display.update() #Updates the screen
pygame.quit()'''