/******************************************************************************************************************************
;*****************************************************************************************************************************
;Program name: "Assignment 2: Root Calculator". This program will demonstrate how to input float numbers, how to input said float numbers and return invalid if it is indeed invalid.
; also demonstrates use of C, C++, and Assembly program, and can caculate quadratic formula and display roots if there exists any.		*
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
;   Program Name: Assignment 2: Root calcultator
;   Programming languages: One module done in x86 and three in c++ and one in C
;   Date Program began : 2021-Feb-21
;   Date Program completed: 2021-Feb-23
;   Status: Complete.  No noticeable error found after testing. Note really extreme values may be rounded similar to how most calculators work.
;
This File
;   Original Author  : Bilal 
;   File Name : isfloat.cpp
;   Language  : x86
;   Compile   : ng++ -c -m64 -Wall -fno-pie -no-pie -o isfloat.o isfloat.cpp -std=c++17
;   Link      : g++ -m64 -no-pie -o valid.out -std=c++17 triangle.o  isfloat.o area.o
;   Purpose   : The purpose of this file is to first take in string input from the user validate those strings as non-negative floats and then calculate Heron's formula
;               for the are of a triangle. If the user input is invalid it will display an error message and prompt the user to input another set of sides for the triangle.
;               If the input is valid it will print out the area of the triangle and return that value to triangle.cpp.
;
;*/


#include <cstdlib>
#include <ctype.h> 

using namespace std;

extern "C" bool isfloat(char []);

bool isfloat(char w[]) 
{
    bool result = true; // Assume floating number until proven otherwise.
    bool found = false; // Checks if only 1 decimal is entered.
    int start = 0;
    // if the floating point value is negative then we return false as a side of the triangle cannot be negative.
    if ( w[0] == '+' || w[0] == '-') start = 1;
    unsigned long int k = start;
    while( !(w[k]=='\0') && result )
        {
            if ((w[k] == '.') && !found) { found = true; 
            }
            else { result = result && isdigit(w[k]);
            }
            k++;
        }
    return result && found;
}