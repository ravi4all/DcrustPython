import pygame
import random

pygame.init()

width = 1000
height = 500

red = (255,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((width, height))

zombie_1 = pygame.image.load('images/zombie_1.gif')
zombie_2 = pygame.image.load('images/zombie_2.png')

zombie_list = [zombie_1, zombie_2]

currentZombie = random.choice(zombie_list)

pointer = pygame.image.load('images/aim_pointer.png')
backgroundImage = pygame.image.load('images/background.png')

shot_sound = pygame.mixer.Sound('sounds/shot_sound.wav')
backgroundMusic = pygame.mixer.Sound('sounds/background.wav')
backgroundMusic.play(-1)

counter = 0

zombie_x = random.randint(0,width - 100)
zombie_y = random.randint(0,height-100)

def score(counter):
    font = pygame.font.SysFont(None, 80)
    text = font.render('Score : '+str(counter), True, red)
    screen.blit(text, (40,0))

while True:

    posX, posY = pygame.mouse.get_pos()
    
    rect_1 = pygame.Rect(zombie_x, zombie_y, currentZombie.get_width(), currentZombie.get_height())

    rect_2 = pygame.Rect(posX,posY, pointer.get_width(), pointer.get_height())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            shot_sound.play()
            if rect_1.colliderect(rect_2):
                counter += 1
                currentZombie = random.choice(zombie_list)
                zombie_x = random.randint(0,width - 100)
                zombie_y = random.randint(0,height-100)
                print("Collision detection")

    #print(posX, posY)
    
    screen.fill(white)
    screen.blit(backgroundImage, (0,0))
    screen.blit(currentZombie, (zombie_x, zombie_y))

    screen.blit(pointer, (posX - 50, posY - 50))

    score(counter)

    pygame.display.update()
