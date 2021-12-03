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


"""This is the player file"""


class Player:
    """This is the player class"""

    def __init__(self):
        """This is the Player constructor"""
        self.score = 0
        self.name = ''
        self.initial_roll = 0

    @staticmethod
    def player_prompt():
        """Prompt asking for how many players user wants."""
        validinput = False
        while validinput is False:
            print("do you want to play with", end=" ")
            aianswer = input("an ai named Hal [press y for yes or n for no]: ")
            if aianswer == 'y' or aianswer == 'n':
                validinput = True
            else:
                print("input error please try again.")
        return aianswer

    @staticmethod
    def playercount():
        """This initializes the number of players."""
        playernumvalidation = False
        while not playernumvalidation:
            print("how many players are", end=" ")
            numbplayers = int(
                input("playing the game?[2-4 players are allowed]: ")
            )

            if numbplayers > 4 or numbplayers < 2:
                print("invalid number of players please try again.")
            else:
                playernumvalidation = True
        return numbplayers

    def aiplayersetup(self):
        """This sets up the ai name as Hal9000"""
        self.name = "Hal9000"
        return self.name

    def playersetup(self, number):
        """This sets up player names."""
        namecheck = False
        playername = input("please enter your name player" + str(number) + ":")
        while not namecheck:
            if playername == "Hal9000":
                playername = input(
                    "please do not copy my name user. Please enter another name: "
                )
            else:
                namecheck = True
        self.name = playername

    def rollinput(self, number):
        """This has changes players objects initial roll."""
        self.initial_roll = number

    def scoreadd(self, number):
        """This adds the turn score to the player score object."""
        self.score = self.score + number

    def getname(self):
        """Gets the name"""
        return self.name

    def getscore(self):
        """Gets the score"""
        return self.score

    def getinitialroll(self):
        """Gets the initial roll"""
        return self.initial_roll
