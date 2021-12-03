//****************************************************************************************************************************
//Create a program in mixed languages (C, C++, and of course x86) that will compute the sum of the float numbers in an array.                             *
//                                                                                                                           *
//This file is part of the software program "Sum of an array".                                                        *
//Sum of array is free software: you can redistribute it and/or modify it under the terms of the GNU General Public*
//License version 3 as published by the Free Software Foundation.                                                            *
//Sum of array is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the       *
//implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more      *
//details.  A copy of the GNU General Public License v3 is available here:  <https:;www.gnu.org/licenses/>.                  *
//****************************************************************************************************************************
// The GPL3 conveys these basic rights: permission to study the source code, modify the source code, run it on any platform, distribute
//it in any media.   The GPL3 prohibits the recipient from removing the license from the source code and it prohibits
//information about the previous author(s).  There are more details about what GPL3 allows and disallows, but this is not
//the place to enumerate everything.  Visit the GNU website to know more details.
//
//=======1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**
//
//Author information
//  Author name: Richard Gresham
//  Author email: rgresham@csuf.fullerton.edu
//
//Program information
//  Program name: Sum of array
//  Programming languages: One modules in C++ and one module in X86
//  Date program began: 2021-Mar-06
//  Date of last update: 2021-Mar-21
//  Date comments upgraded: 2021-Mar-21
//  Date open source license added: 2021-Mar-06
//  Files in this program: Main.c Display.cpp Control.asm Fill.asm Sum.asm Script.sh
//  Status: Finished.
//  References consulted: Seyfarth, Chapter 18, Seyfarth, Chapter 7
//
//Purpose
//Create a program in mixed languages (C, C++, and of course x86) that will compute the sum of the float numbers in an array.
//This file
//  File name: Main.c
//  Language: C#
//  Max page width: 132 columns  [132 column width may not be strictly adhered to.]

//===== Begin code area ============================================================================================================

#include <stdio.h>
#include <stdint.h>    //Library not used
#include <string.h>
#include <math.h>

extern double Controlio(); //externing Control.asm function for use in c file.


int main()
{

double sum = -9.99; //set sum to random value


printf("Welcome to High Speed Array Summation by Richard Gresham. \n");
printf("Software licensed by GNU GPL 3.0. \n");
printf ("Version 1.0 released on January 28, 2021. \n");


sum = Controlio(); //set sum = to my asm function to call it.

printf("The main has received this number %.9lf and will keep it. \n", sum); //print out returned value of Control
printf("Thank you for using High Speed Array Software. \n"); //end of call messages
printf("For system support contact Richard Gresham at rgresham@csu.fullerton.edu \n");
printf("A zero will be returned to the operating system. \n");


return 0;


}



