'''Date:Apr. 29, 2019
   Author:Andrew Lin
   Description: The classes that will be used in my BreakOut game.
'''


import pygame,random
 
class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, (255, 0, 0), (8, 8), 8, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,235)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.window = screen
        self.dx = 6
        self.dy = -5
 
    def changeDirection(self):
        '''This method causes the x direction of the ball to reverse.'''

        self.dy = -self.dy
       
             
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
           ((self.rect.bottom < self.window.get_height()) and (self.dy < 0)):
            self.rect.top -= self.dy
        # If yes, then reverse the y direction. 
        else:
            self.dy = -self.dy
            
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player 1 and the second paddle'''
    def __init__(self, screen,x,y):
        '''This initializer takes a screen surface, and player number as
        parameters.  Depending on the player number it loads the appropriate
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes for a black rectangle.
        self.image = pygame.Surface((100, 10))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
 
        # If we are initializing a sprite for player 1, 
        # position it 10 pixels from screen left.

        self.rect.top = y
 
        # Center the player hoizontally in the window.
        self.rect.centerx = x
        self.window = screen
        self.dx = 0
    
    def setPosition(self,x,y):
        '''This method recieves two int as a parameter to set the position 
        of the paddles.'''
        self.rect.centerx = x
        self.rect.top = y
        return self.rect.centerx, self.rect.top
    
    def changeDirection(self, xyChange):
        '''This method takes a (x,y) tuple as a parameter, extracts the 
        x element from it, and uses this to set the players x direction.'''
        self.dx = xyChange[0]
        

    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        # Check if we have reached the right or left of the screen.
        # If not, then keep moving the player in the same x direction.
        if ((self.rect.left > 0) and (self.dx < 0)) or\
           ((self.rect.right < self.window.get_width()) and (self.dx > 0)):
            self.rect.right += (self.dx*8)
            
class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our bottom end zones'''
    def __init__(self, screen, xPosition):
        '''This initializer takes a screen surface, and x position  as
        parameters.  For the left (player 1) endzone, x_position will = 0,
        and for the right (player 2) endzone, x_position will = 639.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.Surface((screen.get_width(),1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = xPosition
        self.rect.bottom = screen.get_height()
        
class Lives(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.font=pygame.font.Font("walt.ttf", 30)
        #self.font = pygame.font.SysFont("Arial", 30)
        self.player1Lives = 3
         
    def player1Lose(self):
        '''This method minuses one to the lives for player 1'''
        self.player1Lives -= 1
     
    def loser(self):
        '''Player 1 loses when 3 lives are lost.
        This method returns 0 if there is no loser yet, 1 if player 1 has lost 3 lives
        it returns 1.'''
        return self.player1Lives == 0

 
    def update(self):
        '''This method will be called automatically to display 
        the current amount of lives at the top of the game window.'''
        message = "Lives: " + str(self.player1Lives)
        self.image = self.font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 15)
        
class Brick(pygame.sprite.Sprite):
    '''A simple Sprite subclass to represent static Brick sprites.'''
    def __init__(self, screen,row,location):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((35, 20))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.points=row
        self.rect.center=location
        
        if self.points==1:   
            self.image.fill((0,0,255))

        elif self.points==2:
            self.image.fill((0,255,0))

        elif self.points==3:
            self.image.fill((253,145,3))
            
        elif self.points==4:
            self.image.fill((253,253,3))

        elif self.points==5:
            self.image.fill((255,0,0))

        elif self.points==6:
            self.image.fill((128,3,253))

    
    def getScore(self):
        '''This method returns the value of the brick object .'''
        return self.points
        
     
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
         
    def player1(self,points):
        '''This method adds one to the score for player 1'''
        self.score=points
        if self.score==1:   
            self.player1Score += 1
        if self.score==2:
            self.player1Score += 2
        if self.score==3:
            self.player1Score += 3
        if self.score==4:
            self.player1Score += 4
        if self.score==5:
            self.player1Score += 5
        if self.score==6:
            self.player1Score += 6
        
     
    def winner(self):
        '''There is a winner when one player reaches 378 points.
        This method returns 0 if there is no winner yet.'''
        if self.player1Score == 378:
            return 1

 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Player 1: " + str(self.player1Score)
        self.image = self.font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 15)
        
