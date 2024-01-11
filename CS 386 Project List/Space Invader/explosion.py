# Richard Gresham
# CPSC 386-01
# 2021-12-13
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab spaceinvaders
#
# This is where my Explosion happens.
#


"""This is my explosion class"""
import pygame


# create Explosion class
class Explosion(pygame.sprite.Sprite):
    """Start of my explosion"""

    def __init__(self, main_dir, x, y, explosionspeed):
        """Initializes my explosion"""
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 10):
            img = pygame.image.load(f"image/exp{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        self.explosion_speed = explosionspeed

    def update(self):
        """updates my explosion"""

        # update explosion animation
        self.counter += 1

        if self.counter >= self.explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if the animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= self.explosion_speed:
            self.kill()
