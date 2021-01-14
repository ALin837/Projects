'''Date:Apr. 29, 2019
   Author:Andrew Lin
   Description: A BreakOut game that has an enhancement that will add another paddle once
   half the bricks have been eliminated.
'''

# I - IMPORT AND INITIALIZE
import pygame, BOsprites
pygame.init()
     
def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # D - DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("BreakOut")
     
    # E - ENTITIES
    background= pygame.image.load("background.png").convert()
    
    bordertop = pygame.Surface((screen.get_width(), 38))
    bordertop = bordertop.convert()
    bordertop.fill((0,0,0))

    
    screen.blit(background, (0, 0))
    screen.blit(bordertop, (0, 0))

    
    pygame.mixer.music.load("pirate.ogg")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)       
    
    boing=pygame.mixer.Sound("shotgun.wav")
    boing.set_volume(0.6)
    
    canon=pygame.mixer.Sound("canon.wav")
    canon.set_volume(1.0)   
    
    Lose=pygame.mixer.Sound("Lose.wav")
    Lose.set_volume(0.8)       
    
    gun=pygame.mixer.Sound("gun.wav")
    gun.set_volume(1.0)
    
    myFont = pygame.font.Font("walt.ttf", 60)
    label1= myFont.render("GAME OVER!", True, (0, 0, 0))
    label2= myFont.render("ALL DONE!", True, (0, 0, 0))
    # Initialize Brick objects.
    bricks = []
    
    for row in range(1,7):
        for brickNumber in range(1,19):
            location=(36*brickNumber-int((35/2)),230-20*row)
            bricks.append(BOsprites.Brick(screen,row,location))
       
    


    # Sprites for: ScoreKeeper label, End Zones, Ball, Players, Bricks

    Lives = BOsprites.Lives()
    Score = BOsprites.ScoreKeeper()
    ball = BOsprites.Ball(screen)
    player1 = BOsprites.Player(screen,screen.get_width()/2,screen.get_height()-10)
    SecondPaddle=BOsprites.Player(screen,1000,1000)
    player1Endzone = BOsprites.EndZone(screen,0)
    brickGroup=pygame.sprite.OrderedUpdates(bricks)
    allSprites = pygame.sprite.OrderedUpdates(Lives, player1Endzone, ball, player1, Score, bricks,SecondPaddle)
    
    
    #bricks=BOsprites.EndZone(screen)
    
    
    # A - ACTION
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    switch=True
        # Hide the mouse pointer
    pygame.mouse.set_visible(False)
     
    # L - LOOP
    while keepGoing:
         
        # TIME
        clock.tick(30)
         
        # E - EVENT HANDLING: Player 1 uses arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    player1.changeDirection((-1,0))
                    SecondPaddle.changeDirection((1,0))
                elif event.key==pygame.K_RIGHT:
                    player1.changeDirection((1,0))
                    SecondPaddle.changeDirection((-1,0))
                    
        # If the ball hits the player 1 paddle, change direction.
        if ball.rect.colliderect(player1.rect):
            canon.play()
            ball.changeDirection()
        
        # If the ball hits the second paddle.
        if ball.rect.colliderect(SecondPaddle.rect):
            canon.play()
            ball.changeDirection()        
            
        # If the ball hits a brick, the brick should be deleted and score should be added.
        collision = pygame.sprite.spritecollide(ball, brickGroup, False)
        if collision:
            for Bricks in collision:
                Score.player1(Bricks.getScore())
                Bricks.kill()
            boing.play()
            ball.changeDirection()            
                    
        if len(brickGroup) == 54 and switch==True :
            gun.play()
            SecondPaddle.setPosition(screen.get_width()/2,screen.get_height()-10)
            switch=False

     
        # Check if ball hits player's endzone
        if ball.rect.colliderect(player1Endzone):
            Lose.play()
            Lives.player1Lose()
            ball.changeDirection()

                 
        # Check for game over (if a player loses 3 lives)
        if Lives.loser():
            screen.blit(label1,(100,255))
            keepGoing = False
            
        if Score.winner():
            screen.blit(label2,(100,255))
            keepGoing = False
                         

                         
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