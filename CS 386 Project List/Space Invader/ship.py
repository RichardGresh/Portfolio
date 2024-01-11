# Richard Gresham
# CPSC 386-01
# 2021-12-13
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab spaceinvaders
#
# This is where my ship/car thing is.
#


"""This is my ship file"""
import os
import pygame
import laser


class Player(pygame.sprite.Sprite):
    """Representing the player as a spaceship."""

    def __init__(self, screen, main_dir, audiodir, pos):
        """Initializes my ship"""
        super().__init__()
        self.file = os.path.join(main_dir, "image", "player.png")
        self.image = pygame.image.load(self.file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 50))
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 4
        self._screen = screen
        self.timecharge = 0
        self.laser_recharge = 500
        self.laser_charged = True
        self.lasers = pygame.sprite.Group()
        self._screen = screen
        sound = os.path.join(audiodir, "Laser.wav")
        self.shiplasersound = pygame.mixer.Sound(sound)
        self.shiplasersound.set_volume(0.2)

    def update(self):
        """updates my player"""
        self.player_input()
        self.boundary()
        self.lasercharger()

    def player_input(self):
        """records player input"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x += -self.speed
        if keys[pygame.K_SPACE] and self.laser_charged:
            self.lasershoot()
            self.laser_charged = False
            self.timecharge = pygame.time.get_ticks()

    def lasercharger(self):
        """I'm charging my laser"""
        if self.laser_charged == False:
            current_time = pygame.time.get_ticks()
            if current_time - self.timecharge >= self.laser_recharge:
                self.laser_charged = True

    def lasershoot(self):
        """Fires my laser"""
        self.shiplasersound.play()
        self.lasers.add(
            laser.Laser(self.rect.center, (15, 255, 80), self._screen, True)
        )

    def boundary(self):
        """checks if my player hits a boundary and prevents OFB"""
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 800:
            self.rect.right = 800
