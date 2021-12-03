;****************************************************************************************************************************
;Create a program in mixed languages (C, C++, and of course x86) that will ask for user input of float values
; it will make sure user doesn't overfill array and will display floats in array and return sum to main.                                                                                                                      *
;This file is part of the software program "Sum of an array".                                                        *
;Sum of an Array is free software: you can redistribute it and/or modify it under the terms of the GNU General Public*
;License version 3 as published by the Free Software Foundation.                                                            *
;Sum of an Array is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the       *
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
;  Date of last update: 2021-Mar-21
;  Date comments upgraded: 2021-Mar-21
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
;  File name: Fill.asm
;  Language: X86 with Intel syntax.
;  Max page width: 132 columns
;  Assemble: nasm -f elf64 -l Fill.asm

;=====================================================================================================================================
extern printf
extern scanf

global Fill

segment .data
prompt1 db "Please enter floating point numbers seperated by ws.", 10, 0
prompt2 db "When finished press enter followed by cntl+D" , 10, 0
display1 db "The counter is at %ld" , 10 ,0
float_format db "%lf",0


segment .bss


segment .text


Fill:



;===== Backup all the registers that are used in this program =====================================================================
push rbp                                                    ;Backup the base pointer
mov  rbp,rsp                                                ;Advance the base pointer to start of the current stack frame
push rdi                                                    ;Backup rdi
push rsi                                                    ;Backup rsi
push rdx                                                    ;Backup rdx
push rcx                                                    ;Backup rcx
push r8                                                     ;Backup r8
push r9                                                     ;Backup r9
push r10                                                    ;Backup r10
push r11                                                    ;Backup r11: printf often changes r11
push r12                                                    ;Backup r12
push r13                                                    ;Backup r13
push r14                                                    ;Backup r14
push r15                                                    ;Backup r15
push rbx                                                    ;Backup rbx
pushf                                                       ;Backup rflags
;rax, rip, and rsp are intentionally not backed up.  r15 is not used explicitly in this program, but it is backed up nevertheless.

mov r14, rsi ;array size
mov r15, rdi ;the array



mov rax, 0
mov rdi, prompt1
call printf

mov rax, 0
mov rdi, prompt2
call printf



;================Creating the array of Floats===========


;this is our initial loop counter keeping track of how much of the array we fill.
mov r13, 0 ;loop counter

;our start of our loop
begin_loop:

;compare how much we filled in our array with our array size to make sure user doesn't overfill it.
cmp r13, r14
jge finish_loop

;this block indicates user input for the number.
push qword 0
mov rax, 0
mov rdi, float_format
mov rsi, rsp
call scanf


;this checks to see if we inputed ctrl d, if if we did it will put -1 into rax
cdqe
;if it is equal then user indicated he is done filling array and thus it will exit.
cmp rax, -1
je done_loop

;if not equal continue downward and fill in number into our array.
pop rax
mov r12 , rax


mov [r15 + 8*r13], r12

inc r13 ;increasing our loop counter for size filled.

jmp begin_loop ;goes back to beginning of loop.


done_loop:
pop r10 ;this pops to prevent seg fault error.

finish_loop:





mov rax, r13 ;stores how much we filled of the array and sends it back to control.asm


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

