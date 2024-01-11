
def main():
    print("this is my Predictive table program.")
    uinput = input("Please enter in a trace input: ")
    table = input("if problem 1 table press 1, else press 2: ")
    print(table)
    if table == '1':
        validation = Table(uinput)
        validation.validationcheckp1()
        if validation._ar == False:
            print("REJECTED")
        else:
            print("ACCEPTED")
    if table == '2':
        validation = Table(uinput)
        validation.validationcheckp2()
        if validation._ar == False:
            print("REJECTED")
        else:
            print("ACCEPTED")

class Table:
    def __init__(self,input):
        self._userinput = input
        self._ar = True
                        #i     #+       #-       # *      # /      #(     #)       #$
        self.PTable1 =[["TQ", "blank", "blank", "blank", "blank", "TQ" , "blank", "blank"], #E
                     ["blank", "+TQ","-TQ", "blank", "blank", "blank", "lambda", "lambda"],#Q
                     ["FR", "blank", "blank", "blank", "blank", "FR", "blank", "blank"],   #T 
                     ["blank", "lambda", "lambda", "*FR", "/FR", "blank", "lambda", "lambda"], #R
                     ["i", "blank", "blank","blank","blank", "(E)","blank","blank"]] #F
                        #a     # =     # +       # -      #/        # *     # (      # )      # $
        self.PTable2 =[["aW", "blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank"], #S
                       ["blank", "=E", "blank", "blank", "blank", "blank", "blank", "blank", "blank"], #W
                       ["TQ", "blank", "blank", "blank", "blank", "blank", "TQ", "blank", "blank"],    #E
                       ["blank", "blank", "+TQ", "-TQ", "blank", "blank", "blank", "lambda", "lambda"],#Q
                       ["FR", "blank", "blank", "blank", "blank", "blank", "FR", "blank", "blank"],    #T
                       ["blank", "blank", "lambda", "lambda", "/FR", "*FR", "blank", "lambda", "lambda"], #R
                       ["a", "blank", "blank", "blank", "blank", "blank", "(E)", "blank", "blank"]] #F
        
    
    def validationcheckp1(self):
        tracinginput = self._userinput
        stackinput = []  
        stackinput.append("$")
        stackinput.append("E")
        for i in tracinginput:
            #print("read: " , i)
            row = -1
            column = -1
            looper = True
            while(looper):
                if len(stackinput) == 0:
                    self._ar = False
                    looper = False
                    
                value = stackinput.pop()
                #checks if value is i if not checks row and column number for next value, if it doesn't exist on the parsing table it returns rejected.
                if i == value:
                   # print("Value:", value)
                   # print("Match with input: ", i)
                    looper = False
                else:
                    #GO To EX:[A, x]
                    if value == "E":
                        row = 0
                    elif value == "Q":
                        row = 1
                    elif value == "T":
                        row = 2
                    elif value == "R":
                        row = 3
                    elif value == "F":
                        row = 4
                    else:
                        print("falls through", value)
                        self._ar = False
                        break
                    if i == "i":
                        column = 0
                    elif i == "+":
                        column = 1
                    elif i == "-":
                        column = 2
                    elif i == "*":
                        column = 3
                    elif i == "/":
                        column = 4
                    elif i == "(":
                        column = 5
                    elif i == ")":
                        column = 6
                    elif i == "$":
                        column = 7
                        
                    parseinput = self.PTable1[row][column]
                    if parseinput == "blank":
                        #print(parseinput)
                        self._ar = False
                        break
                    elif parseinput != "lambda":  
                        for j in reversed(parseinput):
                            stackinput.append(j)
                    
                        
                        
            if self._ar == False:
                break
    def validationcheckp2(self):
        tracinginput = self._userinput
        stackinput = []  
        stackinput.append("$")
        stackinput.append("S")
        for i in tracinginput:
            row = -1
            column = -1
            looper = True
            while(looper):
                if len(stackinput) == 0:
                    self._ar = False
                    looper = False
                    
                value = stackinput.pop()
                
                if i == value:
                    print("Value:", value)
                    print("Match with input: ", i)
                    looper = False
                else:
                    if value == "S":
                        row = 0
                    elif value == "W":
                        row = 1
                    elif value == "E":
                        row = 2
                    elif value == "Q":
                        row = 3
                    elif value == "T":
                        row = 4
                    elif value == "R":
                        row = 5
                    elif value == "F":
                        row = 6
                    else:
                        print("falls through", value)
                        self._ar = False
                        break
                    if i == "a":
                        column = 0
                    elif i == "=":
                        column = 1
                    elif i == "+":
                        column = 2
                    elif i == "-":
                        column = 3
                    elif i == "/":
                        column = 4
                    elif i == "*":
                        column = 5
                    elif i == "(":
                        column = 6
                    elif i == ")":
                        column = 7
                    elif i == "$":
                        column = 8
                    parseinput = self.PTable2[row][column]
                    if parseinput == "blank":
                        #print(parseinput)
                        self._ar = False
                        break
                    elif parseinput != "lambda":  
                        for j in reversed(parseinput):
                            stackinput.append(j)
                    
                        
                        
            if self._ar == False:
                break
   
if __name__ == "__main__":
    main()