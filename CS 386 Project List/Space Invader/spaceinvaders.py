# Richard Gresham
# CPSC 386-01
# 2021-12-13
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab spaceinvaders
#
# This is where my game runs
#


"""This is my spaceinvader file and it runs the game"""
import os
import pygame
import pygame.time
import scene


def display_info():
    """Print out information about the display drive"""
    print('display is using the "{}" driver.'.format(pygame.display.get_driver()))
    print("Video Info: ")
    print(pygame.display.Info())


class Spaceinvaders:
    """This is the SnakeGame Class"""

    def __init__(self):
        """This is my initialization of Class"""
        self.window_size = (800, 800)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.window_size)
        self.title = "Space Invaders!!!"
        self.running = True
        self._main_dir = os.path.split(os.path.abspath(__file__))[0]
        self._data_dir = os.path.join(self._main_dir, "data")
        self._maintime = 0
        self._mainscore = 0
        self._restart = False
        self.bonus_round = False

    def run(self):
        """This is the entry point to the game"""
        if not pygame.font:
            print("Warning: fonts disabled.")
        if not pygame.mixer:
            print("Warning: sound disabled.")
        pygame.init()
        display_info()
        scene_list = [
            scene.BlinkingTitleScene(
                self.screen, (0, 0, 0), self.title, (120, 120, 240), 36
            ),
            scene.TimedGameScreen(self.screen, (0, 0, 0)),
            scene.Leaderboard(
                self.screen,
                (255, 181, 197),
            ),
        ]
        finalscore = [0, 0, False]
        for current_scene in scene_list:
            current_scene.start(self._mainscore, self._maintime)
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
            finalscore = current_scene.end()
            if finalscore[0] > 0:
                self._maintime = finalscore[0]
            if finalscore[1] > 0:
                self._mainscore = finalscore[1]
            if finalscore[2] is True:
                self._restart = True
        if self._restart is True:
            self.__init__()
            self.run()
        print("Exiting!")
        pygame.quit()
        return 0
