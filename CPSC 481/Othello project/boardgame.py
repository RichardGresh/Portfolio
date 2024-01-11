from operator import truediv
from queue import Empty
from random import betavariate
from this import d
import pygame
import game
import os
import math
import time
from numpy import *
import copy

class othello_board(object):
    
    def __init__(self, displayWidth, displayHeight, game):
        self.surface = pygame.display.set_mode((displayWidth,displayHeight))
        self.square1color = (60, 179, 113)
        self.square2color = (28, 155, 188)
        self.squareSize = 800//8
        self._game = game
        self.select = { 'piece': -1, 'y': -1, 'x': -1 }
        self.target = { 'piece': -1, 'y': -1, 'x': -1 }
        self.IMAGES = {}
        self.squaresize = 800//8
        self.pack = 'images'
        self.load_Images(self.pack)
        self.valid_moves = []
        self.user_clicks = 0
        self.playercolor = 1
        self._ai = False
        self.game_end = False
        self.noact1 = False
        self.noact2 = False
        self.scoreb = 0
        self.scorew = 0
        
        
        
    def process(self):
        
        self.player_move()
        self.validmoveplacement() 
        
    def draw(self):
        for x in range(0,8):
            for y in range(0,8):
                if(y % 2 == 0 and x %2 == 0):
                    pygame.draw.rect(self.surface, self.square1color, pygame.Rect(y * self.squareSize , x * self.squareSize , self.squareSize , self.squareSize ))
                elif(y % 2 == 0 and x %2 == 1):
                    pygame.draw.rect(self.surface, self.square2color, pygame.Rect(y * self.squareSize , x * self.squareSize , self.squareSize , self.squareSize ))
                elif (y %2 == 1 and x%2 == 1):
                    pygame.draw.rect(self.surface, self.square1color, pygame.Rect(y * self.squareSize , x * self.squareSize , self.squareSize , self.squareSize ))
                
                elif (y %2 == 1 and x%2 == 0):
                    pygame.draw.rect(self.surface, self.square2color, pygame.Rect(y * self.squareSize , x * self.squareSize , self.squareSize , self.squareSize ))
        self.validmoveplacement() 
        self.drawpieces()
        self.drawvalid()
        
        
    
    
    def load_Images(self, imgpack):
        pieces = [1,2]
        for piece in pieces:
            self.IMAGES[piece] = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), imgpack, str(piece) + '.png')).convert_alpha(), (self.squareSize, self.squareSize))
            
        self.IMAGES['ring'] = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), imgpack, 'ring' + '.png' )).convert_alpha(), (self.squaresize, self.squaresize ))
                
            
    
    def drawpieces(self):
        self._game.board
        for x in range(8):
            for y in range(8):
                piece = self._game.board[y][x]
                if piece != 0 and (x,y) != (self.select['x'], self.select['y']):
                    self.surface.blit(self.IMAGES[piece], pygame.Rect(x*self.squareSize, y*self.squareSize, self.squareSize, self.squareSize))
                    
                    
    def validmoveplacement(self):
        self.valid_moves = self._game.movevalidation(self._game.player)
        #print(self.valid_moves)
        
    def drawvalid(self):
        for moves in self.valid_moves:
            self.surface.blit(self.IMAGES['ring'], pygame.Rect(moves[1]*self.squaresize, moves[0]*self.squaresize, self.squareSize, self.squareSize))
        
    
    def player_move(self):
        if self._game.player == 1:
            select_x, select_y = pygame.mouse.get_pos()
            select_x = math.floor(select_x / self.squaresize)
            select_y = math.floor(select_y/ self.squaresize)
            if select_x < 8 and select_y < 8:
                piece = self._game.board[select_y][select_x]
            else:
                piece = -1
        
            if pygame.mouse.get_pressed()[0] == 1:
                self._game.movevalidation(1)
               # print(self._game.board)
                pressed_x = select_y
                pressed_y = select_x
                #print(pressed_x)
                #print(pressed_y)
                #print("button pressed")
                #print(piece)
                if ((pressed_x, pressed_y) in self.valid_moves):
                    self._game.moveifvalid((pressed_x,pressed_y), self._game.player)
                    if self._game.player == 1:
                        self._game.player = 2
        elif self._game.player == 2:
            best_move = self.Alpha_beta(self._game)
            self._game.movevalidation(2)
            self._game.aimake_move(best_move, 2)
            self._game.player = 1
            print("ai over")
                
            #means player left clicked
    def endgame(self):
        #print(self.valid_moves)
        if self._game.player == 1 and len(self.valid_moves) == 0 and self.noact1 == False:
            self.noact1 = True
            self._game.player = 2
            #print("skip")
        if self._game.player == 2 and len(self.valid_moves) == 0 and self.noact2 == False:
            self.noact2 = True
            self._game.player = 1
            #print('skip')
        if len(self.valid_moves) != 0:
            self.noact1 = False
            self.noact2 = False
        if self.noact1 == True and self.noact2 == True:
            #print("endgame")
            self.scoreb = self._game.bscore
            self.scorew = self._game.wscore
            return True
        else:
            return False
    
    def Alpha_beta(self, game, alpha = -math.inf, beta = math.inf, d = 4 ):
        cuttoff_test = lambda depth: depth == 0
        eval_fn = lambda : game.advanced_evaluation(game.board)
        best_score = -math.inf
        best_move = None
        depth = d
        
        
        for x in game.actions(game.player):
            
            copyboard = copy.deepcopy(game.board)
            game.aimake_move(x,game.player)
            print(copyboard)
            value = self.min_value(alpha, beta, depth - 1, game, eval_fn)
            game.board = copyboard
            print(game.board)
            #time.sleep(30)
            game.scoreupkeep()
            print(value)
            if(value >= best_score):
                best_move = x
                best_score = value
                print(best_score)
                print(best_move)
        if game.player == 1:
            game.player = 2
        print("happened")
        print(game.board)
        print(best_move)
        return best_move
        
    def min_value(self, alpha, beta, depth, game, eval_fn):
        if depth == 0:
            return -eval_fn()
        best_min_score = math.inf
        if(game.player == 2):
            game.player = 1
            
        for move in game.actions(game.player):
            boardcopy = copy.deepcopy(game.board)
            game.aimake_move(move,game.player)
            best_min_score = min(best_min_score, self.max_value(alpha, beta, depth - 1, game, eval_fn))
            game.board = boardcopy
            game.scoreupkeep()
            beta = min(beta, best_min_score)
            if (beta <= alpha):
                #print("best_max_score: ", best_min_score)
                return best_min_score
        return best_min_score
        
    def max_value(self, alpha, beta, depth, game, eval_fn):
        if depth == 0:
            return -eval_fn()
        best_max_score = -math.inf
        if game.player == 1:
            game.player = 2
        for move in game.actions(game.player):
            boardcopy = copy.deepcopy(game.board)
            game.aimake_move(move, game.player)
            best_max_score = max(best_max_score, self.min_value(alpha, beta, depth - 1, game, eval_fn))
            game.board = boardcopy
            game.scoreupkeep()
            alpha = max(alpha, best_max_score)
            if (beta <= alpha):
                return best_max_score
        #print("best_max_score: ", best_max_score)
        return best_max_score
                
                
            
            
        
        
        
            
            
