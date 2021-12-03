//****************************************************************************************************************************
//Program name: "rectangle".  The main purpose of the program is given the width and height of the rectangle compute the total perimeter and the
// average length of side. It will then return the                                   *
//                                                                                                                           *
//This file is part of the software program "Rectangle".                                                        *
//Rectangle is free software: you can redistribute it and/or modify it under the terms of the GNU General Public*
//License version 3 as published by the Free Software Foundation.                                                            *
//Rectangle is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the       *
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
//  Program name: Rectangle
//  Programming languages: One modules in C++ and one module in X86
//  Date program began: 2021-jan-27
//  Date of last update: 2021-Feb-13
//  Date comments upgraded: 2021-Feb-13
//  Date open source license added: 2020-Sep-20
//  Files in this program: rectangle.cpp, perimeter.asm 
//  Status: Finished.
//  References consulted: Seyfarth, Chapter 18
//
//Purpose
//  This program will demonstrate how to input float numbers, do basic arithmetic using float numbers, converting an int into a float number
//   and outputting  our finished answer from our asm file into our cpp file. Also linking an asm and a c++ or C# file.
//
//This file
//  File name: rectangle.cpp
//  Language: C++
//  Max page width: 132 columns  [132 column width may not be strictly adhered to.]

//===== Begin code area ============================================================================================================

#include <stdio.h>
#include <stdint.h>    //Library not used
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;

extern "C" double rectangleio();
 

int main()
{
  double mystery_number = 0.00009;

printf("%s", "Welcome to a friendly assembly program by Richard Gresham \n ");


mystery_number = rectangleio();
 
printf ("The main function received this number %2.4lf and has decided to keep it.\n", mystery_number);

printf("A 0 will be returned to the operating system. \n");
printf("Have a nice day.\n");


return 0;
}
