import pygame
import sys
import random

from startMenu import start
from endMenu import end
from setup import select
from instructions import instruct

pygame.init()

#Resolution dimensions
resx = 1366
resy = 768

gui = pygame.display.set_mode((resx, resy)) 
width = gui.get_width()
height = gui.get_height()

pygame.display.set_caption("Galactic Survival: Among You") #Title of Window
running = True


titleFont = pygame.font.Font(r'./in-your-face-joffrey/In your face, joffrey!.ttf', 100)
buttonFont = pygame.font.Font(r'./in-your-face-joffrey/In your face, joffrey!.ttf', 32)
taskFont = pygame.font.Font(r'./in-your-face-joffrey/In your face, joffrey!.ttf', 50)
instructFont = pygame.font.Font(r'./negara-serif/NegaraSerif-HairlineItalic.otf', 32)

def posText(text, x, y):
    titleRect = text.get_rect()
    titleRect.center = (x, y)
    return titleRect

green = (0, 255, 0)

stars = []

screen = 0

short_tasks = 1
long_tasks = 0

increase_task_sound = pygame.mixer.Sound("./audio/zapsplat_multimedia_game_sound_digital_short_generic_could_be_collect_item_001_56968.wav")
decrease_task_sound = pygame.mixer.Sound("./audio/zapsplat_multimedia_game_tone_marimba_high_pitched_generic_tone_003_56830.wav")
error_task_sound = pygame.mixer.Sound("./audio/Computer Error Alert-SoundBible.com-783113881.wav")

for i in range(60):
    starx = random.randrange(0, resx)
    stary = random.randrange(0, resy)
    stars.append([starx, stary])

def spacebg():
    from main import resx, resy, running, gui, pygame, stars, starx , stary
    import random

    for i in range(len(stars)):
        # Draw the star
        pygame.draw.circle(gui, (255, 255, 255), stars[i], 2)
        # Move the star right one pixel
        stars[i][0] += 1
        # If the star has moved off the bottom of the screen
        if stars[i][0] > resx:
            # Reset it just above the top
            starx = random.randrange(-50, -10)
            stars[i][0] = starx
            # Give it a new y position
            stary = random.randrange(0, resy)
            stars[i][1] = stary

while running:
    pygame.time.delay(50) 

    mouse = pygame.mouse.get_pos()

    if screen == 0:
        start()

    elif screen == 1:
        select()
    
    elif screen == 2:
        instruct()

    else:
        end()
    
    pygame.display.update() #Updates the screen


pygame.quit()
quit() 