import pygame
import random

pygame.init()

white = (255,255,255)
red = (255,0,0)

rect_x = 50
rect_y = 50

clock = pygame.time.Clock()
FPS = 100

speed = [2,2]

width = 600
height = 500

gameBoard = pygame.display.set_mode((width, height))

while True:

    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 10
                move_y = 10
                print("KEY PRESSED...")
                
    gameBoard.fill(white)
    #rect = pygame.draw.rect(gameBoard, red, [rect_x, rect_y, 50, 50])
    pygame.draw.circle(gameBoard, red, [rect_x,rect_y], 50)
    
    rect_x += speed[0]
    rect_y += speed[1]

    if rect_x > width - 50 or rect_x <= 0:
        speed[0] = -speed[0]
    elif rect_y > height - 50 or rect_y <= 0:
        speed[1] = -speed[1]

    pygame.display.update()
    clock.tick(FPS)








