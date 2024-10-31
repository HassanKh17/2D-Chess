import pygame
pygame.mixer.init()
checkSound= pygame.mixer.Sound("C:\\Users\lunap\Downloads\\checkMusic.wav")
class GameCondition():
    def __init__(self):
        #the board is a 2d array of 8*8 as a chess board has 8 columns and 8 rows
        #the first letters refers to the piece being either black or white
        #"--" represent vacants positions on the board
        self.board=[
              ["b_rook","b_knight","b_bishop","b_queen","b_King","b_bishop","b_knight","b_rook"],
              ["b_pawn","b_pawn","b_pawn","b_pawn","b_pawn","b_pawn","b_pawn","b_pawn"],
              ["--","--","--","--","--","--","--","--"],
              ["--","--","--","--","--","--","--","--"],
              ["--","--","--","--","--","--","--","--"],
              ["--","--","--","--","--","--","--","--"],
              ["w_pawn","w_pawn","w_pawn","w_pawn","w_pawn","w_pawn","w_pawn","w_pawn"],
              ["w_rook","w_knight","w_bishop","w_queen","w_King","w_bishop","w_knight","w_rook"]
        ]
        #this is to allows white pieces to move when true
        self.WhiteToMove= True
        #this keeps track of the moves made by the player
        self.moveLog=[]
        self.WhiteKingLocation=(7,4)
        self.BlackKingLocation=(0,4)
        self.checkMate=False
        self.stalleMate=False


        #this allows the pieces to move on the board
    #This takes parameter to make the move on the piece    
    def makeMove(self,move):
        self.board[move.startRow][move.startCol]="--"
        self.board[move.endRow][move.endCol]=move.pieceMoved
        self.moveLog.append(move)
        #This is to switch turns
        self.WhiteToMove= not self.WhiteToMove
        #This is to update the king's to keep track of checkmate
        if move.pieceMoved == "w_King":
            self.WhiteKingLocation=(move.endRow,move.endCol)
        elif move.pieceMoved == "b_King":
            self.BlackKingLocation=(move.endRow,move.endCol)           


    #this will undo the last move    
    def undoMove(self):
        if len(self.moveLog)!=0:
            move=self.moveLog.pop()
            self.board[move.startRow][move.startCol]= move.pieceMoved
            self.board[move.endRow][move.endCol]= move.pieceCaptured
            #This is to switch turns back
            self.WhiteToMove = not self.WhiteToMove
            #This is to update the king's to keep track of checkmate
            if move.pieceMoved == "w_King":
             self.WhiteKingLocation=(move.startRow,move.startCol)
            elif move.pieceMoved == "b_King":
             self.BlackKingLocation=(move.startRow,move.startCol) 



    #all moves considering checks        
    def getValidMoves(self):    
        #This takes all possible moves for all pieces   
        moves= self.getAllPossibleMoves()
        for i in range(len(moves)-1,-1,-1):
            self.makeMove(moves[i])

            self.WhiteToMove= not self.WhiteToMove
            #Checks if in checkmate position
            if self.inCheckmate():   
            #This removes all other moves which  would cause the game to stay in checkmate 
               moves.remove(moves[i]) 
            #This changes the turn back   
            self.WhiteToMove= not self.WhiteToMove
            self.undoMove()
            #checks if no valid moves can be made
        if len(moves)==0:
            #if no moves can be made and game in checkmate position then game end by checkmate
            if self.inCheckmate():
                self.checkMate=True
             #if no moves can be made and game isn't in checkmate position then game end by stallemate
            else:
                self.stalleMate=True         
        else:
              self.checkMate=False  
              self.stalleMate=False       

        return moves


