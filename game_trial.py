import pygame
import time
import random

pygame.init()

#defining colors
white = (255,255,255)
black = (0,0,0)
blue = (35,41,207)
red = (227,23,0)
green = (2,227,55)

#Display size and settings
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pong')

pygame.display.update()

clock = pygame.time.Clock()

#Fixed variable definitions
ball_radius = 7
pad_width = 20
pad_height = 60
pad_move = 10
l_score = 0
r_score = 0
FPS = 50

font = pygame.font.SysFont(None, 25)

#making a screen message
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def ball_start_move(right):
    ball_x_change = random.randrange(1,4)
    ball_y_change = random.randrange(1,4)

    if right == False:
        ball_x_change = -ball_x_change
        ball_x_change
        -ball_y_change
#defining game loop
def gameLoop ():
    gameExit = False
    gameOver = False
#pad and ball position
    pad1_x = 600
    pad1_y = 300
    pad1_x_change = 0
    pad1_y_change = 0

    pad2_x = 200
    pad2_y = 300
    pad2_x_change = 0
    pad2_y_change = 0

    ball_x = 400
    ball_y = 300
    ball_x_change = 0
    ball_y_change = 0

    while not gameExit:
#game over handler
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update ()
#restart or quit handler
            for event in pygame.event.get ():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop ()
#button controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pad1_x_change = -pad_move
                elif event.key == pygame.K_RIGHT:
                    pad1_x_change = pad_move

                elif event.key == pygame.K_UP:
                    pad1_y_change = -pad_move
                elif event.key == pygame.K_DOWN:
                    pad1_y_change = pad_move

                elif event.key == pygame.K_w:
                    pad2_y_change = -pad_move
                elif event.key == pygame.K_s:
                    pad2_y_change = pad_move

                elif event.key == pygame.K_a:
                    pad2_x_change = -pad_move
                elif event.key == pygame.K_d:
                    pad2_x_change = pad_move
                elif event.key == pygame.K_SPACE:
                    ball_x_change = random.randrange(1,4)
                    ball_y_change = -random.randrange(1,4)
                    #ball_start_move(True)

#button controls: stopping continuos movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pad1_x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pad1_y_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    pad2_x_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    pad2_y_change = 0
#ball boundary logic

        if ball_x >= display_width or ball_x < 0:
            gameOver = True
        if ball_y >= display_height or ball_y < 0:
            ball_y_change = -ball_y_change
        #ball - pad contact logic
        # if ball_x + ball_radius == pad1_x + pad_height and ball_y == pad1_y + pad_width:
        #     message_to_screen( "boing", red)
        #     pygame.display.update()
        #     time.sleep(2)

#summation of pad and ball movement
        pad1_x += pad1_x_change
        pad1_y += pad1_y_change
        pad2_x += pad2_x_change
        pad2_y += pad2_y_change
        ball_x += ball_x_change
        ball_y += ball_y_change

#Pad Boundaries
        if pad1_x + pad_width >= display_width and pad1_x_change > 0:
            pad1_x -= pad1_x_change
        if pad1_x <= display_width/2 and pad1_x_change < 0:
            pad1_x -= pad1_x_change
        if pad1_y + pad_height >= display_height and pad1_y_change > 0:
            pad1_y -= pad1_y_change
        if pad1_y <= 0 and pad1_y_change < 0:
            pad1_y -= pad1_y_change
            # message_to_screen( "boundary", red)
            # pygame.display.update()
            # time.sleep(2)
        if pad2_x <=0 and pad2_x_change < 0:
            pad2_x -= pad2_x_change
        if pad2_x >= display_width/2 and pad2_x_change > 0:
            pad2_x -= pad2_x_change
        if pad2_y + pad_height >= display_height and pad2_y_change > 0:
            pad2_y -= pad2_y_change
        if pad2_y <= 0 and pad2_y_change < 0:
            pad2_y -= pad2_y_change

        #ball - pad contact logic
        if ball_x + 1 in range(pad1_x - 1, pad1_x + pad_width + 1) and ball_y + 1 in range(pad1_y - 1, pad1_y + pad_height + 1) or ball_x + ball_radius + 1 in range(pad1_x - 1, pad1_x + pad_width + 1) and ball_y + ball_radius + 1 in range(pad1_y - 1, pad1_y + pad_height + 1):
            ball_x_change = -ball_x_change
            # message_to_screen( "boing", red)
            # pygame.display.update()
            # time.sleep(2)

        if ball_x - 1 in range(pad2_x + 1, pad2_x + pad_width) and ball_y - 1 in range(pad2_y + 1, pad2_y + pad_height + 1) or ball_x - ball_radius - 1 in range(pad2_x + 1, pad2_x + pad_width) and ball_y - ball_radius - 1 in range(pad2_y + 1, pad2_y + pad_height):
            ball_x_change = -ball_x_change

        #drawing the screen and objects
        gameDisplay.fill(blue)
        pygame.draw.rect(gameDisplay, white, [display_width/2,1,1,display_height])
        pygame.draw.rect(gameDisplay, white, [pad1_x,pad1_y,pad_width,pad_height])
        pygame.draw.rect(gameDisplay, white, [pad2_x,pad2_y,pad_width,pad_height])
        pygame.draw.circle(gameDisplay, green, [ball_x,ball_y],ball_radius,0)
        pygame.display.update()


        clock.tick(FPS)
#you lose text
    message_to_screen( "You lose", red)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()

    quit()

gameLoop ()
