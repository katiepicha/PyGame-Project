import sys # use tools in this module to exit the game when the player quits

import pygame # contains the functionality we need to make a game

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init() # initializes the background settings that pygame needs to work properly
        self.settings = Settings() # create an instance of Settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        # creates a display window on which we'll draw all the game's graphical elements
        # (1200, 800) is a tuple that defines the dimensions of the game window, which is 1200 pixels wide and 800 pixels high
        # we use the screen_width and screen_height attributes of self.settings
        # setting the display to self.screen attribute will allow it to be available in all methods of the class
        ''' The object we assigned to self.screen is a surface. A surface in Pygame is a part of the screen where a game element
        can be displayed. Each element in the game, like an alien or a ship, is its own surface. The surface returned by
        display.set_mode() represents the entire game window. When we activate the game's animation loop, this surface will be
        redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.'''
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # make an instance of ship after the screen has been created
        # the call to Ship() requires one argument, an instance of AI and the self argument refers to the current instance of AI
        # this is the parameter that gives Ship access to the game's resources

        # set the background color
        self.bg_color = (230, 230, 230) # colors in Pygame are specified as RGB colors (red, green, blue) that range from 0-255
        # you can mix values to create up to 16 million colors. this produces a light gray background color 

    def run_game(self): # game is controlled by the run_game() method
        '''Start the main loop for the game.'''
        while True: # runs continually
            # helper methods: do work inside a class but are not meant to be called through an instance
            self._check_events() # allows you to manage events separately from other aspects of the game
            self.ship.update() # allows position to be updated in response to player's input and ensures updated position will be used
            self._update_screen() # a separate method to simplify code

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get(): # event loop and code manages screen updates
            ''' An event is an action that the user performs while playing the game, such as pressing a key or moving a mouse
            to make our program respond to events, we write this loop to listen for events and perform appropriate tasks
            depending on the kind of events that occur.''' 
            ''' pygame.event.get() is used to access the events that pygame detects. This function return a list of events
            that have taken place since the last time the function was called. Any keyboard or mouse event will cause this
            for loop to run.'''
            if event.type == pygame.QUIT: # to detect and respond to specific events like clicking the game window's close button
                sys.exit() # exits the game
            elif event.type == pygame.KEYDOWN: # KEYDOWN event = any key press by the user
                self.__check_keydown_events(event) # call to new method (simpler with cleaner code structure)
            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event) # call to new method (simpler with cleaner code structure)

    def __check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT: # check whether the key pressed was the right arrow key
            self.ship.moving_right = True # set moving_right to true when the right key is pressed
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True # set moving_left to true when the left key is pressed
        elif event.key == pygame.K_q:
            sys.exit() # ends the game when the player presses 'Q'

    def __check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False # set moving_right to false when right key is released
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False # set moving_left to false when left key is released

    def _update_screen(self):
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color) # fill the screen with the background color; fill() acts on a surface
        # we use self.settings to access the background color when filling the screen
        self.ship.blitme() # draws the ship on the screen on top of the background
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        ''' draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is
        visible. When we move the game elements around, pygame.display.flip() continually updates the display to show the
        new positions of game elements and hides the old ones, creating the illusion of smooth movement.'''

if __name__ == '__main__': # only runs if the file is called directly
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

