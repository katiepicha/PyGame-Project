import pygame.font

class Scoreboard:
    '''A class to report scoring information.'''

    def __init__(self, ai_game): # ai_game parameter allows access to the settings, screen, and stats objects
        '''Initialize scorekeeping attributes.'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30) # set text color
        self.font = pygame.font.SysFont(None, 48) # instantiate a font object

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score() # displayed separate from the score so we need a new method
        self.prep_level()

    def prep_score(self):
        '''Turn the score into a rendered image.'''
        rounded_score = round(self.stats.score, -1) # the -1 argument in the round() function rounds to the nearest 10
        score_str = "{:,}".format(rounded_score) # inserts commas into numbers when converting to a string
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color) # creates the image

        # Display the score at the top right of the screen and expands to the left as the score increases.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 # to make sure score always lines up with the right side of the screen
        self.score_rect.top = 20

    def prep_high_score(self):
        '''Turn the high score into a rendered image.'''
        high_score = round(self.stats.high_score, -1) # round the high score to the nearest 10
        high_score_str = "{:,}".format(high_score) # and format with commas
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx # center the high score rect horizontally
        self.high_score_rect.top = self.score_rect.top # set its top attribute to match the top of the score image

    def prep_level(self):
        '''Turn the level into a rendered image.'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color) # creates an image from value

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right # sets image right attribute to match the score's right attribute
        self.level_rect.top = self.score_rect.bottom + 10 # sets top attribute 10 pixels beneath the bottom of the score image

    def show_score(self):
        '''Draw scores and level to the screen.'''
        self.screen.blit(self.score_image, self.score_rect) # draws score image onscreen at the location score_rect specifies
        self.screen.blit(self.high_score_image, self.high_score_rect) # draws the high score at the top center of the screen
        self.screen.blit(self.level_image, self.level_rect) # draws the level image to the screen

    def check_high_score(self): # checks the current score against the high score
        '''Check to see if there's a new high score.'''
        if self.stats.score > self.stats.high_score: # if the current score is greater,
            self.stats.high_score = self.stats.score # we update the value of high score
            self.prep_high_score() # updates the high score's image