import math

















def fib1A(m): #recursive approach so the function must call itself back.
    if m <= 1: #at m < 1 it will just return that number
        return m #this is for the first and second element on the list so that it is printed.
    else:
        problem1A = fib1A(m-1) + fib1A(m-2) #based off of the diagram given. It will keep calling back fib1A(m-1) and fib1A(m-2) until those conditions no longer apply iE less than or equal to 1.
        return problem1A  #this is a recursive function since it calls itself.
#time complexity:
# T(m) = T(m - 1) + T(m - 2) + c (constant times of returns)
# T(m) = 2T(m - 2) + c This is because T(m-1) can be approximated to T(m-2) and vice versa
# T(m) <= c + 2c + 2^2c + 2^3 c + 2^4 c + 2^5 c + 2^6 c + .... + 2 ^(m-2)c + 2 ^(m-1)c
# T(m) = O(2^(m - 1)) + c 
# T(m) = O(2^m) every time the increment increases through this method, it will increase exponentially in the amount called. giving us tis O(2^m)
#master theorem cannot be applied here.

def prompt1(n):
    print("Problem 1A): The First Approach first " + str(n) + " terms printed.")
    fib1Asequence = list() # this could be used for future implementation, rather than just printing out the twenty turns it could be used for just printing one of them.
    Term_number = 0
    while Term_number != n:
        fib1Asequence.append(fib1A(Term_number)) #appends onto the list, and runs for first twenty terms, from 0 to 19 which represents the 20 numbers
        Term_number = Term_number + 1
    Listlength = len(fib1Asequence)
    
    i = 0
    while Listlength != 0:
        print("when n = " + str(i) + "     " + "Sequence is: " + str(fib1Asequence[i])) #prints out completed list of the fibanocci sequence
        i = i + 1
        Listlength = Listlength - 1

def fibEqu1(n):
    square5 = math.sqrt(5)
    fibnumb1 = (1 + square5)**n 
    fibnumb2 =  (1 - square5)**n
    fibnumb3 = (2**n) * square5
    fibfinal = (fibnumb1 - fibnumb2) / fibnumb3
    return int(fibfinal)

def fibEqu2(n, p):
    square5 = math.sqrt(5)
    if n == 0:
        return n
    if n == 1:
        return n
    if n > 1:
        Fp = fibEqu1(p)
    fibfinal = Fp * (((1 + square5) / 2) ** (n - p))
    return fibfinal

def fibEqu3(n): # f(n+1) is approximately f(n) * (1 + sqrt(5)) / 2
    if n == 0: #starting term
        return n  #starting term.
    if n == 1:
        return n 
    n = n - 1
    num1 = fibEqu1(n)
    square5 = math.sqrt(5)
    num2 = ((1 + square5)/2)
    numfib = num1 * num2 # f(n + 1) = f(n) * (1 + sqrt(5))/2
    return numfib  #return f(n + 1)
    

def prompt2A(n):
    print("")
    print("The Fibonacci sequence of Equation 2 printing first " + str(n) + " terms.")
    i = 0
    while n != 0:
        p = i - 1
        num = fibEqu2(i, p)
        print("when n = " + str(i) + "     " + "Sequence is: " + str(num))
        i = i + 1
        n = n - 1

    while True:   
        try:
            numberp = int(input("Please enter term p as a positive integer: "))
            assert(numberp > 0)
            break
        except:
            print("Error, Please try again.")
    while True:   
        try:
            numbern = int(input("Please enter term n as a positive integer: "))
            assert(numbern > 0)
            break
        except:
            print("Error, Please try again.")
        
    
    num3 = fibEqu2(numbern,numberp)
    print("This is the number when you find F" + str(numbern) + " using F" + str(numberp) + " as the previous term: " + str(num3))
   





def prompt2B(n):
    print("The Fibonacci sequence of Equation 3 printing first " + str(n) + " terms.")
    i = 0
    while n != 0:
        
        num = fibEqu3(i)
        print("when n = " + str(i) + "     " + "Sequence is: " + str(num))
        i = i + 1
        n = n - 1
    while True:   
        try:
            numbern = int(input("Please enter term n as a positive integer for Equation 3: "))
            assert(numbern > 0)
            break
        except:
            print("Error, Please try again.")
    answerq = fibEqu3(numbern)
    print("The Fibanocci number at sequence " + str(numbern) + " is: " + str(answerq))   
    #T(n) = 2 + n(3n + 7 + 3) + n(6) + 3n + 7 + 1 
    #T(n) = 2 + 3n^2 + 7n + 3n 6n + 3n + 7 + 1
    #T(n) = 3n^2 + 19n + 10
    #T(n) = O(3n^2 + 19n + 10)
    #T(n) = O(n^2)


def Subarray(V):
    b = 0
    e = 1
    for i in range(0,len(V) - 1):
        for j in range(i + 1,len(V)):
            if sum(V[i:j]) > sum(V[b:e]): #can be seen as getting the sum of n elements and sum of another n elements, where n is i through to j and b through to e.
                b = i
                e = j
    return V[b:e]



def finalprompt():
    print("Largest Sum Subarray Problem")
    parray = input("Please enter your array: ")
    varray = parray.replace('(', ' ').replace(')', ' ').replace(',', ' ').split() #this is 4n because each replace iterates thorughout the string, as does split so n+ n + n+ n.
    num = len(varray)
    i = 0
    barray = list()
    while num != 0:
        tempnum = varray[i]
        tempnum = int(tempnum)
        barray.append(tempnum)
        num = num - 1
        i = i + 1
    answer1 = Subarray(barray)
   
    print("This is the largest subarray: ")
    print(answer1)

   


        
 



    

    











def main():
    prompt1(20)
    prompt2A(20)
    prompt2B(20)
    finalprompt()


    
    

    




if __name__ == '__main__':
    main()