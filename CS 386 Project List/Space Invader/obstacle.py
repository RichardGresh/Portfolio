# Richard Gresham
# CPSC 386-01
# 2021-12-13
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab spaceinvaders
#
# This is where my Obstacle is.
#


"""This is where my obstacle is"""
import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        """Creates my Obstacle blocks"""
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
