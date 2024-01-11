# ------------------------------------------------------------------
#             Group names: Gresham, Richard and McCarthy, Sean
#             Assignment: No. 3
#             Due Date: Febuary 16, 2022
#             Purpose: this program runs a CFG and determines whether
#             to accept or reject input string by grammar.
# -----------------------------------------------------------------------

from re import A
from sre_parse import State


def String_Checker(myinput):
    Initial_State = 0
    transition_table = [
        # a, b, c
        [0, 1, 2],  # S = 0
        [2, 1, 3],  # B = 1
        [0, 3, 3],  # C = 2
        [1, 3, 2],  # D = 3
    ]
    # The 2-D array above represents the FA and where the FA points to.
    CurrentState = Initial_State
    # below checks each char input and changes the location of our current
    # state accordingly
    for char in myinput:
        if char == "a":
            CurrentState = transition_table[CurrentState][0]
        elif char == "b":
            CurrentState = transition_table[CurrentState][1]
        elif char == "c":
            CurrentState = transition_table[CurrentState][2]
        elif char == "$":
            if CurrentState == 1 or CurrentState == 2:
                return True
            else:
                return False
        else:
            return False


def main():
    """This is my Grammar program"""
    word = input("Please input a Grammar to be validated: ")

    Final_answer = String_Checker(word)
    if Final_answer == False:
        print("Rejected")
    else:
        print("Accepted")


if __name__ == "__main__":
    main()
