;****************************************************************************************************************************
;Program name: "perimeter". Purpose of the program is given the width and height of the rectangle compute the total perimeter *
; and the average length of side.                                                                                                                           *
;This file is part of the software program "Area of Rectangles".                                                        *
;Root Calculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public*
;License version 3 as published by the Free Software Foundation.                                                            *
;Root calculators is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the       *
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
;  Program name: perimeter
;  Programming languages: One modules in C++ and one module in X86
;  Date program began: 2021-Jan-28
;  Date of last update: 2021-Feb-13
;  Date comments upgraded: 2021-Feb-13
;  Date open source license added: 2021-Feb-01
;  Files in this program: rectangle.cpp, perimeter.asm, run.sh
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
;  File name: perimeter.asm
;  Language: X86 with Intel syntax.
;  Max page width: 132 columns
;  Assemble: nasm -f elf64 -l rectabgke.asm


;===== Begin code area ========================================================================================================


extern printf
extern scanf

global rectangleio

segment .data

input1prompt db "Enter the height:" ,10 ,0 

input2prompt db "Enter the width:" ,10 ,0 
output1prompt db "This program will compute the perimeter and the average side length of a rectangle." , 10 , 0
output2prompt db "The height of the rectangle is: %5.3lf" , 10,  0 ;use for upgradeability/not used for this project
output3prompt db "The width of the rectangle is: %5.3lf" , 10, 0  ;use for upgradeability/not used in this project
output4prompt db "The perimeter of the rectangle is: %5.3lf" , 10, 0
output5prompt db "The length of the average side: %5.3lf" , 10 , 0
height_float_number db "%lf", 0
width_float_number db "%lf", 0
perimeter_float_number db "%lf", 0
division_float_number db "%lf", 0
;final message
finalmessage1 db "I hope you enjoyed your rectangle" , 10 ,0
finalmessage2 db "The assembly program will send the perimeter to the main function." , 10, 0


segment .bss  ;Reserved for uninitialized data/ for things like arrays which is not needed this project

segment .text ;Reserved for executing instructions ;used below


rectangleio:          ;my function called rectangleio

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

;Display a welcome message to the viewer.
mov rax, 0                      ;means print f uses no data from xmm registers
mov rdi, output1prompt               ; above message 
call printf


; Display a prompt message asking for height

push qword 0
mov rax, 0
mov rdi, input1prompt
call printf
pop rax

; Begin the scanf block
push qword 0
mov rax, 0
mov rdi, height_float_number
mov rsi, rsp
call scanf
movsd xmm10, [rsp] ; height of my rectangle           

pop rax



; Display a prompt message asking for width
push qword 0
mov rax, 0
mov rdi, input2prompt
call printf
pop rax

; begin the scanf block for width
push qword 0
mov rax, 0
mov rdi, width_float_number
mov rsi, rsp
call scanf
movsd xmm11, [rsp]; width of my rectangle
pop rax


; now we are onto the arithmatic part
; ------------------------- math part----------------------------------------------------------------
;--- Arithmetic to get the perimeter of the rectangle------------------------------------------------

mov rax, 2
cvtsi2sd xmm12, rax   ;stores float 2.00 in my xmm12 register


mov rax, 4
cvtsi2sd xmm13, rax    ;stores float 4.00 in my xmm13 register


movsd xmm14, xmm10; copy of my data so I can maintain original numbers for later use in case of upgrades.
movsd xmm15, xmm10  
movsd xmm9, xmm11

addsd xmm14, xmm11; adds my width to my copy height
mulsd xmm14, xmm12; multiplies my copy height with my float number 2 giving me my perimeter 2(l + w)

; xmm14 will have our perimeter
;---------------------------------------------------Average side-----------------------------

 mulsd xmm15, xmm12; multiplies our widthand height by 2 giving us the number for all the sides
 mulsd xmm9, xmm12

 addsd xmm15, xmm9

 divsd xmm15, xmm13; makes our xmm15 have our average side



pop rax
; --------------------------------------display perimeter and average side-------------- -
; display perimeter
mov rax, 1
mov rdi, output4prompt
movsd xmm0, xmm14
call printf


;display average side

mov rax, 1
mov rdi, output5prompt
movsd xmm0, xmm15
call printf

movsd xmm10, lscpu

; ==========================Prepare to exit the program======================================================================== =

; Goobye message
mov rax, 0
mov rdi, finalmessage1
call printf



mov rax, 0
mov rdi, finalmessage2
call printf

mov rax, xmm0

 


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




