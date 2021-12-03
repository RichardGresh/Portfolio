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


""""This is our piggame file"""
import time
import player
import die


class Pgame:
    """This is the pgame class."""

    def __init__(self):
        """This is the pgame constructor"""
        self.player = player.Player()
        self.dice = die.Die()
        self.players = []
        self.turnscore = 0
        self.rollcount = 0
        self.temppoint = 0
        self.playerturn = True

    def startgame(self):
        """This is the core of the program and runs most of the functions."""
        playerlist = []
        print("Welcome to the game of pig")
        print("This pig program can be enjoyed with up to four players,")
        print("or you can play against an ai instead")
        answer = self.player.player_prompt()
        if answer == 'n':
            playercount = self.player.playercount()
            brange = 1
            counter = 0
            while counter != playercount:
                humanplayer = player.Player()
                humanplayer.playersetup(brange)
                playerlist.append(humanplayer)
                brange = brange + 1
                counter = counter + 1
            counter = 0
            while counter != playercount:
                # Start for initial roll, asks user to press r, reads input
                # and checks for validation, then sets initial roll in player class.
                time.sleep(1)
                print("Please roll for turn", end=" ")
                checkr = input(
                    "order press r to roll "
                    + playerlist[counter].getname()
                    + ":"
                )
                valid1input = True
                while valid1input:
                    if checkr != 'r':
                        time.sleep(1)
                        checkr = input("Error Please press r to roll.")
                    else:
                        valid1input = False
                rolled = self.dice.dicemechanic()
                playerlist[counter].rollinput(rolled)
                print("you rolled a: ", rolled)
                counter = counter + 1
            self.players = sorted(playerlist, key=lambda x: x.getinitialroll())
            # this command sorts the playerlist by their initial roll.
            counter = 0
            print("Turn order is: ")
            while counter != playercount:
                print(self.players[counter].getname(), end=' ')
                counter = counter + 1

        if answer == 'y':
            playercount = 2
            aiplayer = True
            humanplayer = player.Player()
            brange = 1
            humanplayer.playersetup(1)
            playerlist.append(humanplayer)
            aiplayer = player.Player()
            aiplayer.aiplayersetup()
            playerlist.append(aiplayer)
            print("Please roll for turn", end=" ")
            checkr = input(
                "order press r to roll "
                + playerlist[0].getname()
                + ":"
                # this asks for roll
            )
            # asks player for roll.
            valid1input = True
            while valid1input:
                if checkr != 'r':
                    checkr = input("Error Please press r to roll.")
                else:
                    valid1input = False
            rolled = self.dice.dicemechanic()
            time.sleep(1)
            print("you rolled a: ", rolled)
            playerlist[0].rollinput(rolled)

            airolled = self.dice.dicemechanic()
            time.sleep(1)
            print("Hal9000 rolled a: ", airolled)
            playerlist[1].rollinput(airolled)
            self.players = sorted(playerlist, key=lambda x: x.getinitialroll())
            # sorts the human player an ai by ascending initial score, For ties player goes first.
            counter = 0
            time.sleep(1.0)
            print("Turn order is: ")
            while counter != playercount:
                print(self.players[counter].getname(), end=' ')
                counter = counter + 1
        time.sleep(1.0)
        print("\n LET THE GAMES BEGIN!!!")
        self.gamebegins()

    def gamebegins(self):
        """The game began"""
        game = True
        while game:
            # This while loop is essentially the running of the game.
            # As long as a player doesn't win after the for loop will keep repeating,
            # enabling a ordered repeat of turns going from players 1-4 back and forth.
            # there is no valid input in this series of choices as
            # if a player enters a wrong prompt it just restarts in the path.
            for participant in self.players:
                self.playerturn = True
                points = 0
                self.rollcount = 0
                self.turnscore = 0
                # turn score is temporary and if player holds it gets added to player attribute score
                self.temppoint = 0
                valid2input = False
                # This is for the ai, and is essentially an early turnscore
                # + score,lets ai know to hold and win the game when they reach 100.
                time.sleep(1.5)
                print("it's " + participant.getname() + "'s turn.")
                while self.playerturn:
                    time.sleep(1.0)
                    print("total score: " + str(participant.getscore()))
                    time.sleep(1.0)
                    print("Current turn score: " + str(self.turnscore))
                    time.sleep(1.0)
                    print("Turn Roll count:  " + str(self.rollcount))
                    if participant.getname() != "Hal9000":
                        # I'm designating different paths for the player and
                        # AI by checking the players name.
                        # If it doesn't match ainame it runs the human player path.
                        if self.rollcount == 0:
                            time.sleep(1.0)
                            rollrhold = input(
                                "press r to roll "
                                + participant.getname()
                                + ": "
                            )
                            while not valid2input:
                                if rollrhold == 'r':
                                    valid2input = True
                                else:
                                    time.sleep(1.0)
                                    rollrhold = input(
                                        "Error Please press r to roll: "
                                    )
                            if rollrhold == 'r':
                                points = self.dice.dicemechanic()
                                time.sleep(1.0)
                                print("you rolled a: " + str(points))
                                if points == 1:
                                    time.sleep(1.0)
                                    print("too bad")
                                    self.turnscore = 0
                                    self.playerturn = False
                                else:
                                    self.turnscore = self.turnscore + points
                                    self.rollcount = self.rollcount + 1
                        else:
                            time.sleep(1.0)
                            # rollrhold = input("press r to roll
                            # or h to hold {}: ".format(participant.getname()))
                            print("press r to roll", end=" ")
                            rollrhold = input(
                                "or h to hold " + participant.getname() + ": "
                            )
                            while not valid2input:
                                if rollrhold == 'r' or rollrhold == 'h':
                                    valid2input = True
                                else:
                                    time.sleep(1.0)
                                    rollrhold = input(
                                        "Error Please press r to roll or h to hold: "
                                    )
                            if rollrhold == 'h':
                                time.sleep(1.0)
                                print("player holds.")
                                participant.scoreadd(self.turnscore)
                                # adds the turnscore into our score attribute.
                                self.playerturn = False
                            elif rollrhold == 'r':
                                points = self.dice.dicemechanic()
                                time.sleep(1.0)
                                print("you rolled a: " + str(points))
                                if points == 1:
                                    time.sleep(1.0)
                                    print("too bad.")
                                    self.turnscore = 0
                                    self.playerturn = False
                                else:
                                    self.turnscore = self.turnscore + points
                                    self.rollcount = self.rollcount + 1
                    if participant.getname() == "Hal9000":
                        if self.rollcount == 0:
                            time.sleep(1.0)
                            print("Hal9000 presses r.")
                            points = self.dice.dicemechanic()
                            time.sleep(1.0)
                            print("Hal9000 rolled a: " + str(points))
                            if points == 1:
                                time.sleep(1.0)
                                print("This was not a part of my calculations.")
                                self.turnscore = 0
                                self.playerturn = False
                            else:
                                self.turnscore = self.turnscore + points
                                self.rollcount = self.rollcount + 1
                                self.temppoint = points
                        else:
                            time.sleep(1.0)
                            print("Hal9000 is deciding to roll or hold.")
                            tempcheck = self.turnscore + participant.getscore()
                            if tempcheck >= 100:
                                time.sleep(1.0)
                                print("Ha, Ha, Ha, Ha, Ha, Ha, Ha.")
                                participant.scoreadd(self.turnscore)
                                self.playerturn = False
                            else:
                                if self.temppoint <= 3 and self.turnscore >= 15:
                                    time.sleep(1.0)
                                    print("Hal9000 has decided to hold.")
                                    participant.scoreadd(self.turnscore)
                                    self.playerturn = False
                                else:
                                    time.sleep(1.0)
                                    print("Hal9000 has decided to roll")
                                    points = self.dice.dicemechanic()
                                    time.sleep(1.0)
                                    print(
                                        "Hal9000 has rolled a: " + str(points)
                                    )
                                    if points == 1:
                                        time.sleep(1.0)
                                        print(
                                            "This was not a part of my calculations."
                                        )
                                        self.turnscore = 0
                                        self.playerturn = False
                                    else:
                                        self.temppoint = points
                                        self.turnscore = self.turnscore + points
                                        self.rollcount = self.rollcount + 1
                    if participant.getscore() >= 100:
                        # set commands to leave the game and give the winner.
                        winner = participant.getname()
                        self.playerturn = False
                        game = False
                if game is False:
                    # immediately break the for loop as there is no point continuing turns.
                    break
        self.win(winner)

    @staticmethod
    def win(dplayer):
        """This is the player winning function"""
        time.sleep(1.0)
        print(dplayer + " wins!")
