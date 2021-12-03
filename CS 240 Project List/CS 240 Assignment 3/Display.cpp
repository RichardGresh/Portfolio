/******************************************************************************************************************************
;*****************************************************************************************************************************
;Program name: "Assignment 3: Sum of an array". Create a program in mixed languages (C, C++, and of course x86) 
;that will allow user to enter in values into array in a function called fill. Will then display those numbers and return the sum
;to main.
;Copyright (C) 2021 Richard Gresham																							*
;This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License  *
;version 3 as published by the Free Software Foundation.                                                                    *
;This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied         *
;Warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.     *
;A copy of the GNU General Public License v3 is available here:  <https://www.gnu.org/licenses/>.                           *
;*****************************************************************************************************************************
;
;
;===================================================================
; Author information
;   Author name: Richard Gresham
;   Author email: rgresham@csu.fullerton.edu
;
; Program information
;   Program Name: Assignment 3: Sum of an array
;   Programming languages: One module done in x86 and three in c++ and one in C
;   Date Program began : 2021-Mar-06
;   Date Program completed: 2021-Mar-21
;   Status: Complete.  No noticeable error found after testing. Note really extreme values may be rounded similar to how most calculators work.
;
*/


#include <stdio.h>
#include <stdint.h>    //Library not used
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <iostream>
#include <iomanip>

extern "C" void Display( double array[],long int size); //prototype




void Display(double array[],long int size)  //my function that is called in Conrol to display array
{

for( int i = 0; i < size; i++)   //this is the loop that prints out my array to length of 8 decimal places.
{
    std::cout << std::fixed;           
    std::cout << std::setprecision(8);
    std::cout << array[i] << std::endl;

}


}







