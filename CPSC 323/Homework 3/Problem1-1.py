# ------------------------------------------------------------------
#             Group names: Gresham, Richard and McCarthy, Sean
#             Assignment: No. 3
#             Due Date: Febuary 16, 2022
#             Purpose: this program reads a file and determines whether a variable is a
#             ,identifier, and a reserved word.
# -----------------------------------------------------------------------
import os


def number_check(value):
    # checks a value to see if it finds a float if not return false.
    try:
        float(value)
        return True
    except ValueError:
        return False


def tokenchecker(file, reserved):
    tokenlist = []
    Tabledict = {}
    dictcount = 0
    lines = (
        file.readlines()
    )  # python's built in line reader, reads an entire line at a time.
    count = 0
    for line in lines:
        count += 1
        line = line[
            :-1
        ]  # This deletes the extra space that is found by using the readlines() command at the end.
        tokenlist.append(line)  # add it to the token list.
        # print(f" line {count}: {line}") checks to confirm line read
    for token in tokenlist:
        # This loops throughout our token list and checks for each condition returing a table value based upong what the file had.
        tokeninfo = []
        numcheck = True
        identifiercheck = True
        reservedcheck = False

        if not number_check(token):
            # checks to see if identifier passes number_check.
            numcheck = False
        if not (
            (token[0] >= "a" and token[0] <= "z")
            or (token[0] >= "A" and token[0] <= "Z")
            or (token[0] == "_")
        ):
            identifiercheck = False

        if identifiercheck == True:
            # checks to see if token passes identifier checks.
            for i in range(len(token)):
                if not (
                    (token[i] >= "a" and token[i] <= "z")
                    or (token[i] >= "A" and token[i] <= "Z")
                    or (token[i] == "_")
                    or (token[i] >= "0" and token[i] <= "9")
                ):
                    identifiercheck = False
        for word in reserved:
            # checks to see if token passes reserved check.
            if token == word:
                reservedcheck = True
        tokeninfo.append(token)
        if numcheck == True:
            tokeninfo.append("yes")
        else:
            tokeninfo.append("no")
        if identifiercheck == True:
            tokeninfo.append("yes")
        else:
            tokeninfo.append("no")
        if reservedcheck == True:
            tokeninfo.append("yes")
        else:
            tokeninfo.append("no")
        Tabledict[dictcount] = tokeninfo
        dictcount = dictcount + 1
        # Below are commmands to make the table look nice.
    print(
        "{:<5} {:<8} {:<5} {:<8} {:<5}".format(
            "Pos", "Token", "number", "identifier", "reserved word"
        )
    )
    for k, v in Tabledict.items():
        Token, number, identifier, reservedword = v
        print(
            "{:<5} {:<8} {:<8} {:<8} {:<8}".format(
                k, Token, number, identifier, reservedword
            )
        )


def main():
    """This is my word checker program"""
    file = "WordCheck.txt"
    file = open(file, "r")
    # our list of reserved words.
    reserved = ["while", "for", "switch", "do", "return"]
    tokenchecker(file, reserved)
    file.close()


if __name__ == "__main__":
    main()
