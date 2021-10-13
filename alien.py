import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent a single alien in the fleet.'''

    def __init__(self, ai_game):
        '''Initialize the alien and set its starting position.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width # add a space to the left that is equal to the alien's width so it is easy to see
        self.rect.y = self.rect.height # add a space above it that is equal to the alien's height so it is easy to see

        # Store the alien's exact horizonal position.
        self.x = float(self.rect.x) # mainly concerned with the alien's horizontal speed so we track the horizontal position precisely

    def update(self):
        '''Move the alien to the right.'''
        self.x += self.settings.alien_speed # track the alien's exact position (which can hold decimal values)
        self.rect.x = self.x # update the position of the alien's rect