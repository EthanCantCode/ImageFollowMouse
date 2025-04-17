import pygame
from pyrect import WIDTH, HEIGHT
import keyboard

pygame.init()

WIDTH = 500
HEIGHT = 500
IWIDTH = 50
IHEIGHT = 50
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

picture = pygame.transform.scale(pygame.image.load('Enter Image Path name here'), (IWIDTH, IHEIGHT))

run = True
while run:
    screen.fill('white')
    timer.tick(fps)
    mouse_position = pygame.mouse.get_pos()
    # pygame.draw.circle(screen,'purple', mouse_position, 10)

    # Adjust the position so the image centers on the mouse
    pic_rect = picture.get_rect(center=mouse_position)
    screen.blit(picture, pic_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
