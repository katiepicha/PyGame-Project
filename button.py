import pygame.font # lets pygame render text to the screen

class Button:

    def __init__(self, ai_game, msg): # msg contains the button's text
        '''Initialize button attributes.'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) # set button's color to bright green
        self.text_color = (255, 255, 255) # set text color to white
        self.font = pygame.font.SysFont(None, 48) # None argument tells pygame to use default font, and 48 specifies the font size

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''Turn msg into a rendered image and center text on the button.'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # font.render() turns text to an image
        '''The font.render() method takes a Boolean value to turn antialiasing on or off (antialiasing makes the edges of the text
        smoother). The remaining arguments are the specified font and background color.'''
        self.msg_image_rect = self.msg_image.get_rect() # center the text image on the button
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect) # draw the rectangular portion of the button
        self.screen.blit(self.msg_image, self.msg_image_rect) # draw the text image to the screen
