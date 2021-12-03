;****************************************************************************************************************************
;Program name: "Root Calculator". This program will demonstrate how to input float numbers, how to input said float numbers and return invalid if it is indeed invalid.
; also demonstrates use of C, C++, and Assembly program, and can caculate quadratic formula and display roots if there exists any.                                                                                                                        *
;This file is part of the software program "Root Calculator".                                                        *
;Root Calculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public*
;License version 3 as published by the Free Software Foundation.                                                            *
;Root Calculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the       *
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
;  Program name: Root Caculator
;  Programming languages: One modules in C++ and one module in X86
;  Date program began: 2021-Feb-17
;  Date of last update: 2021-Feb-27
;  Date comments upgraded: 2021-Feb-27
;  Date open source license added: 2021-Feb-01
;  Files in this program: isfloat.cpp, Quad_library.cpp, Quadratic.asm, Second_degree.c, Run.sh
;  Status: Finished.
;  References consulted: CS 240 class notes/lectures/Professor examples ie. floatio. Seyfarth, Chapter 18
;  Future upgrade possible: software to reject non-floats.
;
;Purpose
;  The main purpose of the program is given the width and height of the rectangle compute the total perimeter and the
; average length of side.
;  
;
;This file
;  File name: Quadratic.asm
;  Language: X86 with Intel syntax.
;  Max page width: 132 columns
;  Assemble: nasm -f elf64 -l rectabgke.asm


;===== Begin code area ========================================================================================================

extern printf
extern scanf
extern isfloat
extern atof
extern Quad_library
extern show_no_root
extern show_one_root
extern show_two_root

global Quadraticio


segment .data

openingmessage1 db "Please enter the three floating point coefficients of a quadratic equation in the order a, b, c. " ,10 , 0
openingmessage2 db "seperated by the end of line character. " ,10 , 0

inputmessage1 db "%lf", 0
stringformat1 db "%s", 0

check1 db "The number is %lf" , 10, 0
error_a db "This is not a quadratic equation. You may run this program again." , 10 ,0

outputmessage2 db "Invalid input data detected. You may run this program again." ,10 ,0
finalmessage db "One of these roots will be returned to the caller function." ,10 ,0
segment .bss  ;Reserved for uninitialized data/ for things like arrays which is not needed this project





segment .text ;Reserved for executing instructions ;used below


Quadraticio: ;function


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
push qword 0



;welcome prompt to enter in the three values.


;gives the first prompted opening message
mov rax, 0
mov rdi, openingmessage1
call printf


;gives the second prompted opening message
mov rax, 0
mov rdi, openingmessage2
call printf
 

 ;===========first input value=======================================
push qword 0 
mov rax, 0
mov rdi, stringformat1
sub rsp, 1024
mov rsi, rsp
call scanf  ;inputs our first value

;rsp will hold our value.

;========================data validation==========================================================
;calling isfloat setup
mov rdi, rsp   
mov rax, 0
call isfloat  ;checks out first value for data validation

;comparison if else function

cmp rax, 0 ;if rax == 0 then it means that the user's inputed value is invalid and an error message will be sent

je invalidRoot          ;translates my string of number into a float to be stored in a registers
mov rax, 1
mov rdi, rsp
call atof 
movsd xmm15, xmm0    ;xmm15 holds A

add rsp, 1024 ;adding back into the stack what we took and popping to clear the stack
pop rax

jmp end_of_if_else  ;this jumps past my invalid root function preventing it from being ran.

 invalidRoot:     ;rax == 0 and thus print error message
mov rax, 0
mov rdi, outputmessage2
call printf

add rsp, 1024  ;adding back into the stack what we took and popping to clear the stack
pop rax

jmp end_of_program ;once error message is ran it will jmp to the end of the assembly program

 end_of_if_else: ;jump location for correct data validation

;==================2nd input===============================
push qword 0
mov rax, 0
mov rdi, stringformat1
sub rsp, 1024
mov rsi, rsp
call scanf  ;this will contain our second string of float numbers

;========================data validation==========================================================

;calling isfloat setup
mov rdi, rsp   
mov rax, 0
call isfloat  ;this will check it for data validation

;comparison if else function

cmp rax, 0 ;if rax == 0 then jump to invalid

je invalidRoot2  ;if rax == 0 or if our input is invalid jump to our invalid prompt

mov rax, 1   
mov rdi, rsp
call atof
movsd xmm14, xmm0  ;xmm14 holds our second value

add rsp, 1024 ;clears stack for next input.
pop rax

jmp end_of_if_else2

 invalidRoot2:     ;rax == 0
