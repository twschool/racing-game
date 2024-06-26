"""
v1 of the spawn vehicle module
A Module to spawn a enemy vehicle on the screen
This module just works on the spawning of the enemy vehicle on the screen
not the ai or the movement of the vehicle.

Instead of doing that I converted everything into being object orientated
the vehicle spawning will be down in v2
"""

import random
import copy
import pygame
from vehicles_vars import NPCVehicle, SpecialVehicle, TruckVehicle, PLAYER_PREFIX, IMAGE_SUFFIX


DISPLAY_SIZE = [800, 700]



class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def format(self):
        """Returns the players formatted coordinates (x, y) as a tuple"""
        return (self.x, self.y)


class Sprite(Coordinate):
    """A class to represent a sprite on the screen"""
    
    def __init__(self, x, y, image_object: pygame.Surface, scale=1):
        """Initialize the sprite object with the x, y coordinates and the scaled image object"""
        super().__init__(x, y)
        
        # Scales the player image object to the given scale
        self.image_object = pygame.transform.scale(
                                                    image_object, (
                                                        int(image_object.get_width() * scale),
                                                        int(image_object.get_height() * scale)
                                                                      )
                                                   )
        
    def show(self, screen: pygame.Surface):
        """Displays the sprite on the screen"""
        screen.blit(self.image_object, self.format())


class Player(Sprite):
    """A class to represent the player on the screen"""
    def __init__(self, color):
        
        player_filename = self.get_player_filename(color)
        image = pygame.image.load(player_filename)
        
        # Initiate the sprite class with the image object and x, y coords
        super().__init__(100, 500, image, 1.25)
        
        self.color = color
 

        

    def get_player_filename(self, color):
        return PLAYER_PREFIX + color + IMAGE_SUFFIX

    def get_coords(self):
        """Return the x, y coords as a tuple (x, y)"""
        return self.format()
    
        
class Background:
    """A class to represent the background image on the screen"""
    def __init__(self):
        """Initiator."""
        self.y1 = 0  # Start the first image at the top of the screen
        self.y2 = -background_image_object.get_height()  # Start the second image immediately above the first

        self.image_object = background_image_object

    def update_background(self):
        """Update the position of the background for scrolling effect."""
        self.y1 += 5
        self.y2 += 5

        # Reset y1 and y2 to create a seamless loop
        if self.y1 >= background_image_object.get_height():
            self.y1 = self.y2 - background_image_object.get_height()

        if self.y2 >= background_image_object.get_height():
            self.y2 = self.y1 - background_image_object.get_height()
    
    def show(self, screen: pygame.Surface):
        screen.blit(self.image_object, (0, self.y1))
        screen.blit(self.image_object, (0, self.y2))



class Enemy(Sprite):    
    """A class to represent the enemy vehicle on the screen"""
    def __init__(self, color):
        """Initiator"""
        
        # Initiate the 
        super().__init__(100, 100, pygame.image.load(self.get_enemy_filename(color)))
        self.color = color
        self.speed = random.randint(GameController.enemy_speed_range)


class GameController:
    def __init__(self, fps=60):
        self.enemy_speed_range = (1, 5)
        self.enemy_objects = []
        self.spawn_rate = fps * 2
        self.next_car_spawn_interval = 0
        self.previous_lane = 0
        self.offscreen_limits = (-300, DISPLAY_SIZE[1] + 300)
    
    def update(self, screen: pygame.Surface, player_object: Player,
                enemy_objects: list[Enemy]):
        
        """Update the game state"""
        
       
        player_object.show(screen)
        
        for enemy in copy.deepcopy(enemy_objects):
            if enemy.y > self.offscreen_limits[1]:
                enemy_objects.remove(enemy)


        # self.spawn_enemy()
        # self.move_enemies()
        # self.check_collision()
    
        
def make_background_object() -> pygame.Surface:
    # Define all background related variables
    background_image = pygame.image.load("background.png")
    background_scale_x =  DISPLAY_SIZE[0] / background_image.get_width()
    background_scale_y =  (DISPLAY_SIZE[1] * 2) / background_image.get_height()
    new_background_image = pygame.transform.scale(background_image, (int(background_image.get_width() * background_scale_x)
                                                            , int(background_image.get_height() * background_scale_y)))
    return new_background_image  






# Initialize pygame and set the display caption
pygame.init()
pygame.display.set_caption('Test sprites!')
screen = pygame.display.set_mode(DISPLAY_SIZE)


# Main routine
background_image_object = make_background_object() # Used for testing purposes


# Defines the y upper and lower bound to give the illusion of screen wrapping for the background
# The upper bound is the highest the y of the image can be be so that the full image is displayed on the screen
# The lower bound is the lowest the image can be so the full image is displayed on the screen
# When the y is 0 the image isnt displayed on the screen (fully offscreen)
y_lower_bound = background_image_object.get_height() - DISPLAY_SIZE[1]
y_upper_bound = background_image_object.get_height()


background_object = Background()


fps = 60
finished = False
player_object = Player("blue")


game_controller = GameController()

enemy_objects: list[Enemy] = []

clock = pygame.time.Clock()

print(f"Y upper bound: {y_upper_bound}, Y lower bound: {y_lower_bound}")
# Main loop
while not finished:

    screen.fill((0, 0, 0))
    
    background_object.update_background()
    background_object.show(screen)
    
    game_controller.update(screen, player_object, enemy_objects)
    
    
    pygame.display.update()
    clock.tick(fps)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_object.x + player_object.image_object.get_width() >= 220:
            player_object.x -= 6
    if keys[pygame.K_RIGHT]:
        if player_object.x + player_object.image_object.get_width() <= DISPLAY_SIZE[0] - 150:
            player_object.x += 6
    
    if keys[pygame.K_UP]:
        if player_object.y + player_object.image_object.get_height() >= 122:
                player_object.y -= 6
    if keys[pygame.K_DOWN]:
        if player_object.y + player_object.image_object.get_height() <= DISPLAY_SIZE[1] - 2:
            player_object.y += 4

   
    # Event handling
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            finished = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                print(player_object.get_coords())
                
        
        # For debugging purposes
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.dict["pos"])


    # When the y get to y -787