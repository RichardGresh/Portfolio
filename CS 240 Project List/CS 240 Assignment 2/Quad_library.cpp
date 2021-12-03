
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
;   Date Program completed: 2021-Feb-27
;   Status: Complete.  No noticeable error found after testing. Note really extreme values may be rounded similar to how most calculators work.
;
*/

#include <stdio.h>
#include <stdint.h>    //Library not used
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>

extern "C" void show_no_root();
extern "C" void show_one_root(double root1);
extern "C" void show_two_root(double root1, double root2);

void show_no_root()
{

printf("There are no roots in this equation. \n");

 
}
void show_one_root(double root)
{
    
printf("The root is %.9lf \n", root);
}
void show_two_root(double root1, double root2)
{
printf("The roots are %.9lf and %.9lf \n", root1, root2);



}