mov rax, 0
mov rdi, outputmessage2
call printf   ;outputs error message

add rsp, 1024 ;clears stack for next input
pop rax

jmp end_of_program ;jumps to end of program

 end_of_if_else2: ;jump location for our data if it's validation

;==================3rd input===============================
push qword 0 ;push into stack
mov rax, 0
mov rdi, stringformat1
sub rsp, 1024            ;gives extra bytes for longer floats
mov rsi, rsp
call scanf               ;input c into our stack

;calling isfloat setup
mov rdi, rsp   
mov rax, 0
call isfloat                    ;call isfloat function from isfloat.cpp for data validation

;========================data validation==========================================================

;comparison if else function

cmp rax, 0 ;if rax == 0 then jump to invalid, since it's not a float     

je invalidRoot3          ;command that will jump it to invalid error block

mov rax, 1
mov rdi, rsp
call atof
movsd xmm13, xmm0 ;holds C as a float

add rsp, 1024 ;clears stack for next input since it's if else, need both
pop rax

jmp end_of_if_else3  

 invalidRoot3:     ;rax == 0 this is our invalid float block that prints error message
mov rax, 0
mov rdi, outputmessage2
call printf

add rsp, 1024 ;clears stack for next input
pop rax

jmp end_of_program  ;invalid data jumps to end of program

 end_of_if_else3: ;this is where our valid data will jump to


;=============================math part==============================================================================================================
push qword 0
;xmm15 is A
;xmm14 is b
;xmm13 is C


mov rax, -1
cvtsi2sd xmm10, rax


mulsd xmm10, xmm14 ; -b



mulsd xmm14, xmm14 ;b^2


mov rax, 4
cvtsi2sd xmm9 , rax ; 4.00

mulsd xmm9, xmm15 ;4a

mulsd xmm9, xmm13;4ac

subsd xmm14, xmm9 ; b^2 - 4ac


mov rax, 2
cvtsi2sd xmm11, rax ;xmm11 has 2.0000

;===========check for a = 0 /======================================================================







mov rax, 0
cvtsi2sd xmm12, rax ; 0 as a float
ucomisd xmm15, xmm12        ;ucomisd compares two float numbers. 

je a_equal_to ; if a = 0 then jump
;====================check for two roots, one roots, zero roots==============================================

ucomisd xmm14, xmm12 ;comparing b^2 - 4ac == 0

;at this point xmm10 has -b, xmm14 has b^2 -4ac, xmm9 has 4ac
;and xmm12 has 0

je equal_to ;if they are equal that is xmm14 == 0, jump

Ja greater_than  ;if they are greater than xmm14 > 0 jump

;======if they haven't jump yet it must be < than 0 and thus no roots========

call show_no_root ;calls our show_no_root function in Quad_library

movsd xmm0, xmm12
jmp Break_from_statements ;breaks to end of if else statements. 

;========if they are greater than xmm14 > 0 or two roots=================================
greater_than:
sqrtsd xmm9, xmm14 ; sqrt(b^2 -4ac)
mulsd xmm15, xmm11 ; xmm15 has 2a

movsd xmm13, xmm10 ;copy of xmm10 or -be
addsd xmm10, xmm9  ; -b + sqrt(b^2 - 4ac)
subsd xmm13, xmm9  ; -b - sqrt(b^2 - 4ac)

divsd xmm10, xmm15 ; (-b + sqrt(b^2 - 4ac)) / 2a
divsd xmm13, xmm15 ;(-b - sqrt(b^2 - 4ac)) / 2a

movsd xmm0, xmm10 ;stores our first root in xmm0 so it is used when the function is called.
movsd xmm1, xmm13 ;stores our second root in xmm1 so it is used when the function is called.

call show_two_root ;calls show two root which will display our two roots.



mov rax, 0
mov rdi, finalmessage
call printf 

movsd xmm0, xmm10

jmp Break_from_statements ;breaks to end of if else statements

;==============if xmm14 == 0 / 1 root ======================================================================
equal_to:
mulsd xmm15, xmm11 ; xmm15 has 2a
divsd xmm10, xmm15 ; -b/2a  this works since b^2 - 4ac is 0.
movsd xmm0, xmm10  ; move it into xmm0 so it can be called by show_one_root
call show_one_root

mov rax, 0
mov rdi, finalmessage
call printf 

movsd xmm0, xmm10
jmp Break_from_statements ;breaks to end of if else statements
;=================================if a = 0====================================================
a_equal_to: ;error message if a = 0
mov rax, 0
mov rdi, error_a
call printf
jmp Break_from_statements

;================================ending lines====================================================================
Break_from_statements:

pop rax
end_of_program:



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
