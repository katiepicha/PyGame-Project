import sys # use tools in this module to exit the game when the player quits

import pygame # contains the functionality we need to make a game

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init() # initializes the background settings that pygame needs to work properly

        self.screen = pygame.display.set_mode((1200, 800)) 
        # creates a display window on which we'll draw all the game's graphical elements
        # (1200, 800) is a tuple that defines the dimensions of the game window, which is 1200 pixels wide and 800 pixels high
        # setting the display to self.screen attribute will allow it to be available in all methods of the class
        ''' The object we assigned to self.screen is a surface. A surface in Pygame is a part of the screen where a game element
        can be displayed. Each element in the game, like an alien or a ship, is its own surface. The surface returned by
        display.set_mode() represents the entire game window. When we activate the game's animation loop, this surface will be
        redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.'''
        pygame.display.set_caption("Alien Invasion")

    def run_game(self): # game is controlled by the run_game() method
        '''Start the main loop for the game.'''
        while True: # runs continually
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

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            ''' draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is
            visible. When we move the game elements around, pygame.display.flip() continually updates the display to show the
            new positions of game elements and hides the old ones, creating the illusion of smooth movement.'''

if __name__ == '__main__': # only runs if the file is called directly
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

