#Part1
import pygame,sys
import time
import random

pygame.init()

white = (255,255,255)
black = (100,0,0)
red = (255,0,0)
window_width = 800
window_height = 600


gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('slither')

#Part2
clock = pygame.time.Clock()     #event based on timings  like if we need to refresh ur screen in particular interval of time
FPS = 10
blockSize = 20


'''
sizeGrd = window_width // blockSize
row = 0
col = 0
for nextline in range(sizeGrd):
'''

def myquit():
    ''' Self explanatory '''
    pygame.quit()
    sys.exit(0)

font = pygame.font.SysFont(None, 25, bold=True)

def drawGrid():

	sizeGrd = window_width // blockSize


#PArt3
def snake(blockSize, snakelist):
    #x = 250 - (segment_width + segment_margin) * i
    for size in snakelist:
        pygame.draw.rect(gameDisplay, black,[size[0],size[1],blockSize,blockSize],2)   #2 is width   [x,y,height,width of the snake block]    

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/2, window_height/2])

#PArt4   

def gameLoop():
    gameExit = False           #stop the entire game
    gameOver = False           #snake was killed but player can still start the game
    lead_x = window_width/2      #start x position of the snake 
    lead_y = window_height/2    #start y positon of the snake 
    change_pixels_of_x = 0      #change in snake position in x axis
    change_pixels_of_y = 0      #change in snake position in y axis
    snakelist = []
    snakeLength = 1
    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

    

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press c to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:     #KEYDOWN is a class where all the events are present for various movement
                    if event.key == pygame.K_q:     #quit
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:     #continue
                        gameLoop()

#Logic1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                leftArrow = event.key == pygame.K_LEFT

                rightArrow = event.key == pygame.K_RIGHT

                upArrow = event.key == pygame.K_UP

                downArrow = event.key == pygame.K_DOWN

                if leftArrow:
                    change_pixels_of_x = -blockSize      #change in ;osition in x Axis
                    change_pixels_of_y = 0

                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = 0

                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = 0
                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = 0
                
#logic2   Boundary check
            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True
        #Update the coordinates with changed position
        lead_x += change_pixels_of_x

        lead_y += change_pixels_of_y

        gameDisplay.fill(white)

        AppleThickness = 20
#Logic3   Food spawn
        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(gameDisplay, red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])
        #increassse size of snake 
        allspriteslist = []              #snake head
        allspriteslist.append(lead_x)    #append x and y co ordinates
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)
        if len(snakelist) > snakeLength:
            del snakelist[0]
        #when snake hits itself
        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True
#Logic4 draw snake
        snake(blockSize, snakelist)

        pygame.display.update()
       
#Logic5   check apple and snake collision
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:

            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:

                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0

                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

                snakeLength += 1



             

        clock.tick(FPS)       #Shows No of Frames per second



    pygame.quit()

    quit()

gameLoop()