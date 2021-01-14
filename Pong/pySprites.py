import pygame
 
class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 10, 0)
        #self.image = pygame.image.load("ball.jpg")    
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.window = screen
        self.dx = 5  #5
        self.dy = -3   #-3
 
    def changeDirection(self):
        '''This method causes the x direction of the ball to reverse.'''
        if self.dx < 0:
            self.dx-=1
        elif self.dx > 1:
            self.dx+=1
        elif self.dy < 0:
            self.dx-=1
        elif self.dy > 1:
            self.dy+=1         
            
        self.dx = -self.dx
       
             
    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''
        # Check if we have reached the left or right end of the screen.
        # If not, then keep moving the ball in the same x direction.
        if ((self.rect.left > 0) and (self.dx < 0)) or\
           ((self.rect.right < self.window.get_width()) and (self.dx > 0)):
            self.rect.left += self.dx
        # If yes, then reverse the x direction. 
        else:
            self.dx = -self.dx
             
        # Check if we have reached the top or bottom of the court.
        # If not, then keep moving the ball in the same y direction.
        if ((self.rect.top-40 > 0) and (self.dy > 0)) or\
           ((self.rect.bottom+40 < self.window.get_height()) and (self.dy < 0)):
            self.rect.top -= self.dy
        # If yes, then reverse the y direction. 
        else:
            self.dy = -self.dy
            
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player 1 and Player 2'''
    def __init__(self, screen, playerNum):
        '''This initializer takes a screen surface, and player number as
        parameters.  Depending on the player number it loads the appropriate
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes for a black rectangle.
        #self.image = pygame.Surface((10, 100))
        #self.image = self.image.convert()
        #self.image.fill((0, 0, 0))
        self.image = pygame.image.load("twig.jpg")        
        self.rect = self.image.get_rect()
 
        # If we are initializing a sprite for player 1, 
        # position it 10 pixels from screen left.
        if playerNum == 1:
            self.rect.left = 10
        # Otherwise, position it 10 pixels from the right of the screen.
        else:
            self.rect.right = screen.get_width()-10
 
        # Center the player vertically in the window.
        self.rect.top = screen.get_height()/2 + 50
        self.window = screen
        self.dy = 0
      
    def changeDirection(self, xyChange):
        '''This method takes a (x,y) tuple as a parameter, extracts the 
        y element from it, and uses this to set the players y direction.'''
        self.dy = xyChange[1]
         
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        # Check if we have reached the top or bottom of the screen.
        # If not, then keep moving the player in the same y direction.
        if ((self.rect.top > 0) and (self.dy > 0)) or\
           ((self.rect.bottom < self.window.get_height()) and (self.dy < 0)):
            self.rect.top -= (self.dy*7)   #5
        # If yes, then we don't change the y position of the player at all.
    
class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our left and right end zones'''
    def __init__(self, screen, xPosition):
        '''This initializer takes a screen surface, and x position  as
        parameters.  For the left (player 1) endzone, x_position will = 0,
        and for the right (player 2) endzone, x_position will = 639.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.Surface((1, screen.get_height()))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = xPosition
        self.rect.top = 0
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.font=pygame.font.Font("walt.ttf", 30)
        #self.font = pygame.font.SysFont("Arial", 30)
        self.player1Score = 0
        self.player2Score = 0
         
    def player1Scored(self):
        '''This method adds one to the score for player 1'''
        self.player1Score += 1
 
    def player2Scored(self):
        '''This method adds one to the score for player 1'''
        self.player2Score += 1
     
    def winner(self):
        '''There is a winner when one player reaches 3 points.
        This method returns 0 if there is no winner yet, 1 if player 1 has
        won, or 2 if player 2 has won.'''
        if self.player1Score == 5:
            return 1
        elif self.player2Score == 5:
            return 2
        else:
            return 0
 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Player 1: " + str(self.player1Score) +\
            " vs. Player 2: " + str(self.player2Score)
        self.image = self.font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)