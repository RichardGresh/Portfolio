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
"""This is the snakeplayer class"""
import pygame
import pygame.constants


class Snake:
    """This is my Snake Class"""

    def __init__(self, screen, length, framerate):
        """This is my initialization of Class"""
        self._length = length
        self._screen = screen
        (w, h) = screen.get_size()
        self.w = w
        self.h = h
        self._snake_color = (34, 139, 34)
        self.x = w // 2
        self.y = h // 2
        self.direction = 4
        self.list_snake = [[self.x, self.y, self.direction]] * length
        self.snake_tail = self.list_snake[-1]
        self._snakespeed = 300
        self.velX = 0
        self.velY = 0
        self.dt = pygame.time.Clock().tick(framerate) / 1000

    # 1 = left, 2 = right, 3 = left, 4 = right

    def move_left(self):
        """This moves left"""
        self.direction = 1

    def move_right(self):
        """This moves right"""
        self.direction = 2

    def move_up(self):
        """This moves up"""
        self.direction = 3

    def move_down(self):
        """This moves down"""
        self.direction = 4

    def movement(self):
        """This controls movement"""
        if self.direction == 1:
            self.x -= (self.w) // 20
        elif self.direction == 2:
            self.x += (self.w) // 20
        elif self.direction == 3:
            self.y -= (self.h) // 20
        elif self.direction == 4:
            self.y += (self.h) // 20
        self.list_snake.insert(0, [self.x, self.y, self.direction])
        self.list_snake.pop()
        pygame.time.Clock().tick(self._snakespeed * self.dt)

    def addlength(self):
        """This adds length"""
        self._length = self._length + 1
        if self._length > len(self.list_snake):
            i = self.list_snake[-1]
            self.list_snake.append(i)

    def update(self):
        """This updates the display"""
        self.draw()

    def draw(self):
        """This draws my pygame"""
        for i in range(self._length):
            snakerect = pygame.Rect(
                self.list_snake[i][0], self.list_snake[i][1], self.w // 20, self.h // 20
            )
            pygame.draw.rect(self._screen, self._snake_color, snakerect)
