'''To draw the player's ship on the screen, we will load an image and then use the Pygame blit() method to draw the image. It is
important to pay attention to licensing when choosing artwork for games. It is easiest to use a bitmap (.bmp) file because Pygame
loads bitmaps by default. It is also important to pay attention to the background color of your image.'''

import pygame
from pygame.sprite import Sprite

class Ship(Sprite): # make sure ships inherits from Sprite
    '''A class to manage the ship.'''

    def __init__(self, ai_game): # takes the self reference and a reference to the current instance of the AlienInvasion class
        # this gives Ship access to all the game resources defined in AlienInvasion
        '''Initialize the ship and set its starting position.'''
        super().__init__()
        self.screen = ai_game.screen # assign the screen to an attribute of Ship so we can access easily in all methods in the class
        self.settings = ai_game.settings # create a settings attribute for Ship so we can use it in update()
        self.screen_rect = ai_game.screen.get_rect() # allows us to place the ship in the correct location on the screen
        '''Pygame lets you treat all game elements like rectangles (rects). In order to figure out if two game elements have collided,
        rectangles make that recognition much easier.'''

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') # loads the image and give it the location of our ship image
        # this function (above) returns a surface representing the ship
        self.rect = self.image.get_rect()
        # when the image is loaded, we call get_rect() to access the ship surface's rect attribute so we can use it to place the ship

        '''When you're working with a rect object, you can use x- and y- coordinates at the top, bottom, left, and right edges of the
        rectangle, as well as the center to place the object. You can also use attributes of rect to place an object. Options: center, 
        centerx, centery, top, bottom, left, right, midbottom, midtop, midleft, midright.'''
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom # uses this attribute to center horizontally and align at the bottom

        '''Because we are adjusting the position of the ship by fractions of a pixel, we need to assign the position to a variable
        that can store a decimal value. You can use a decimal value to set an attribute of rect, but the rect will only keep the 
        integer portion of that value. To keep track of the ship's position accurately, we define a new self.x attribute that can
        hold decimal values.'''
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x) # float() function converts the value to a decimal

        '''When the player holds down the right arrow key, we want the ship to continue moving right until the player releases
        the key. When the key is released, the game will detect a pygame.KEYUP event, and we can use the KEYUP and KEYDOWN events
        together with a flag to implement continuous motion. When the flag is false (no key press), the ship will be motionless.'''
        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self): # not a helper method because it will be called through an instance of ship
        '''Update the ship's position based on the movement flags.'''
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: # checks the position of the ship before changing the value
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: # if value of the left side of the rect is > 0, the ship has not reached the edge
            self.x -= self.settings.ship_speed
        ''' use two separate if blocks instead of an elif to allow the ship's rect.x value to be increased and then decreased 
        when both arrow keys are held down. This results in the ship standing still.'''

        # Update rect object from self.x.
        self.rect.x = self.x # use new value to update self.rect.x which controls the position of the ship
        # only the integer portion of self.x will be stored in self.rect.x, but that's fine for displaying the ship

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect) # draws the image to the screen at the position specified by self.rect.
    
    def center_ship(self):
        '''Center the ship on the screen.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
