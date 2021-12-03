;****************************************************************************************************************************
;Create a program in mixed languages (C, C++, and of course x86) that will ask for user input of floats into a an array of definitive size
;preventing overfill if user enters in too many values. It will then display and compute the sum of the array and return it to main.*
;Sum of an Array is free software: you can redistribute it and/or modify it under the terms of the GNU General Public       *
;License version 3 as published by the Free Software Foundation.                                                            *
;Sum of an Array is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the              *
;implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more      *
;details.  A copy of the GNU General Public License v3 is available here:  <https:;www.gnu.org/licenses/>.                  *
;****************************************************************************************************************************

;========1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**
;
;Author information
;  Author name: Richard Gresham
;  Author email: rgresham@csu.fullerton.edu
;
;Program information
;  Program name: Sum of a array
;  Programming languages: One modules in C++ and one module in X86
;  Date program began: 2021-Mar-06
;  Date of last update: 2021-Mar-24
;  Date comments upgraded: 2021-Mar-24
;  Date open source license added: 2021-Mar-06
;  Files in this program: Control.asm, Display.cpp, Fill.asm, Main.c, Script.sh, Sum.asm
;  Status: Finished.
;  References consulted: CS 240 class notes/lectures/Professor examples ie. floatio. Seyfarth, Chapter 18
;  Future upgrade possible: software to reject non-floats.
;
;Purpose
;  Create a program in mixed languages (C, C++, and of course x86) that will ask for user input to fill an array.
;  The program will prevent array overfill and will display the array and return the sum of array to main.
;  
;
;This file
;  File name: Control.asm
;  Language: X86 with Intel syntax.
;  Max page width: 132 columns
;  Assemble: nasm -f elf64 -l Control.asm


;===== Begin code area ========================================================================================================

extern printf
extern scanf
extern Fill
extern Sum
extern Display

global Controlio


Segment .data

prompt1 db "Welcome to HSAS. The accuracy and rleiability of this program is guaranteed by Richard Gresham", 10, 0

prompt2 db "The numbers you entered are these:" , 10 , 0
prompt3 db "The sum of these value is: %.8lf" , 10 ,0
goodbye1 db "The control module will now return the sum to the caller module." ,10 ,0


Segment .bss

myArray resq 10 ;set an array at size 10



Segment .text



Controlio:

;Prolog ===== Insurance for any caller of this assembly module ========================================================
;Any future program calling this module that the data in the caller's GPRs will not be modified. ;useful to always do
push rbp
mov  rbp,rsp
push rdi                                                    ;Backup rdi
push rsi                                                    ;Backup rsi
push rdx                                                    ;Backup rdx
push rcx                                                    ;Backup rcx
push r8                                                     ;Backup r8
push r9                                                     ;Backup r9
push r10                                                    ;Backup r10
push r11                                                    ;Backup r11
push r12                                                    ;Backup r12
push r13                                                    ;Backup r13
push r14                                                    ;Backup r14
push r15                                                    ;Backup r15
push rbx                                                    ;Backup rbx
pushf                                                       ;Backup rflags

;Registers rax, rip, and rsp are usually not backed up.


;Welcome prompt asking for inputed values
push qword 0

mov rax, 0 
mov rdi, prompt1
call printf


;calls fill with two parameters, rdi containing the array pointer, and rsi holding the size of the array. 
mov r12, 0
mov rax, 0
mov rdi, myArray
mov rsi, 10 ; since counter starts at 0
call Fill

mov r15, rax ;set r15 to how many numbers were filled in our array

;gives second prompt saying these numbers are:
mov rax, 0
mov rdi, prompt2
call printf

;sets up the call for the C++ function Display. With parameter 1 being myarray and parameter 2 being the size of the array we filled.
push qword 0
mov rax, 0
mov rdi, myArray
mov rsi, r15
call Display
pop rax

;sets up the call for the final call which is the sum, which takes parameter 1 which is our array, and parameter 2 which is how much of that array we filled

push qword 0
mov rax, 0
mov rdi, myArray
mov rsi, r15
call Sum ;sum function will give us the sum of our entire array
pop rax ;pop to prevent segfault, our number is stored in xmm0

movsd xmm10, xmm0  ;set xmm10 as the register to hold our number since xmm0 is unstable

;give the third prompt stating what our sum is
push qword 0
mov rax, 1
mov rdi, prompt3
call printf
pop rax

;gives our goodbye prompt stating the sum will return to Main.c
mov rax, 0
mov rdi, goodbye1
call printf

;moves back our sum back in xmm0 since that is the register that will return our value to main.
movsd xmm0, xmm10

pop rax

;===== Restore original values to integer registers ===================================================================
popf                                                        ;Restore rflags
pop rbx                                                     ;Restore rbx
pop r15                                                     ;Restore r15
pop r14                                                     ;Restore r14
pop r13                                                     ;Restore r13
pop r12                                                     ;Restore r12
pop r11                                                     ;Restore r11
pop r10                                                     ;Restore r10
pop r9                                                      ;Restore r9
pop r8                                                      ;Restore r8
pop rcx                                                     ;Restore rcx
pop rdx                                                     ;Restore rdx
pop rsi                                                     ;Restore rsi
pop rdi                                                     ;Restore rdi
pop rbp                                                     ;Restore rbp



ret

;========1=========2=========3=========4=========5=========6=========7=========8=========9=========0=========1=========2=========3**



