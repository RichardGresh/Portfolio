# Richard Gresham
# CPSC 386-01
# 2021-11-29
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab Snake
#
# This is where my Snake is made
#

"""This is my Fruit File"""
import random
import pygame


class Fruit:
    """This is my Fruit Class"""

    def __init__(
        self,
        screen,
    ):
        """This is the initialization of my class"""
        self._screen = screen
        (w, h) = screen.get_size()
        self.w = w
        self.h = h
        self._squarecount = 20
        self.x = random.randint(1, self._squarecount - 2) * w // 20
        self.y = random.randint(1, self._squarecount - 2) * h // 20
        self.color = (255, 0, 0)
        self.fruit_rect = 0

    def draw(self):
        """This draws my pygame"""
        self.fruit_rect = pygame.Rect(self.x, self.y, self.w // 20, self.h // 20)
        pygame.draw.rect(self._screen, self.color, self.fruit_rect)

    def update(self):
        """This updates my pygame"""
        self.x = random.randint(1, self._squarecount - 2) * self.w // 20
        self.y = random.randint(1, self._squarecount - 2) * self.h // 20
        self.fruit_rect = pygame.Rect(self.x, self.y, self.w // 20, self.h // 20)
