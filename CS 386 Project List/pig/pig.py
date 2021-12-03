#!/usr/bin/env python3
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


"""This is a Pig program!"""
import sys
from pig_game import Pgame


def main():
    """This is the main function"""
    pig = Pgame()
    pig.startgame()
    sys.exit()


if __name__ == '__main__':
    main()
