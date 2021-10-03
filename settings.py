''' Each time we introduce a new functionality into the game, we'll typically create some new settings. Instead of adding settings
throughout the code, we wrote a module called settings that contains a class to store all the values in one place. This approach
allows us to work with just one settings object any time we need to access an individual setting. This also makes it easier to 
modify the game's appearance and behavior as the project grows.'''

class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5 # position is adjusted by 1.5 pixels each pass through the loop
        # decimals give us finer control of the ship's speed when we increase the tempo of the game

    