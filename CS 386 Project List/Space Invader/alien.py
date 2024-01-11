# Richard Gresham
# CPSC 386-01
# 2021-12-13
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab spaceinvaders
#
# This is where my aliens are.
#


"""This is my alien class"""
import pygame
import os


class Alien(pygame.sprite.Sprite):
    """This is my alien class"""

    def __init__(self, screen, main_dir, pos, size, speed):
        """Initializes my alien class"""
        super().__init__()
        self.file = os.path.join(main_dir, "image", "snowflake.png")
        self.image = pygame.image.load(self.file).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)
        self.down = 3
        self.direction = 1
        self.speed = speed

    def update(self, direction):
        """Updates my alien"""
        self.alienmovement(direction)

    def alienmovement(self, direction):
        """Moves my alien"""
        if direction == 1:
            self.rect.x += self.speed
        if direction == -1:
            self.rect.x += -self.speed
        if direction != self.direction:
            self.rect.y += self.down
            self.direction = direction
            self.down = self.down + 1
