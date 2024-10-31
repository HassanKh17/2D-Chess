
import pygame
import time
import random
import os
from pygame import image
import tkinter
from tkinter import*
pygame.init()


from Game import GameDesign


#screen dimensions
display_width = 600
display_height = 600
#Board width and height set to be a multiple of 8 so the board is symmetrical
board_height= 600
board_width= 600
#A chess board has 8 rows and 8 columns
dimensions=8
#This insures that the squares are of in right proportions as compared to the board's height and it's dimemsion
Squaresize= board_height//dimensions
IMAGES= {}
#colour constants for button backgrounds and screen backgrounds
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE=(0, 87, 128)
RED = (200,0,0)
GREEN = (0,200,0)
YELLOW = (255,255,0)
BROWN=(159,105,52)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (3, 166, 66)
LIGHT_YELLOW = (236, 240, 7)


#creates the screen area
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()     

#this creates our buttons parameters text, x position, y position, width of button, height of button,
#  colour, hover colour, function to run.
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #check position and draw the rectangle - takes the screen we set up gameDisplay

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
         action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("C:\\Users\lunap\Downloads\Gameshow-BzZ3.ttf",50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#this is for text boxes on the screens 
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# this is for large title texts    
def Ltext_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect() 


#this is for loading the images of sprites(pieces) 
def loadImages():
    pieces=['b_bishop','w_bishop','b_knight','w_knight','b_rook','w_rook','b_queen','w_queen','b_King','w_King','b_pawn','w_pawn']
    for r in pieces:
     IMAGES[r]=pygame.transform.scale(pygame.image.load( "C:\\Users\lunap\Downloads\Project\ChessEnv\Game\Pieces/"+ r +".png" ),(Squaresize,Squaresize))   


#this draws the actual chess board
def drawBoard(gameDisplay):
 colors=[pygame.Color("sandybrown"),pygame.Color("saddlebrown")]
 #r is short for row
 #c is short for column
 for r in range(dimensions):
  for c in range(dimensions):
    color = colors[(r+c)%2]
    #this draw the squares with alternating colors
    pygame.draw.rect(gameDisplay,color, pygame.Rect(c*Squaresize, r*Squaresize, Squaresize, Squaresize))


#this draw the pieces on the board
def drawPieces(gameDisplay,board):
    for r in range(dimensions):
        for c in range(dimensions):
            piece=board[r][c]
            #"--" refers to a position on board which is vacant
            if piece != "--":
                #this ensures the a piece occupies a whole square
                gameDisplay.blit(IMAGES[piece],pygame.Rect(c*Squaresize, r*Squaresize, Squaresize, Squaresize))

#This is to create the guiding pointer                     
def GuidingPointer(gameDisplay,gameScreen,SelectedSquare,validMoves):   
    if SelectedSquare !=():
        r,c = SelectedSquare
        if gameScreen.board[r][c][0]==("w" if gameScreen.WhiteToMove else "b"):
            #highlighting piece
            s= pygame.Surface((Squaresize,Squaresize))
            #This is to make it transparent
            s.set_alpha(100)
            s.fill(pygame.Color("darkblue"))
            gameDisplay.blit(s,(c*Squaresize,r*Squaresize))
            #This highlights the square which would be valid for a piece to be moved to
            s.fill(pygame.Color("green"))
            for move in validMoves:
                if move.startRow==r and move.startCol==c:
                    gameDisplay.blit(s,(move.endCol*Squaresize,move.endRow*Squaresize))  

#this combines the board, pieces and guiding pointer so they can be setup is ready
def drawGameState(gameDisplay,gameScreen,SelectedSquare,validMoves):
    drawBoard(gameDisplay)
    drawPieces(gameDisplay,gameScreen.board)
    GuidingPointer(gameDisplay,gameScreen,SelectedSquare,validMoves)     

#This is to draw small text messages
def drawText(gameDisplay,text):
    font=pygame.font.Font("C:\\Users\lunap\Downloads\Gameshow-BzZ3.ttf",50)
    textObject= font.render(text,0,pygame.Color("purple"))
    textLocation= pygame.Rect(0,0,display_width,display_height).move(display_width/2 - textObject.get_width()/2,display_height/2.5 - textObject.get_height()/0.5)
    gameDisplay.blit(textObject,textLocation)
#This is to draw larger text messages
def LdrawText(gameDisplay,text):
    font=pygame.font.Font("C:\\Users\lunap\Downloads\Gameshow-BzZ3.ttf",100)
    textObject= font.render(text,0,pygame.Color("purple"))
    textLocation= pygame.Rect(0,0,display_width,display_height).move(display_width/2 - textObject.get_width()/2,display_height/3 - textObject.get_height()/0.5)
    gameDisplay.blit(textObject,textLocation)

 


#This will contains the content of different info screens
def checkInfo():
    pass
def pawnInfo():
    pass 
def bishopInfo():
    pass
def rookInfo():
    pass 
def knightInfo():
    pass
def queenInfo():
    pass
def kingInfo():
    pass   


#Music/Sound:
promotionSound= pygame.mixer.Sound("C:\\Users\lunap\Downloads\Project\ChessEnv\Game\\promotionSound1.wav")
pieceSound= pygame.mixer.Sound("C:\\Users\lunap\Downloads\Project\ChessEnv\Game\\pieceSound.wav")
music= pygame.mixer.music.load("C:\\Users\lunap\Downloads\Project\ChessEnv\Game\\chessMusic.wav")
gameOverSound=pygame.mixer.Sound("C:\\Users\lunap\Downloads\Project\ChessEnv\Game\\gameOver.wav")


# main menu screen
def main_menu():

    inGame = True

    while inGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #set our screen background colour        
        backgroundimage= pygame.image.load ("C:\\Users\lunap\Downloads\chessback3.jpg").convert_alpha()
        gameDisplay.blit(backgroundimage,(0,0))

        #sets the text size and font for title 
        largeText = pygame.font.Font("C:\\Users\lunap\Downloads\Hokjesgeest-PDGB.ttf",45)
        TextSurf, TextRect = Ltext_objects("MAIN MENU", largeText)

         #sets the position of title text - i just changed the display_height divided by for vertical position
        pygame.draw.rect(gameDisplay, BROWN, pygame.Rect(80, 90, 440, 60))
        TextRect.center = ((display_width/2),(display_height/5))
        gameDisplay.blit(TextSurf, TextRect)

        #call button function to create the buttons
        button("PLAY",250,250,125,50,BROWN,BLUE,game_loop)
        button("INFO",250,350,125,50,BROWN,BLUE,information)
        button("QUIT",250,450,125,50,BROWN,BLUE,quitgame)

        pygame.display.update()
        clock.tick(15)               

#main game loop - change your main game play loop to a procedure so that it runs from the button. you may experience some variable undeclared issues here. As a temporary fix add keyword global before the variable name and then initialise
#e.g. global score
def game_loop():
    inGame = False
    play = True
    gameScreen=GameDesign.GameCondition()
    validMoves=gameScreen.getValidMoves()
    checkM=gameScreen.inCheckmate()
    moveMade= False
    #the images of sprites are loaded once
    loadImages()

    #this refers to the square selected by the user
    SelectedSquare=()
    #this refers to moves the player made so a move log can be created
    playerClicks=[]
    #gameover
    gameOver=False
    #the background music is loaded here
    pygame.mixer.music.play(-1) 
    

    while play:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #this allows pieces to be selected via mouse and then move to desired postion
            elif event.type== pygame.MOUSEBUTTONDOWN:
               if not gameOver:   
                Location= pygame.mouse.get_pos()
                col= Location[0]//Squaresize
                row= Location[1]//Squaresize
                if SelectedSquare==(row,col):
                    SelectedSquare=()
                    playerClicks=[]
                else:
                    SelectedSquare=(row,col)
                    playerClicks.append(SelectedSquare)

                #This is for selecting and moving a piece    
                if len(playerClicks)==2:
                    move=GameDesign.Move(playerClicks[0],playerClicks[1],gameScreen.board)
                    #This allows only valid moves
                    for i in range (len(validMoves)):
                        if move==validMoves[i]:
                         gameScreen.makeMove(validMoves[i])
                         #This checks if Pawn promotion is flagged
                         if move.PawnPromotion==True:

                          #This creates a choice box for promotion choice   
                          root = Tk()
                          choices = ['Queen', 'Knight', 'Bishop','Rook']
                          variable = StringVar(root)
                          variable.set('Choices')
                          w = OptionMenu(root, variable, *choices)
                          w.pack()   
                          root.mainloop()
                          #This checks which piece type the user choose           
                          if variable.get()=="Queen":
                           gameScreen.board[row][col]=move.pieceMoved[0]+"_queen"
                          elif variable.get()=="Rook":
                           gameScreen.board[row][col]=move.pieceMoved[0]+"_rook" 
                          elif variable.get()=="Knight":
                           gameScreen.board[row][col]=move.pieceMoved[0]+"_knight"
                          elif variable.get()=="Bishop":
                           gameScreen.board[row][col]=move.pieceMoved[0]+"_bishop" 
                          moveMade=True
                          promotionSound.play()
                          SelectedSquare=()
                          playerClicks=[]
                         else:
                           moveMade=True
                           SelectedSquare=()
                           playerClicks=[]
                           pieceSound.play()
 
                   
                    if not moveMade:
                        playerClicks=[SelectedSquare]  
            #key handlers
            elif event.type == pygame.KEYDOWN:
                #will undo the move when z is pressed
                if event.key == pygame.K_z:
                    gameScreen.undoMove()
                    moveMade=True
        if moveMade:
             validMoves=gameScreen.getValidMoves()
             moveMade=False   

        #This is the background behind the board               
        backgroundBoard=pygame.image.load ("C:\\Users\lunap\Downloads\\backgroundDesign.jpg").convert_alpha()
        gameDisplay.blit(backgroundBoard,(0,0))
        gameDisplay.fill(BROWN)
        #making the game screen
        drawGameState(gameDisplay,gameScreen,SelectedSquare,validMoves)  
        #This initiates the gameover screen when game is won
        if gameScreen.checkMate:
            gameOver=True
            pygame.mixer.music.stop()
            gameDisplay.fill("BLACK")
            button("MAIN MENU",175,250,275,50,BROWN,BRIGHT_GREEN,main_menu)
            button("PLAY AGAIN",175,350,275,50,BROWN,BLUE,game_loop)
            button("QUIT",175,450,275,50,BROWN,BRIGHT_RED,quitgame)
            LdrawText(gameDisplay,"Game Over")
            gameOverSound.play()
            if gameScreen.WhiteToMove:
                drawText(gameDisplay,"Black wins by checkmate")

            else:
                drawText(gameDisplay,"White wins by checkmate")

        elif gameScreen.stalleMate:
            gameOver=True
            pygame.mixer.music.stop()
            gameDisplay.fill("BLACK")
            button("MAIN MENU",175,250,275,50,BROWN,BRIGHT_GREEN,main_menu)
            button("PLAY AGAIN",175,350,275,50,BROWN,BLUE,game_loop)
            button("QUIT",175,450,275,50,BROWN,BRIGHT_RED,quitgame)
            LdrawText(gameDisplay,"Game Over")
            drawText(gameDisplay,"Game Drawn by Stalemate")
        pygame.display.update()
        clock.tick(15)                      


def information():
    #we may use these variables for a back button.
    inGame = False
    play = False
    info = True

    while info:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        background=pygame.image.load ("C:\\Users\lunap\Downloads\\chessback3.jpg").convert_alpha()
        gameDisplay.blit(background,(0,0)) 
        largeText = pygame.font.Font("C:\\Users\lunap\Downloads\Hokjesgeest-PDGB.ttf",30)
        TextSurf, TextRect = Ltext_objects("INFORMATION", largeText)
        #sets the position of title text - i just changed the display_height divided by for vertical position
        pygame.draw.rect(gameDisplay, BROWN, pygame.Rect(125, 25, 350, 60))
        TextRect.center = ((display_width/1.99),(display_height/10.5))
        gameDisplay.blit(TextSurf, TextRect) 

        #Buttons on the info screen
        button("CHECKMATE",150,120,300,50,BROWN,BLUE,checkInfo)     
        button("KING",50,200,200,50,BROWN,BLUE,kingInfo)
        button("QUEEN",350,200,200,50,BROWN,BLUE,queenInfo)
        button("KNIGHT",50,300,200,50,BROWN,BLUE,knightInfo)
        button("ROOK",50,400,200,50,BROWN,BLUE,rookInfo)
        button("BISHOP",350,300,200,50,BROWN,BLUE,bishopInfo)
        button("PAWN",350,400,200,50,BROWN,BLUE,pawnInfo)
        button("MENU",50,500,150,50,BRIGHT_GREEN,GREEN,main_menu)
        button("PLAY",225,500,150,50,LIGHT_YELLOW,YELLOW,game_loop)
        button("QUIT",400,500,150,50,RED,BRIGHT_RED,quitgame)

        pygame.display.update()
        clock.tick(15)

    
def quitgame():
    pygame.quit()
    quit()
main_menu()    
game_loop()
