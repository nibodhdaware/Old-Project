import pygame
import random

# initialization
pygame.init()

#Window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

#images
one = pygame.image.load("dice faces\die_face_1.png")
two = pygame.image.load("dice faces\die_face_2.png")
three = pygame.image.load("dice faces\die_face_3.png")
four = pygame.image.load("dice faces\die_face_4.png")
five = pygame.image.load("dice faces\die_face_5.png")
six = pygame.image.load("dice faces\die_face_6.png")

#game loop
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                num = random.randint(1,6)
                print(num)
                if num == 1:
                    win.blit(one, (0,0))
                if num == 2:
                    win.blit(two, (0,0))
                if num == 3:
                    win.blit(three, (0,0))
                if num == 4:
                    win.blit(four, (0,0))
                if num == 5:
                    win.blit(five , (0,0))
                if num == 6:
                    win.blit(six, (0,0))
    pygame.display.update()