import pygame
from pygame.sprite import Sprite # sprites allow us to group related elements in the game and act on all grouped elements at once

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship'''

    def __init__(self, ai_game): # __init__() needs the current instance of AlienInvasion
        '''Create a bullet object at the ship's current position.'''
        super().__init__() # super() inherits properly from Sprite
        self.screen = ai_game.screen # sets attributes for the screen and settings objects and the bullet's color
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) # not based on image so built from scratch
        self.rect.midtop = ai_game.ship.rect.midtop # this will make the bullet emerge from the top of the ship

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y) # store as decimal so we can make fine adjustments to the speed of the bullet

    def update(self): # update() method manages the bullet's position
        '''Move the bullet up the screen.'''
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed # the bullet speed setting allows us to increase the speed as the game progresses
        # Update the rect position.
        self.rect.y = self.y 

    def draw_bullet(self):
        '''Draw the bullet to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect) #the draw.rect() function fills the part of the screen defined by the
        # bullet's rect with the color stored in self.color.'''
