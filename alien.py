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

    def check_edges(self):
        '''Return True if alien is at edge of screen.'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: # to see whether alien is at the left or right edge
            return True

    def update(self):
        '''Move the alien right or left.'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        '''If fleet_direction is 1, the value of alien_speed will be added to the alien's current position, moving the alien to the
        right; if fleet_direction is -1, the value will be subtracted from the alien's position, moving the alient to the left.'''
        self.rect.x = self.x # update the position of the alien's rect