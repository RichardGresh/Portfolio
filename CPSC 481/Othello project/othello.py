# Richard Gresham
# CPSC 481-05
# 2022 - 04 - 26
#rgresham@csu.fullerton.edu
# Othello program


import os
import pygame
import pygame.time
import scene
import time



def display_info():
    """Prints info about the display drive"""
    print('display is using the "{}" driver.'.format(pygame.display.get_driver()))
    print("Video Info: ")
    print(pygame.display.Info())




class Othello:
    """This is my Othello Class"""
    
    def __init__(self):
        """intiialization of Class"""
        self.window_size = (800,800)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.window_size)
        self.title = "Othello"
        self.running = True
        self._main_dir = os.path.split(os.path.abspath(__file__))[0]
        self._data_dir = os.path.join(self._main_dir, "data")
        self._restart = False
        self._scoreb = 0
        self._scorew = 0
        self.winner = 0
    
    
    def run(self):
        """This is the entry point into the game"""
        print("hi")
        if not pygame.font:
            print("Warning: fonts disabled")
        pygame.init()
        display_info()
        scene_list = [scene.BlinkingTitleScene(self.screen, (0,0,0), self.title, (120,120,240), 36 
                      ),
                      scene.GameScene(self.screen, (201,76,76)),
                      scene.EndScene(self.screen, (255,181,197),
                                    ),
                     ]
        finaloutcome = [0,0,False]
        for current_scene in scene_list:
            current_scene.start(self._scorew, self._scoreb)
            print("scene started")
            while current_scene.is_valid():
                self.clock.tick(current_scene.frame_rate())
                for event in pygame.event.get():
                    current_scene.process_event(event)
                    pygame.display.update()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    pygame.display.update()
                    current_scene.update()
                    current_scene.draw()
                    pygame.display.update()
                finaloutcome = current_scene.end()
                #print(finaloutcome[0])
                if finaloutcome[0] >= 0:
                    self._scoreb = finaloutcome[0]
                if finaloutcome[1] >= 0:
                    self._scorew = finaloutcome[1]
                if finaloutcome[2] == True:
                    self._restart = True
                
            if self._restart is True:
                self.__init__()
                self.run()
        print("Exiting!")
        pygame.quit()
        return 0
                    
            
    