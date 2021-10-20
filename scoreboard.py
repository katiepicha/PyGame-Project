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

    def prep_score(self):
        '''Turn the score into a rendered image.'''
        rounded_score = round(self.stats.score, -1) # the -1 argument in the round() function rounds to the nearest 10
        score_str = "{:,}".format(rounded_score) # inserts commas into numbers when converting to a string
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color) # creates the image

        # Display the score at the top right of the screen and expands to the left as the score increases.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 # to make sure score always lines up with the right side of the screen
        self.score_rect.top = 20

    def show_score(self):
        '''Draw score to the screen.'''
        self.screen.blit(self.score_image, self.score_rect) # draws score image onscreen at the location score_rect specifies