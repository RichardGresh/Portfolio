# Richard Gresham
# CPSC 386-01
# 2021-12-13
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab spaceinvaders
#
# This is where my Laser is.
#


"""This is my Laser File"""
import pygame


class Laser(pygame.sprite.Sprite):
    """This is my laser class"""

    def __init__(self, pos, color, screen, flag):
        """This initializes my Laser"""
        super().__init__()
        self.image = pygame.Surface((4, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.speed = 8
        self._screen = screen
        (w, h) = screen.get_size()
        self.h = h
        self.playerflag = flag

    def outofbounds(self):
        """lasers to far out of bounds, delete it"""
        if self.rect.y <= -(self.h // 8) or self.rect.y >= self.h + 100:
            self.kill()

    def update(self):
        """updates movement of laser"""
        self.movement()
        self.outofbounds()

    def movement(self):
        """increments movement of alien"""
        if self.playerflag == True:
            self.rect.y -= self.speed
        if self.playerflag == False:
            self.rect.y += self.speed
