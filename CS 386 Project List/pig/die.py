# Richard Gresham
# CPSC 386-01
# 2021-10-15
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab 02-01
#
# This is my pig game and it does not oink.
#


"""This is my die class for my six sided dice."""
from random import randint


class Die:
    """This is the die class"""

    def __init__(self):
        """Die Class initializer"""
        self.dieroll = 0

    @staticmethod
    def dicemechanic():
        """Die random generator 1-6."""
        num = randint(1, 6)
        return num
