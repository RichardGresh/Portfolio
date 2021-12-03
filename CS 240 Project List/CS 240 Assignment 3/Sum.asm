;****************************************************************************************************************************
;Create a program in mixed languages (C, C++, and of course x86) that will compute the sum of the float numbers in an array.                                                                                                                        *
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
;  File name: Sum.asm
;  Language: X86 with Intel syntax.
;  Max page width: 132 columns
;  Assemble: nasm -f elf64 -l Fill.asm

;=====================================================================================================================================
extern printf
extern scanf

global Sum

segment .data
answer db "the answer is %lf" , 10 ,0


segment .bss

segment .text



Sum:


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


mov r15, rdi ; is my array
mov r14, rsi ; how much we filled the array.

mov r13, 0   ;keeps track to make sure we don't go outside the size of what we filled.

mov rax, 0
cvtsi2sd xmm15, rax


begin_loop:
cmp r13, r14 ;compares how much we filled to our counter, if equal then we went through all of the array we filled.
jge finish_loop


movsd xmm14, [r15 + 8* r13]          ;moves our value in array into our xmm14 register so we can do float point math.

addsd xmm15, xmm14
inc r13  ;increase our counter.

jmp begin_loop



finish_loop:

movsd xmm0, xmm15 ;stores our sum into xmm0 which will be returned to our Control.asm






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

