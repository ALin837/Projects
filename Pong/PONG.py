# I - IMPORT AND INITIALIZE
import pygame, pySprites
pygame.init()
     
def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # D - DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("pyPong! v1.0")
     
    # E - ENTITIES
    #background = pygame.Surface(screen.get_size())
    #background = background.convert()
    #background.fill((255, 255, 255))
    background= pygame.image.load("beach.jpg").convert()
    screen.blit(background, (0, 0))
    pygame.mixer.music.load("pirate.ogg")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)       
    
    boing=pygame.mixer.Sound("shotgun.wav")
    boing.set_volume(0.8)
    
    canon=pygame.mixer.Sound("canon.wav")
    canon.set_volume(1.0)
    mySystemFont = pygame.font.SysFont("Arial", 60)
    label1= mySystemFont.render("GAME OVER!", True, (255, 255, 0))
    # Initialize Joystick objects.
    joysticks = []
    for joystick_no in range(pygame.joystick.get_count()):
        stick = pygame.joystick.Joystick(joystick_no)
        stick.init()
        joysticks.append(stick)
 
    # Sprites for: ScoreKeeper label, End Zones, Ball, and Players
    scoreKeeper = pySprites.ScoreKeeper()
    ball = pySprites.Ball(screen)
    player1 = pySprites.Player(screen, 1)
    player1Endzone = pySprites.EndZone(screen,0)
    player2 = pySprites.Player(screen, 2)
    player2Endzone = pySprites.EndZone(screen,639)
    allSprites = pygame.sprite.OrderedUpdates(scoreKeeper, player1Endzone, \
                                     player2Endzone, ball, player1, player2)
 
    # A - ACTION
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
     
        # Hide the mouse pointer
    pygame.mouse.set_visible(False)
     
    # L - LOOP
    while keepGoing:
         
        # TIME
        clock.tick(30)
         
        # E - EVENT HANDLING: Player 1 uses joystick, Player 2 uses arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #elif event.type == pygame.JOYHATMOTION:
             #   player1.changeDirection(event.value)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2.changeDirection((0, 1))
                if event.key == pygame.K_DOWN:
                    player2.changeDirection((0, -1))
                if event.key == pygame.K_w:
                    player1.changeDirection((0, 1))
                if event.key == pygame.K_s:
                    player1.changeDirection((0, -1))
                        
     
        # Check if player 1 scores (i.e., ball hits player 2 endzone)
        if ball.rect.colliderect(player2Endzone):
                boing.play()
                scoreKeeper.player1Scored()
                ball.changeDirection()
     
        # Check if player 2 scores (i.e., ball hits player 1 endzone)
        if ball.rect.colliderect(player1Endzone):
                boing.play()
                scoreKeeper.player2Scored()
                ball.changeDirection()

                 
        # Check for game over (if a player gets 3 points)
        if scoreKeeper.winner():
            screen.blit(label1,(30,255))
            keepGoing = False
                         
        # Check if ball hits Player 1 or 2
        # If so, change direction, and speed up the ball a little
        if ball.rect.colliderect(player1.rect) or\
            ball.rect.colliderect(player2.rect):
            canon.play()
            ball.changeDirection()

                         
        # R - REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
             
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
     
    
    # Close the game window
    pygame.time.delay(3000)
    pygame.quit()    
         
# Call the main function
main()