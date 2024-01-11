
from this import d
from typing import TYPE_CHECKING
from copy import deepcopy
import math

class Game():
    def __init__(self):
        self.turn = 1
        self.player = 1
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0,],
                      [0, 0, 0, 0, 0, 0, 0, 0,],
                      [0, 0, 0, 0, 0, 0, 0, 0,],
                      [0, 0, 0, 2, 1, 0, 0, 0,],
                      [0, 0, 0, 1, 2, 0, 0, 0,],
                      [0, 0, 0, 0, 0, 0, 0, 0,],
                      [0, 0, 0, 0, 0, 0, 0, 0,],
                      [0, 0, 0, 0, 0, 0, 0, 0,],
                      ]
        self.valid_moves = []
        self.bscore = 0
        self.wscore = 0
    def movevalidation(self, color):
        #first we need to be able to read the board.
        moves = []
        if color == 1:
            other = 2
        elif color == 2:
            other = 1
            
        for x in range(8):
            for y in range(8):
                #print('x: ', x, "y:", y)
                #print(self.board[x][y])
                if self.board[x][y] == color:
                    #print("i")
                    #print(x)
                    #print(y)
                    moves = moves + self.lookup(x,y,color)
        moves = list(set(moves))
        self.valid_moves = moves
        return moves
    def moveifvalid(self, move, color):
        if move in self.valid_moves:
            print("move if valid")
           # print(color)
            #print(move)
            self.board[move[0]][move[1]] = color
            #print(move)
            print(move[1])
            print(move[0])
            print(self.board[move[1]][move[0]])
            for i in range(1,9):
                self.flip(i,move,color)
            if self.player == 1:
                self.player = 2
            elif self.player == 2:
                self.player = 1
        self.scoreupkeep()
        
                    
                    
    def lookup(self, row, column, color):
        places = []
        if color == 1:
            opp = 2
        if color == 2:
            opp = 1
        if row <0 or row > 7 or column < 0 or column > 7:
            return places
        for (x,y) in [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]:
            
            #print(row)
            #print(column)
            pos = self.check_direction(row, column, x, y, opp)
            if pos:
                places.append(pos)
        return places          
                    
    def actions(self,color):
        valid_moves = self.movevalidation(color)
        return valid_moves
    
    def check_direction(self, row,column, x, y, other):
        i = row + x
        j = column + y
        if (i >= 0 and j >= 0 and i < 8 and j < 8 and self.board[i][j] == other):
            i += x
            j += y
            while (i >= 0 and j >= 0 and i < 8 and j < 8 and self.board[i][j] == other):
                i += x
                j += y
            if (i >= 0 and j >= 0 and i < 8 and j <8 and self.board[i][j] == 0):
                return(i,j)
    def update(self):
        pass
        #self.movevalidation(1)
        
    def flip(self, direction, position, color):
        #this will flip captured pieces of a given color to the other one.
        #print(direction)
        #print(position)
        #print(color)
        if direction == 1:
            #north
            row_inc = -1
            col_inc = 0
        if direction == 2:
            #northeast
            row_inc = -1
            col_inc = 1
        if direction == 3:
            # east
            row_inc = 0
            col_inc = 1
        if direction == 4:
            #southeast
            row_inc = 1
            col_inc = 1
        if direction == 5:
            #south
            row_inc = 1
            col_inc = 0
        if direction == 6:
            #south west
            row_inc = 1
            col_inc = -1
        if direction == 7:
            #west
            row_inc = 0
            col_inc = -1
        if direction == 8:
            # northwest
            row_inc = -1
            col_inc = -1
        flipped = [] #positions to be flipped
        i = position[1] + row_inc
        j = position[0] + col_inc
        if color == 1:
            other = 2
        elif color == 2:
            other = 1
        #print(color)
        if j in range(8) and i in range(8) and self.board[j][i] == other:
            flipped = flipped + [(j,i)]
            i = i + row_inc
            j = j + col_inc
            while j in range(8) and i in range(8) and self.board[j][i] == other:
                flipped = flipped + [(j,i)]
                i = i + row_inc
                j = j + col_inc
            if j in range(8) and i in range(8) and self.board[j][i] == color:
                for pos in flipped:
                    #print(flipped)
                    self.board[pos[0]][pos[1]] = color
                    
    
        #print(flipped)    
    def scoreupkeep(self):
        self.bscore = 0
        self.wscore = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 1:
                    self.bscore = self.bscore + 1
                elif self.board[x][y] == 2:
                    self.wscore = self.wscore + 1
        #print("black players score: ", self.bscore)
        #print("white player score: ", self.wscore)
    
    def advanced_evaluation(self, state):
        evaluation = 0
        board2 =  [ 
            [1, -0.25, 0.1, 0.05, 0.05, 0.1, -0.25, 1],
            [-0.25, -0.25, 0.01, 0.01, 0.01, 0.01, -0.25, -0.25],
            [0.1, 0.01, 0.05, 0.02, 0.02, 0.05, 0.01, 0.1],
            [0.05, 0.01, 0.02, 0.01,0.01,0.02,0.01,0.05],
            [0.05, 0.01, 0.02, 0.01,0.01,0.02,0.01,0.05],
            [0.1, 0.01, 0.05, 0.02, 0.02, 0.05, 0.01, 0.1],
            [-0.25, -0.25, 0.01, 0.01, 0.01, 0.01, -0.25, -0.25],
            [1, -0.25, 0.1, 0.05, 0.05, 0.1, -0.25,1 ]
        ]

        for x in range(0,8):
            for y in range(0,8):

                if (state[x][y] == 2):
                    evaluation += board2[x][y]
                elif (state[x][y] == 1):
                    evaluation -= board2[x][y]
        return evaluation
    def aimake_move(self,move,color):
        if move in self.valid_moves:
            #print("move if valid")
           # print(color)
            #print(move)
            self.board[move[0]][move[1]] = color
            #print(move)
            #print(move[1])
            #print(move[0])
            #print(self.board[move[1]][move[0]])
            for i in range(1,9):
                self.flip(i,move,color)
        else:
            print("how")
        self.scoreupkeep()
        