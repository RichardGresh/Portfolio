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
;  Program name: Interview 
;  Programming languages: One modules in C++ and one module in X86
;  Date program began: 2021-April-15
;  Date of last update: 2021-April-25
;  Date comments upgraded: 2021-April-25
;  Date open source license added: 2021-Apr-15
;  Files in this program: Main.cpp, interview.asm r.sh
;  Status: Finished.
;  References consulted: CS 240 class notes/lectures/Professor 
;  Future upgrade possible: possible choices for other majors
;
;Purpose
;  Create a program in mixed languages (C++ and of course x86) that will ask for user to answer questions in an interview
; and have different endings depending upon questions asked, aka chris sawyer.
;  
;
;This file
;  File name: interview.asm
;  Language: X86 with Intel syntax.
;  Max page width: 132 columns
;  Assemble: nasm -f elf64 -l interview.asm


;===== Begin code area ========================================================================================================

extern printf
extern scanf
extern getchar

global interview

Segment .data
 messageintro db "Hello %s I am Ms Fenster. The interview will begin now." ,10 ,0

test1 db "hi." ,10 ,0
resistancequestion db "Alright. Now we will work on your electricity." , 10, 0
resistance1 db "Please enter the resistance of circuit #1 in ohms: " , 10 ,0
resistance2 db "Please enter the resistance of circuit #2 in ohms: " , 10 ,0
floatformat db "%lf"  ,0
floatformat2 db "%lf"  ,0
totalresistance db "The total resistance is %.12lf Ohms." , 10 ,0
charformat db "%s"  ,0
computerscience db "Were you a computer science major (y or n)?" ,10, 0

 wowmessage db "Wow! %lf That's a lot of cash. Who do you think you are, Chris Sawyer(y or n)?",0

exitmessage db "Thank You. Please follow the exit signs to the front desk." , 10 ,0



Segment .bss
myname resq 50; 

Segment .text



interview:



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

mov r14, rdi  ;holds my name

movsd xmm15, xmm0 ;holds the money

;welcome prompt with users name in it.
push qword 0
mov rax, 0
mov rdi, messageintro ;hello message.
mov rsi, r14 ;this is our first parameter holding our name, so it will print the message with our name.
call printf
pop rax




;prompt exclaiming surprise at price of items.
push qword 0
mov rax, 1
mov rdi, wowmessage ;prompt asking if your chris sawyer or not.
movsd xmm0, xmm15   ;prints out message with the money that the interviewie listed.
call printf

pop rax


push qword 0
mov rax, 1
mov rdi, charformat ;sets up scan to charformat so that it can take a char.
mov rsi, rsp
call scanf 
pop rax
mov r15, 'y' ;no use for this command as I didn't use it in compare.  

cmp rax, 'y' ;comparing what the user input with the 'y' char to indicate yes.
je Chris_Sawyer ;if yes this will jump past the resistance part.

mov rax, 0
mov rdi, resistancequestion ;props up the question about resistance.
call printf

;-----prompt for first resistance---------

mov rax, 0
mov rdi, resistance1 ;refers to question please enter first resistance.
call printf



push qword 0
mov rax, 0
mov rdi, floatformat ;sets up answer in float format.
mov rsi, rsp
call scanf
movsd xmm14, [rsp] ;holds first resistance
pop rax

;----------prompt for second resistance--------

mov rax, 0
mov rdi, resistance2 ;second resistance question
call printf


push qword 0
mov rax, 1
mov rdi, floatformat2 ;sets up in float format.
mov rsi, rsp
call scanf
movsd xmm13, [rsp] ;holds our second resistance
pop rax

;---------math part--------------------------------

;add resistance to get total
mov rax, 1
cvtsi2sd xmm12, rax ;stored 1.0
mov rax, 1
cvtsi2sd xmm11, rax ;stored 1.0
mov rax, 1
cvtsi2sd xmm10, rax ;stored 1.0

;1/R = 1/r1 + 1/r2
divsd  xmm12, xmm13 ; 1/r1 

divsd xmm11, xmm14 ; 1/r2

addsd xmm11, xmm12 ; 1/r1 + 1/r2

divsd xmm10, xmm11 ; 1/(1/r1 + 1/r2) = R

push qword 0
mov rax, 1 ;used to signify we are using a value such as xmm0
mov rdi, totalresistance ;message total resistance
movsd xmm0, xmm10 ;sets our total resistance to xmm0 which will be called in our printf
call printf

pop rax

;---------------end of math part --------------

mov rax, 0 
mov rdi, computerscience ;message asking if you are a computer scientist 
call printf


push qword 0
mov rax, 1 ;we are passing in an argument to be scanned
mov rdi, charformat ;sets up in char format since we are only taking in a 'y' or 'n'
mov rsi, rsp 
call scanf ;sets up entering in 'y' or 'n' for yes and no
pop rax

mov r14, 'y'

cmp r14, rax ;compares user input 'y' or 'n' with 'y'. If he is a computer scientist it will jump, if not he won't.

je computer_scientist

mov rax, 0x4092C07AE147AE14; 1200.12 in hex
movq xmm15, rax ;moves the address into xmm15

jmp end_of_interview ;jumps to end of interview skipping computer scientist part




computer_scientist:

mov rax, 0x40F57C0E147AE148;88000.88 in hex format, makes it so i can enter a float into a r register.
movq xmm15, rax


jmp end_of_interview



Chris_Sawyer:
mov rax, 0x412E848000000000; 1 million in hex format
movq xmm15, rax;sets value to 1 million, which when called in main will activate chris sawyer prompt.



end_of_interview:
mov rax, 0
mov rdi, exitmessage ;exit message prompt.
call printf

movsd xmm0, xmm15 ;this will return whatever value is needed to be returned, whether it's 0 to indicate chris sawyer, 2 to indicate social major, or 88000.88 to indicate computer scientist.

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







