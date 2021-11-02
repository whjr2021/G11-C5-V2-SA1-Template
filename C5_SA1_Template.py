# Import pygame library

# Initialzing pygame
pygame.init() 
# Create a game screen of width=600 and height=600 using pygame.display.set_mode() and name it as "screen"
screen = pygame.display.set_mode((600, 600))
# Create a title of game window to "Breakout Game" using pygame.display.set_caption()
pygame.display.set_caption("Breakout Game")
# Define the RGB color combinations of rectangle objects
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,150,0)
YELLOW = (255,255,0)
# Create a paddle rectangle object at x=300, y=500, width=60 and height=10 using pygame.Rect() and name it as "paddle"
paddle = pygame.Rect(300,500,60,10)
# Create a ball rectangle object at x=200, y=250, width=10 and height=10 using pygame.Rect() and name it as "ball"
ball = pygame.Rect(200,250,10,10)
# Define a variable "ballx" and assign -1 to it.
ballx = -1
# Define a variable "bally" and assign -1 to it.
bally = -1
# Define a variable "paddlex" and assign 2 to it.
paddlex = 2
# Define a variable "carryOn" and assign a value True to it.
carryOn = True
# Begin while loop with condition as "carryOn"

    # Use the for loop to iterate for each event
    
        # Checking if user clicked on close or quit on game screen
         
            # Change "carryOn" to False. This indicates we want to exit this while loop 
            
    # Filling the screen with darkblue color. The rgb combination of darkblue color is defined in varaible "DARKBLUE". 
    
      
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
