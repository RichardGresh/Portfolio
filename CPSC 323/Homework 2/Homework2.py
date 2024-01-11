# ------------------------------------------------------------------
#             Group names: Gresham, Richard and McCarthy, Sean
#             Assignment: No. 2
#             Due Date: Febuary 9, 2022
#             Purpose: this program reads an expression in postfix form
#             evaluates the expression and displays its values
# -----------------------------------------------------------------------
def main():
    """This is my stack program"""
    looprun = True
    wordstorage = (
        {}
    )  # saves dictionary so if the user continues, variables he used is saved.
    while looprun:
        # loop of program so it can continue at user request.
        print("please enter in your postfix expression.")
        postfix = input("Enter your expression: ")
        s1 = postfixevaluation(postfix, wordstorage)
        if s1 != False:
            print(s1)
        ask = input("CONTINUE(y/n)? ")
        if ask == "n" or ask == "N":
            looprun = False


def number_check(value):
    # checks a value to see if it finds a float if not return false.
    try:
        float(value)
        return True
    except ValueError:
        return False


def postfixevaluation(exp, wordstorage):
    # this evaluates a postfix expression and turns it into infix.
    stackops = []
    stackvalues = []
    token = ""
    for i in range(0, len(exp)):
        # This for loops creates a list of tokens from user input requires space between each token.
        if exp[i] == " ":
            # print(token)
            stackops.append(token)
            token = ""
        if exp[i] != " ":
            token += exp[i]
            if exp[i] == "$":
                stackops.append(token)
                token = ""

    while len(stackops) != 0:
        # this while loop checks each token and does the appropriate actions via if else if statements.
        value = stackops.pop(0)
        if number_check(value):
            # checks if it's a float or int.
            if value.isdigit():
                value = int(value)
                stackvalues.append(value)
            else:
                value = float(value)
                stackvalues.append(value)
        elif value == "+":
            s1 = stackvalues.pop()
            s2 = stackvalues.pop()
            s3 = s2 + s1
            stackvalues.append(s3)

        elif value == "-":
            s1 = stackvalues.pop()
            s2 = stackvalues.pop()
            s3 = s2 - s1
            stackvalues.append(s3)
        elif value == "*":
            s1 = stackvalues.pop()
            s2 = stackvalues.pop()
            s3 = s2 * s1
            stackvalues.append(s3)
        elif value == "/":
            s1 = stackvalues.pop()
            s2 = stackvalues.pop()
            s3 = s2 / s1
            print(s3)
            stackvalues.append(s3)
        elif value == "^" or value == "**":
            s1 = stackvalues.pop()
            s2 = stackvalues.pop()
            s3 = s2 ** s1
        elif value == "%":
            s1 = stackvalues.pop()
            s2 = stackvalues.pop()
            s3 = s2 % s1
        elif value == "$":
            return stackvalues.pop()
        elif value in wordstorage:
            stackvalues.append(wordstorage[value])
        else:
            # if none of these passes it meant the problem is a variable.
            numerator = input(
                "User please enter in a numeric value for word " + value + ": "
            )
            wordstorage[value] = int(
                numerator
            )  # stores variable and value into dictionary.
            stackvalues.append(wordstorage[value])  # appends the value to the stack.


if __name__ == "__main__":
    main()
