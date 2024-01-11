# Richard Gresham
# CPSC 481-05
# 2022 - 04 - 26
#rgresham@csu.fullerton.edu
# Othello program

import os
import json
import datetime
import pygame
import random
import boardgame
import game

class Scene:
    """This is the scene class"""
    
    def __init__(self, screen, background_color):
        self._is_valid = True
        self._frame_rate = 60
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background_color = background_color
        self._background.fill(self._background_color)
        self._restart = False
    
    def is_valid(self):
        """This returns if the key is valid"""
        return self._is_valid

    def frame_rate(self):
        """This returns my framerate"""
        return self._frame_rate

    def draw(self):
        """This draws my pygame"""
        self._screen.blit(self._background, (0, 0))

    def start(self, scoreb, scorew):
        """This is the starting data"""
        print("scene start")

    def end(self):
        """This is the end function of my class"""
        i = [0, 0, self._restart]
        return i

    def update(self):
        """This updates the display"""
        pygame.display.update()

    def process_event(self, event):
        """This processes keyboard movement"""
        if event.type == pygame.QUIT:
            print("exitgame")
            self._is_valid = False    
class TitleScene(Scene):
    """This is the TitleScene Class"""

    def __init__(self, screen, background_color, title, title_color, title_size):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        self._title_size = title_size
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, title_color)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w / 2, h / 4))

    def draw(self):
        """This draws my pygame"""
        super().draw()
        self._screen.blit(self._title, self._title_pos)

    def process_event(self, event):
        """This updates the display"""
        if event.type == pygame.KEYDOWN:
            print("pressed any key")
            self._is_valid = False


class BlinkingTitleScene(TitleScene):
    """This is the BlinkingTitleScene Class"""

    def __init__(self, screen, background_color, title, title_color, title_size):
        """This is my initialization of Class"""
        super().__init__(screen, background_color, title, title_color, title_size)
        self._title_complement_color = (
            255 - title_color[0],
            255 - title_color[1],
            255 - title_color[2],
        )
        self._counter = 0
        self._message = title
        self.color_speed = 1
        self.color_direction = [-1, 1, -1]
        self.def_color = [120, 120, 240]
        self.minimum_color = 0
        self.maximum_color = 255

    def update(self):
        """This updates the display"""
        super().update()
        self.color_change()

    def draw(self):
        """This draws my pygame"""
        title_font = pygame.font.Font(pygame.font.get_default_font(), self._title_size)
        self._title = title_font.render(self._message, True, self.def_color)
        self._screen.blit(self._title, self._title_pos)
        super().draw()
        self.instructions()

    def instructions(self):
        """This is user instruction"""
        text_font = pygame.font.Font(
            pygame.font.get_default_font(), self._title_size - 5
        )
        instructionlist = [
            "Instructions to Play: ",
            "Each piece played must be laid adjacent ",
            "to an opponents piece so that the opponent's",
            "piece or row of opponent's pieces is flanked",
            "by a piece and another piece of the players",
            "colour. All of the opponents pieces between these",
            "two pieces are captured and turned over to",
            "match the players colour. The game ends",
            " when no legal move can be made, or when the",
            "board is full, winner is",
            "chosen by whoever has the most points.",
        ]
        locationlist = [(400, 250), (400, 300), (400, 350), (400, 400), (400, 450), (400,500), (400,550), (400,600), (400,650), (400,700), (400,750)]
        for i in range(0, len(instructionlist)):
            instructions1 = text_font.render(instructionlist[i], True, self.def_color)
            instructions1_pos = instructions1.get_rect(center=locationlist[i])
            self._screen.blit(instructions1, instructions1_pos)

    def color_change(self):
        """This causes color change"""
        for i in range(3):
            self.def_color[i] += self.color_speed * self.color_direction[i]
            if (
                self.def_color[i] >= self.maximum_color
                or self.def_color[i] <= self.minimum_color
            ):
                self.color_direction[i] *= -1
    
    
    
    
class GameScene(Scene):
    def __init__(self,screen, background_color):
        super().__init__(screen,background_color)
        (w,h) = self._screen.get_size()
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self._game = game.Game()
        self._board = boardgame.othello_board(800,800,self._game)
        print("in new scene")
        self._blackscore = 0
        self._whitescore = 0
        self._restart = False
        
    
    def start(self,scoreb, scorew):
        print("scene started long ago")
        
    def draw(self):
        super().draw()
        self._board.draw()
        
    
    
    
    def process_event(self,event):
        super().process_event(event)
        self._board.process()
        self._board.validmoveplacement()
        final = self._board.endgame()
        if final == True:
            self._whitescore = self._board.scorew
            self._blackscore = self._board.scoreb
            self._is_valid = False
        
    def end(self):
        i = [self._blackscore, self._whitescore, self._restart]
        return i    
    def update(self):
        super().update()
        #self._game.update()
        
class EndScene(Scene):
    """This is the EndScene Class"""

    def __init__(self, screen, background_color):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        self._finalscoreb = 0
        self._finalscorew = 0
        self.winner = "No one it's a tie."
        self._endfont = pygame.font.Font(pygame.font.get_default_font(), 31)
        self._endmessage = self._endfont.render("Game Over!", True, (0, 0, 0))
        self._endmessage_pos = self._endmessage.get_rect(center=(400, 100))
        self._endfont2 = pygame.font.Font(pygame.font.get_default_font(), 24)
        self._endscorebmessage = self._endfont2.render(
            "Black Score: {} points.".format(self._finalscoreb), True, (0, 0, 0)
        )
        self._endscorebmessage_pos = self._endscorebmessage.get_rect(center=(600, 150))
        self._endscorewmessage = self._endfont2.render(
            "White Score: {} points.".format(self._finalscorew), True, (0, 0, 0)
        )
        self._endscorewmessage_pos = self._endscorewmessage.get_rect(center=(200, 150))
        self._winner = self._endfont2.render(
            "Winner is: {}.".format(self.winner), True, (0,0,0)
        )
        self._winner_pos = self._winner.get_rect(center = (400, 200))
        

    def start(self, scoreb, scorew):
        """This is the starting data"""
        self._finalscoreb = scorew
        self._finalscorew = scoreb
        if scoreb > scorew:
            self.winner = "White player"
        if scorew > scoreb:
            self.winner = "Black player"

    def update(self):
        """This updates the display"""
        self._endscorebmessage = self._endfont2.render(
            "Black Score: {} points.".format(self._finalscoreb), True, (0, 0, 0)
        )
        self._endscorewmessage = self._endfont2.render(
            "White Score: {} points.".format(self._finalscorew), True, (0, 0, 0)
        )
        self._winner = self._endfont2.render(
            "Winner is: {}.".format(self.winner), True, (0,0,0)
        )

    def draw(self):
        """This draws my pygame"""
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self._endmessage, self._endmessage_pos)
        self._screen.blit(self._endscorebmessage, self._endscorebmessage_pos)
        self._screen.blit(self._endscorewmessage, self._endscorewmessage_pos)
        self._screen.blit(self._winner, self._winner_pos)
        lastmessage = self._endfont2.render(
            "Press e to exit or r to restart the game", True, (0, 0, 0)
        )
        lastmessage_pos = lastmessage.get_rect(center=(400, 400))
        self._screen.blit(lastmessage, lastmessage_pos)

    def process_event(self, event):
        """This processes keyboard movement"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                self._is_valid = False
            if event.key == pygame.K_r:
                self._is_valid = False
                self._restart = True

    