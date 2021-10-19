import sys # use tools in this module to exit the game when the player quits
from time import sleep # allows us to pause the game for a moment when the ship is hit

import pygame # contains the functionality we need to make a game

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init() # initializes the background settings that pygame needs to work properly
        self.settings = Settings() # create an instance of Settings

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # figure out a window size that will fill the screen
        self.settings.screen_width = self.screen.get_rect().width # use width and height attributes to update the settings object
        self.settings.screen_height = self.screen.get_rect().height 
        # creates a display window on which we'll draw all the game's graphical elements
        # (1200, 800) is a tuple that defines the dimensions of the game window, which is 1200 pixels wide and 800 pixels high
        # we use the screen_width and screen_height attributes of self.settings
        # setting the display to self.screen attribute will allow it to be available in all methods of the class
        ''' The object we assigned to self.screen is a surface. A surface in Pygame is a part of the screen where a game element
        can be displayed. Each element in the game, like an alien or a ship, is its own surface. The surface returned by
        display.set_mode() represents the entire game window. When we activate the game's animation loop, this surface will be
        redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.'''
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self) # make an instance of ship after the screen has been created
        # the call to Ship() requires one argument, an instance of AI and the self argument refers to the current instance of AI
        # this is the parameter that gives Ship access to the game's resources
        self.bullets = pygame.sprite.Group() # instance of the pygame.sprite.Group class which behaves like a list
        # we will use this group to draw bullets to the screen on each pass through the main loop and to update each bullet's position
        self.aliens = pygame.sprite.Group() # create a group to hold the fleet of aliens

        self.__create_fleet()

        # set the background color
        self.bg_color = (230, 230, 230) # colors in Pygame are specified as RGB colors (red, green, blue) that range from 0-255
        # you can mix values to create up to 16 million colors. this produces a light gray background color 

        # Make the Play button.
        self.play_button = Button(self, "Play") # creates an instance of Button with the label "Play"

    def run_game(self): # game is controlled by the run_game() method
        '''Start the main loop for the game.'''
        while True: # runs continually
            # helper methods: do work inside a class but are not meant to be called through an instance
            self._check_events() # allows you to manage events separately from other aspects of the game (always need to call)

            if self.stats.game_active: # only called when the game is active
                self.ship.update() # allows position to be updated in response to player's input and ensures updated position will be used
                self._update_bullets()
                self._update_aliens()

            self._update_screen() # a separate method to simplify code (always need to call)

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() # call _fire_bullet() when the spacebar is pressed

    def __check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False # set moving_right to false when right key is released
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False # set moving_left to false when left key is released

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self) # make an instance of Bullet
            self.bullets.add(new_bullet) # add instance to the group bullets using the add() method (similar to append)
        '''When the player presses the spacebar, we check the length of the bullets. If len(self.bullets) is less than three, 
        we create a new bullet. But if three bullets are already active, nothing happens when the spacebar is pressed.'''

    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets.'''
        # Update bullet positions.
        self.bullets.update() # calls bullet.update() for each bullet we place in the group bullets

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy(): # copy() method to set up the for loop which enables us to modify bullets inside loop
            if bullet.rect.bottom <= 0: # check each bullet to see whether it has disappeared off the top of the screen
                self.bullets.remove(bullet) # remove it from bullets

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        '''Respond to bullet-alien collisions.'''
        # Remove any bullets and aliens that have collided.        
        '''The sprite.groupcollide() function compares the rects of each element in one group with the rects of each element in
        another group. In this case, it compares each bullet's rect with the alien's rect and returns a dictionary containing
        the bullets and aliens that have collided. Each key in the dictionary will be a bullet, and the corresponding value will
        be the alient that was hit.'''
        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien. (The two True arguments will delete the bullets and aliens)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens: # check whether the aliens group is empty (an empty group evaluates to False)
            # Destroy existing bullets and create new fleet.
            self.bullets.empty() # get rid of any existing bullets by removing all remaining sprites from a group
            self.__create_fleet() # fills the screen with aliens again

    def _check_aliens_bottom(self):
        '''Check if any aliens have reached the bottom of the screen.'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self.__ship_hit()
                break # if one alien hits the bottom, there is no need to check the rest, so we break

    def _update_aliens(self):
        '''Check if the fleet is at an edge, then update the positions of all aliens in the fleet.'''
        self._check_fleet_edges() 
        self.aliens.update() # calls each alien's update() method

        '''The spritecollideany() function takes two arguments: a sprite and a group. The functions looks for any member of the group
        that has collided with the sprite and stops looking through the group as soon as it finds one member that has collided with
        the sprite. Here, it loops through the group aliens and returns the first alien it finds that has collided with the ship.'''
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens): # if no collisions occur, the returns None and the if won't execute
            self.__ship_hit() # if it finds a collision, the if block will execute

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def __create_fleet(self):
        '''Create the fleet of aliens.'''
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self) # need to know width and height to place so we create an alien before calculations (not part of fleet)
        alien_width, alien_height = alien.rect.size # get alien's width and height from the size attribute in the rect object
        available_space_x = self.settings.screen_width - (2 * alien_width) # calculate the horizontal space available for aliens
        number_aliens_x = available_space_x // (2 * alien_width) # calculate the number of aliens that can fit in that space

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height # calculate number of rows fit on screen
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows): # outer loop that counts from 0 to the number of rows we want
            for alien_number in range(number_aliens_x): # inner loop that creates the aliens in one row
                self.__create_alien(alien_number, row_number) # helper method

    def __create_alien(self, alien_number, row_number):
        '''Create an alien and place it in the row.'''
        alien = Alien(self) # create a new alien
        alien_width, alien_height = alien.rect.size # get the width and height inside method instead of passing as an argument
        alien.x = alien_width + 2 * alien_width * alien_number # set its x-coordinate value to place it in the row
        ''' ^ Each alien is pushed to the right one alien width from the left margin. We multiply alien width by 2 to account for 
        the space each alien takes up, including the empty space to its right, and we multiply this amount by the alien's position
        in the row.'''
        alien.rect.x = alien.x # use the alien's x attribute to set the position of its rect
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number # change y coorinate when not in the first row
        self.aliens.add(alien) # and then adding it to the group that will hold the fleet

    def _check_fleet_edges(self):
        '''Respond appropriately if any aliens have reached an edge.'''
        for alien in self.aliens.sprites(): # loop through the fleet and call check_edges() for each alien
            if alien.check_edges(): # if check_edges() returns True, we know alien is at the edge
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction.'''
        for alien in self.aliens.sprites(): # loop through all the aliens and drop each one using the setting fleet_drop_speed
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 # line isn't part of the for loop because we only want to change direction once

    def __ship_hit(self):
        '''Respond to the ship being hit by an alien.'''
        if self.stats.ships_left > 0: # tests to make sure player has at least one ship remaining, if so create new fleet and move on
            # Decrement ships_left.
            self.stats.ships_left -= 1 # reduce the number of ships left by 1 when an alien hits a ship

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty() # empty the groups aliens and bullets

            # Create a new fleet and center the ship.
            self.__create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5) # pauses program execution for a half second, long enough for the player to see that the alien has hit the ship
        else:
            self.stats.game_active = False

    def _update_screen(self):
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color) # fill the screen with the background color; fill() acts on a surface
        # we use self.settings to access the background color when filling the screen
        self.ship.blitme() # draws the ship on the screen on top of the background
        for bullet in self.bullets.sprites(): # bullets.sprites() returns a list of all sprites in the group bullets 
            bullet.draw_bullet() # loop through bullets.sprites() and call draw_bullet() on each one to draw fired bullets to screen
        self.aliens.draw(self.screen) # draw() on a group draws each element in the group at the position defined by its rect attribute
        
        # Draw the play button if the game is inactive.
        # to make play button visible above other elements, we draw it after the other elements, but before flipping to new screen
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        ''' draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is
        visible. When we move the game elements around, pygame.display.flip() continually updates the display to show the
        new positions of game elements and hides the old ones, creating the illusion of smooth movement.'''

if __name__ == '__main__': # only runs if the file is called directly
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

