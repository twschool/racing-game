"""v2 of the spawn sprites module
A Simple module to spawn the player on the screen 
using arrow keys to rotate / move the player"""

import pygame

pygame.init()



DISPLAY_SIZE = [1000, 600]
PLAYER_PREFIX = "cars/player/player-"
IMAGE_SUFFIX = ".png"

player_coords = [100, 100]
player_rotation = 0

player_images = ["black", "blue", "red", "white"]


# Get the players sprite based on the color given
get_player_filename = lambda player_color: PLAYER_PREFIX + player_color + IMAGE_SUFFIX


# Hardcoded sprite values
player_image = ["cars/player/player-black.png", "cars/player/player-blue.png", 
                "cars/player/player-red.png", "cars/player/player-white.png"]

screen = pygame.display.set_mode(DISPLAY_SIZE)


player_image_global = pygame.image.load( get_player_filename("red") )

pygame.display.set_caption('Test sprites!')


finished = False

while not finished:

    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    image = pygame.transform.rotate(player_image_global, player_rotation)

    screen.blit(image, player_coords)
    pygame.display.update()
    clock.tick(10)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.K_UP:
            if event.key == pygame.K_UP:
                player_coords[0] -= 20
            elif event.key == pygame.K_DOWN:
                player_coords[0] += 20
            elif event.key == pygame.K_LEFT:
                player_rotation += 30
                
            elif event.key == pygame.K_RIGHT:
                player_rotation -= 30
                
        elif event.type == pygame.MOUSEMOTION:
            print(event.dict["pos"])
    
    


