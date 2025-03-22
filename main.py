import pygame
import os
import random
import time
pygame.font.init()

WIDTH,HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")

#Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("attatch","pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("attatch","pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("attatch","pixel_ship_blue_small.png"))

#Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("attatch","pixel_ship_yellow.png"))

# Laers
RED_LASER = pygame.image.load(os.path.join("attatch","pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("attatch","pixel_laser_green.png"))
BULE_LASER = pygame.image.load(os.path.join("attatch","pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("attatch","pixel_laser_yellow.png"))

# Background
BG = pygame.image.load(os.path.join("attatch","background-black.png"))

#"is_running = True
#while is_running:
#    WIN.blit()
#for event in pygame.event():
#    if event == pygame.quit()
#        break
#pygame.display.update()