import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))

brush = pygame.image.load("brush.png")
brush = pygame.transform.scale(brush, (50, 50))

clock = pygame.time.Clock()

z = 0

while 1:
    clock.tick(60)
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen, "screenshot.jpeg")
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            z = 1
        elif event.type == MOUSEBUTTONUP:
            z = 0
        if z == 1:
            screen.blit(brush, (x - 25, y - 25))
            pygame.display.update()