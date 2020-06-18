import pygame
from pygame.locals import *

pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Chess")
icon = pygame.image.load('knightlogo.png')
pygame.display.set_icon(icon)

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 48)
textsurface = myfont.render('P', False, (0, 0, 0))


#Run Loop

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill((255, 255, 255))

    #
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 != 0:
                pygame.draw.rect(screen, (75, 75, 75), Rect(((i*width/8, j*height/8), (width/8, height/8))))
    #
    screen.blit(textsurface,(150 - (textsurface.get_rect().width/2), 50 - (textsurface.get_rect().height/2)))

    pygame.display.update()


