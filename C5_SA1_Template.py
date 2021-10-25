# Import pygame library

# Initialze pygame
 
# Create a game screen of width=600 and height=600 using pygame.display.set_mode() and name it as "screen"

# Create a title of game window to "Breakout Game" using pygame.display.set_caption()

# Define the RGB color combinations of rectangle objects
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,150,0)
YELLOW = (255,255,0)
# Create a paddle rectangle object at x=300, y=500, width=60 and height=10 using pygame.Rect() and name it as "paddle"

# Create a ball rectangle object at x=200, y=250, width=10 and height=10 using pygame.Rect() and name it as "ball"

# Define a variable "ballx" and assign -1 to it.

# Define a variable "bally" and assign -1 to it.

# Define a variable "paddlex" and assign 2 to it.

# Define a variable "carryOn" and assign a value True to it.

# Begin while loop with condition as "carryOn"

    # Use the for loop to iterate for each event
        
        # Check if user clicked on close or quit on game screen
         
            # Change carryOn to False. This indicates that we are done so we exit this while loop 
            
    # Fill the screen with darkblue color. 
    
      
    # Check for user input to move the paddle
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=paddlex
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=paddlex
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    
    # Update x and y position of the ball on screen 
    ball.x = ball.x + ballx
    ball.y = ball.y + bally
    # Limiting ball movement on screen along x-axis
    if ball.x >= 590:
      ballx = -ballx
    if ball.x <= 10:
      ballx = -ballx
    # Limiting ball movement on screen along y-axis
    if ball.y >= 590:
      bally = -bally
    if ball.y <= 10:
      bally = -bally
    pygame.draw.rect(screen,WHITE ,ball)
    
    # Check for paddle and ball collision and change the ball direction if they collided
    if paddle.collidepoint(ball.x, ball.y):
        bally = -bally
    # Create and draw 6 red bricks on screen 
    for i in range(0,6):
        brick = pygame.Rect(10 + i* 100,60,80,30)
        pygame.draw.rect(screen,RED,brick)
    # Create and draw 6 orange bricks on screen 
    for i in range(0,6):
        brick = pygame.Rect(10 + i* 100,100,80,30)
        pygame.draw.rect(screen,ORANGE,brick)
    # Create and draw 6 yellow bricks on screen 
    for i in range(0,6):
        brick = pygame.Rect(10 + i* 100,140,80,30)
        pygame.draw.rect(screen,YELLOW,brick)
    pygame.time.wait(8)
    # Update the contents of entire display
    pygame.display.flip()
    
# Quit the game  
pygame.quit()