class GameStats:
    '''Track statistics for Alien Invasion.'''

    def __init__(self, ai_game):
        '''Initialize statistics.'''
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        self.ships_left = self.settings.ship_limit
        self.score = 0 # will reset the score each time a new game starts
        self.level = 1 # resets the level at the start of each new game