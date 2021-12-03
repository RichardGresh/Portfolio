import math
from typing import Counter
import heapq






    


def main():
    barray1 = input("please input first array: ")
    barray2 = input("please input second array that will sort the first: ")
    array1 = conversion(barray1)
    array2 = conversion(barray2)
    B = patternsort(array1,array2)
    print(B)
    barray3 = input("please input all lists to be merged: ")
    array3 = Conversion2(barray3)
    final = mergearrays(array3)
    print(final)

def conversion(array1):
    copyarray = list()
    in_brackets = False
    temp = list()
    temp2 = ''
    b = ''
    negative = False
    for x in range(0, len(array1)):
        itsabracket = False
        itsnotallowed = False
        
        if array1[x] == '’' or array1[x] == '‘' or array1[x] == ' ' or array1[x] == "'" or array1[x] == "," :
            itsnotallowed = True
        
        if array1[x] == '[':
            in_brackets = True
            itsabracket = True
        if array1[x] == ']':
            in_brackets = False
        
        if in_brackets == True and itsabracket == False and itsnotallowed == False and negative == False:
            
            temp2 = temp2 + array1[x]
            
        
        if array1[x] == "," or array1[x] == "]":
            copyarray.append(temp2)
            temp2 = ''

    return copyarray
def patternsort(L1, L2):
    for i in range (len(L2) - 1, -1,-1):
        for j in range (0, len(L1)):
            if L1[j] == L2[i]: 
                temp = L1[j]
                L1.pop(j)
                L1.insert(0,temp)              
    return L1
                
    

  
def Conversion2(L1):
    copyarray = list()
    temp = ''
    templist = list()
    in_brackets = False
    for x in range(1, len(L1) - 1):
        itsabracket = False
        itsacomma = False
        itsnotallowed = False

        if L1[x] == '’' or L1[x] == '‘' or L1[x] == ' ' or L1[x] == "'" :

            itsnotallowed = True
        if L1[x] == '[':
            in_brackets = True
            itsabracket = True
        if in_brackets == True and (L1[x] == ',' or L1[x] == ']'):
            itsacomma = True
            templist.append(int(temp))
            temp =''
        if L1[x] == ']':
            in_brackets = False
            itsabracket = True
            copyarray.append(templist)
            templist = list()
        
        
        if in_brackets == True and itsacomma == False and itsabracket == False and itsnotallowed == False:
            temp = temp + L1[x]
    return copyarray
    
def mergearrays(L1):
    finallist = []
    heap = [(firstlist[0],i, 0) for (i, firstlist) in enumerate(L1) if firstlist]  #list comprehension that essentially makes a list of tuples that contains the first element of each list, with tuples representing value, index, and element.
    heapq.heapify(heap) #heapify's it so that we can use heap commands.
    while heap:
        value, index, element = heapq.heappop(heap)  #pop the lowest value of the heap and list it's value, index, and element into the three variables.
        finallist.append(value) #append the element into our final list.
        if element + 1 < len(L1[index]): #if our list branch doesn't go to the end do these commands.
            tuple = (L1[index][element + 1], index, element + 1) #gets the tuple of the next element in the list.
            heapq.heappush(heap, tuple) #push it into our heap. Then we once again run the heap looking for least value.
    return finallist
        
    







    




if __name__ == '__main__':
    main()


