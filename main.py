import pygame
import sys
import random

from startMenu import start
from endMenu import end
from setup import select
from instructions import instruct

from chart_course_exp import chart_course_exp
from simon_says_exp import simon_says_exp

from chart_course import chart_course
from simon_says import simon_says
from retry_calculator import retry_calculator

pygame.init()

#Sounds/Audio 
increase_task_sound = pygame.mixer.Sound("./audio/zapsplat_multimedia_game_sound_digital_short_generic_could_be_collect_item_001_56968.wav")
decrease_task_sound = pygame.mixer.Sound("./audio/zapsplat_multimedia_game_tone_marimba_high_pitched_generic_tone_003_56830.wav")
error_task_sound = pygame.mixer.Sound("./audio/Computer Error Alert-SoundBible.com-783113881.wav")

#Generating pattern for Simon Says 
pink = (255,192,203)
red = (255, 0, 0)
yellow = (255, 255, 0)   
silver = (192, 192, 192)
green = (0, 255, 0)
blue = (0, 0, 255)

colour_names = {(255, 192, 203):'pink', (255, 255, 0):'yellow', (0, 0, 255):'blue', (0, 255, 0):'green', (255, 0, 0):'red'}

#Resolution dimensions
resx = 1366
resy = 768

#Initializing window
gui = pygame.display.set_mode((resx, resy)) 
width = gui.get_width()
height = gui.get_height()

#Title of Window
pygame.display.set_caption("Galactic Survival: Among You") 
running = True

#Fonts
titleFont = pygame.font.Font(r'./fonts/In your face, joffrey!.ttf', 100)
buttonFont = pygame.font.Font(r'./fonts/In your face, joffrey!.ttf', 32)
taskFont = pygame.font.Font(r'./fonts/In your face, joffrey!.ttf', 50)
instructFont = pygame.font.Font(r'./fonts/NegaraSerif-HairlineItalic.otf', 32)

#Used to center text
def posText(text, x, y):
    titleRect = text.get_rect()
    titleRect.center = (x, y)
    return titleRect

stars = []

#Input for username
username = ''
userRectx = width//2-125
userRecty = height//4-20

#Used to determine what screen the user is supposed to be on
screen = 0

short_tasks = 1
long_tasks = 0

difficulty = ('easy', 'normal', 'hard', 'extreme')
index = 1
fails = 0

lose = False
game_end = False

#Sets up positions for stars
for i in range(60):
    starx = random.randrange(0, resx)
    stary = random.randrange(0, resy)
    stars.append([starx, stary])

#Draws a space background
def spacebg():
    from main import resx, resy, running, gui, pygame, stars, starx , stary
    import random

    for i in range(len(stars)):
        pygame.draw.circle(gui, (255, 255, 255), stars[i], 2)
        stars[i][0] += 1
        if stars[i][0] > resx:
            starx = random.randrange(-50, -10)
            stars[i][0] = starx
            stary = random.randrange(0, resy)
            stars[i][1] = stary

#Main game loop to create the entire game
while running:
    pygame.time.delay(10) 

    mouse = pygame.mouse.get_pos()

    retries = retry_calculator(index, fails)

    if screen == 0:
        start()
        fails = 0
        which_message = random.randint(0, 4)

    elif screen == 1:
        select()
    
    elif screen == 2:
        instruct()

    elif screen == 3 and short_tasks == 1:
        angle = 0
        rocketx = 0
        rockety = random.choice([0, 192, 384, 576])
        endPos = [1195.25, random.choice([0, 192, 384, 576])]
        timer = 10  # Decrease this to count down.
        chart_course_exp()

    elif screen == 3.5 and short_tasks == 1:
        clock = pygame.time.Clock()
        #Delta time (time since last tick).
        dt = 0  
        def time():
            import main
            from main import gui, pygame, width
            main.dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.
            time = instructFont.render(str(round(main.timer)), True, blue)
            gui.blit(time, (width-100, 0))
            main.timer -= main.dt
        chart_course()
        time()
        if timer < 0:
            fails += 1
            screen = 3

    elif screen == 4 and long_tasks == 1:
        clicks = 0
        Pcol0 = silver
        Pcol1 = silver
        Pcol2 = silver
        Pcol3 = silver
        Pcol4 = silver
        Pcol5 = silver
        Pcol6 = silver
        Pcol7 = silver
        Pcol8 = silver


        ai = [silver, silver, silver, silver, silver, silver, silver, silver, silver]

        #Randomizing the colours for Simon Says
        colours = [red, green, pink, blue, yellow, silver, silver, silver, silver]
        for i in range(9):
            x = random.choice(colours)
            ai[i] = x
            colours.remove(x)

        count = 0
        pattern = ai
        pattern = list(pattern)
        while True:
            if silver not in pattern:        
                break
            else:
                pattern.remove(silver)

        random.shuffle(pattern)
        #Sets up timer for long task
        timer = 15  
        simon_says_exp()
    
    elif screen == 4.5 and long_tasks == 1:
        clock = pygame.time.Clock()
        dt = 0  

        #Countdown timer
        def time():
            import main
            from main import gui, pygame, width
            main.dt = clock.tick(30) / 1000 
            time = instructFont.render(str(round(main.timer)), True, blue)
            gui.blit(time, (width-100, 0))
            main.timer -= main.dt
        simon_says()
        time()
        if timer < 0:
            fails += 1
            screen = 4

    if game_end == True and screen == 5:
        end()
    
    #Updates the screen
    pygame.display.update() 

pygame.quit()
quit() 