#This checks if the current player is under check or not
    def inCheckmate(self):
        if self.WhiteToMove:
            return self.squareUnderAttack(self.WhiteKingLocation[0],self.WhiteKingLocation[1])
        
            
        else:
            return self.squareUnderAttack(self.BlackKingLocation[0],self.BlackKingLocation[1]) 


    #This checks if the enemy can attack a square  
    def squareUnderAttack(self, r, c):
        self.WhiteToMove= not self.WhiteToMove
       #This generate all the possible moves for the opponent  
        opponentMoves=self.getAllPossibleMoves() 
        self.WhiteToMove= not self.WhiteToMove
        for move in opponentMoves:
            if move.endRow==r and move.endCol==c:
                return True
        return False        


    #all moves without considering checks
    def getAllPossibleMoves(self):
        moves=[]
        for r in range(len(self.board)):
            for c in range (len(self.board[r])):
                turn= self.board[r][c][0]
                if (turn== "w" and self.WhiteToMove) or (turn== "b" and not self.WhiteToMove):
                    #This determines the type of piece the move is being made on
                    piece= self.board[r][c][2]
                    if piece == "p":
                        self.getPawnMoves(r,c,moves)
                    elif piece == "r" :
                        self.getRookMoves(r,c,moves)
                    elif piece == "b" :
                        self.getBishopMoves(r,c,moves)
                    elif piece == "k" :
                        self.getKnightMoves(r,c,moves)
                    elif piece == "q" :
                        self.getQueenMoves(r,c,moves)
                    elif piece == "K" :
                        self.getKingMoves(r,c,moves)  
        return moves    


    #This defines the moves a pawn can make             
    def getPawnMoves(self,r,c,moves):
        #Moves for a white pawn
        if self.WhiteToMove:
            if self.board[r-1][c]=="--":
                moves.append(Move((r,c),(r-1,c),self.board))
                if r==6 and self.board[r-2][c]=="--":
                      moves.append(Move((r,c),(r-2,c),self.board))
            #For capturing opponet's piece          
            if c-1 >= 0:
                if self.board[r-1][c-1][0]=="b":
                    moves.append(Move((r,c),(r-1,c-1),self.board))
            if c+1 <= 7:
                if self.board[r-1][c+1][0]=="b":
                    moves.append(Move((r,c),(r-1,c+1),self.board))
        #Moves for a black pawn              
        else:     
            if self.board[r+1][c]=="--":
                moves.append(Move((r,c),(r+1,c),self.board))
                if r==1 and self.board[r+2][c]=="--":
                      moves.append(Move((r,c),(r+2,c),self.board))
            #For capturing opponet's piece          
            if c-1 >= 0:
                if self.board[r+1][c-1][0]=="w":
                    moves.append(Move((r,c),(r+1,c-1),self.board))
            if c+1 <= 7:
                if self.board[r+1][c+1][0]=="w":
                    moves.append(Move((r,c),(r+1,c+1),self.board))                                



    def getRookMoves(self,r,c,moves):
        #This refers to directions up,left,down,right respectively
        directions=((-1,0),(0,-1),(1,0),(0,1))
        #This indicates the enemy piece by checking it's color
        enemyColor="b" if self.WhiteToMove else "w"
        for d in directions:
            for i in range (1,8):
                endRow= r+d[0]*i
                endCol= c+d[1]*i
                if 0 <= endRow < 8 and 0<= endCol<8:#This ensures that piece stays on board
                 endPiece=self.board[endRow][endCol]
                 if endPiece=="--":#Moves the rook to the square if it's already empty
                     moves.append(Move((r,c),(endRow,endCol),self.board))
                 elif endPiece[0]== enemyColor:#Captures the piece on the square if it belongs to enemy
                     moves.append(Move((r,c),(endRow,endCol),self.board))  
                     #This is to ensure it doesn't jump over the enemy piece
                     break
                 else:
                     #This is to ensure it doesn't jump over the friendly piece
                     break
                else:
                    #This is to ensure it doesn't go off the board
                  break   



    def getBishopMoves(self,r,c,moves):
        #This refers to directions it can move diagonally
        directions=((-1,-1),(-1,1),(1,-1),(1,1))
        #This indicates the enemy piece by checking it's color
        enemyColor="b" if self.WhiteToMove else "w"
        for d in directions:
            for i in range (1,8):
                endRow= r+d[0]*i
                endCol= c+d[1]*i
                if 0 <= endRow < 8 and 0<= endCol<8:#This ensures that piece stays on board
                 endPiece=self.board[endRow][endCol]
                 if endPiece=="--":#Moves the rook to the square if it's already empty
                     moves.append(Move((r,c),(endRow,endCol),self.board))
                 elif endPiece[0]== enemyColor:#Captures the piece on the square if it belongs to enemy
                     moves.append(Move((r,c),(endRow,endCol),self.board))  
                     #This is to ensure it doesn't jump over the enemy piece
                     break
                 else:
                     #This is to ensure it doesn't jump over the friendly piece
                     break
                else:
                    #This is to ensure it doesn't go off the board
                    break         
        


    def getKnightMoves(self,r,c,moves):
        #This refers to directions it can move diagonally
        directions=((-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1))
        #This indicates the enemy piece by checking it's color
        ownColor="w" if self.WhiteToMove else "b"
        for move in directions:
                endRow= r + move[0]
                endCol= c + move[1]
                if 0 <= endRow <=7 and 0<= endCol<=7:#This ensures that piece stays on board
                  endPiece=self.board[endRow][endCol]
        #Captures the piece on the square if it belongs to enemy or move to a square if not occupied by own piece
                  if endPiece[0]!= ownColor:
                    moves.append(Move((r,c),(endRow,endCol),self.board))    


    def getQueenMoves(self,r,c,moves):
        #The queen can move like both a bishop or a rook
        self.getBishopMoves(r,c,moves)
        self.getRookMoves(r,c,moves)  


    def getKingMoves(self,r,c,moves):
        directions=((-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)) 
        #This indicates the enemy piece by checking it's color
        OwnColor="w" if self.WhiteToMove else "b"
        for d in directions:
         for i in range(1,8):
                endRow= r + d[0]*i
                endCol= c + d[1]*i
                if 0 <= endRow < 8 and 0<= endCol<8:#This ensures that piece stays on board
                  endPiece=self.board[endRow][endCol]
                  if endPiece[0]!= OwnColor:#Captures the piece on the square if it belongs to enemy
                    moves.append(Move((r,c),(endRow,endCol),self.board))  
                    #This is to ensure it doesn't jump over the enemy piece
                    break
                  else:
                     #This is to ensure it doesn't jump over the friendly piece
                     break
                else:
                    #This is to ensure it doesn't go off the board
                    break                          
        


class Move():
    rankToRows= {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}  
    rowsToRanks={v:k for k, v in rankToRows.items()} 
    filesToCols={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7} 
    colsToFiles={v:k for k, v in filesToCols.items()}   
    def __init__(self,StartingSquare,EndSquare,board):
        self.startRow= StartingSquare[0]
        self.startCol= StartingSquare[1] 
        self.endRow= EndSquare[0]
        self.endCol=EndSquare[1]
        #indicates the position the board is moved to
        self.pieceMoved=board[self.startRow][self.startCol]
        #this allows pieces to be captured
        self.pieceCaptured=board[self.endRow][self.endCol]
        self.moveID= self.startRow*1000 + self.startCol * 100 + self.endRow*10 + self.endCol

        #This is for pawn promotion
        self.PawnPromotion=False
        if(self.pieceMoved=="w_pawn" and self.endRow==0) or (self.pieceMoved=="b_pawn" and self.endRow==7):
             self.PawnPromotion=True


    #Overriding the equal methods    
    def __eq__(self, other):
        if isinstance(other,Move):
           return self.moveID==other.moveID
        return False      

        #this displays the move log on the side in chess notation
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self,r ,c) :
        return self.colsToFiles[c]+self.rowsToRanks[r]
    


           