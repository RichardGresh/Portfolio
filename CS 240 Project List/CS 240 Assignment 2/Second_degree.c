//****************************************************************************************************************************
//This program will demonstrate how to input float numbers, how to input said float numbers and return invalid if it is indeed invalid.
// also demonstrates use of C, C++, and Assembly program, and can caculate quadratic formula and display roots if there exists any.                                *
//                                                                                                                           *
//This file is part of the software program "Root Calculator".                                                        *
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
//  Program name: Root Calculator
//  Programming languages: One modules in C++ and one module in X86
//  Date program began: 2021-Feb-22
//  Date of last update: 2021-Feb-27
//  Date comments upgraded: 2021-Feb-27
//  Date open source license added: 2020-Sep-20
//  Files in this program: isfloat.cpp, Quad_library.cpp, Quadratic.asm, Second_degree.c, Run.sh
//  Status: Finished.
//  References consulted: Seyfarth, Chapter 18, Seyfarth, Chapter 7
//
//Purpose
//  This program will demonstrate how to input float numbers, how to input said float numbers and return invalid if it is indeed invalid.
// also demonstrates use of C, C++, and Assembly program, and can caculate quadratic formula and display roots if there exists any.
//This file
//  File name: Second_degree.c
//  Language: C++
//  Max page width: 132 columns  [132 column width may not be strictly adhered to.]

//===== Begin code area ============================================================================================================

#include <stdio.h>
#include <stdint.h>    //Library not used
#include <string.h>
#include <math.h>



extern  double Quadraticio();


int main()
{
    double root1 = -9.99;
    

    printf("Welcome to Root Calculator \n");
    printf("Programmed by Richard Gresham, Professional Programmer. \n");


 root1 = Quadraticio();

printf ("The main driver received %.9lf and has decided to keep it \n", root1);

printf("Now 0 will be returned to the operating system. Have a nice day. Bye. \n");






return 0;
}

