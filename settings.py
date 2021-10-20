''' Each time we introduce a new functionality into the game, we'll typically create some new settings. Instead of adding settings
throughout the code, we wrote a module called settings that contains a class to store all the values in one place. This approach
allows us to work with just one settings object any time we need to access an individual setting. This also makes it easier to 
modify the game's appearance and behavior as the project grows.'''

class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's static settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3 # the number of ships the player starts with

        # Bullet settings
        self.bullet_width = 3 # width of 3 pixels
        self.bullet_height = 15 # height of 15 pixels
        self.bullet_color = (60, 60, 60) # dark grey bullets
        self.bullets_allowed = 3 # limits the player to 3 bullets at a time

        # Alien settings
        self.fleet_drop_speed = 10 # controls how quickly the fleet drops down the screen each time an alien reaches either edge

        # How quickly the game speeds up
        self.speedup_scale = 1.1 # value of 2 doubles the speed, a value of 1 keeps the speed constant
        # value of 1.1 should increase speed to be challenging but not impossible

        # How quickly the alien point values increase
        self.score_scale = 1.5 # increase by a noticable amount

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialize settings that change throughout the game.'''
        # sets the initial values for the ship, bullet, and alien speeds
        self.ship_speed = 1.5 # position is adjusted by 1.5 pixels each pass through the loop
        # decimals give us finer control of the ship's speed when we increase the tempo of the game
        self.bullet_speed = 1.5 # bullets will travel slightly slower than the ship
        self.alien_speed = 1.0

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        '''Increase speed settings and alien point values.'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale) # when speed is increased, so is the point value of each hit

    