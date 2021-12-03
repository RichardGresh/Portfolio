;Author Richard Gresham
;CPSC 240-7 Test 1

;===== Begin code area ========================================================================================================


extern printf
extern scanf

global distanceio


segment .data

input1message db "Please enter the coordinates of the first point seperated by ws: " ,10, 0
input2message db "Please enter the coordinates of the second point seperated by ws: ",10, 0

mathmessage db "The distance between those two points is %lf math units " ,10 ,0
endingmessage db "The distance module will now return that number to the caller module." ,10 , 0
valuestring1 db "%lf" , 0
valuestring2 db "%lf" , 0 

valuestring3 db "%lf" , 0

valuestring4 db "%lf" , 0

stringformat db "%s", 0

segment .bss



segment .text

distanceio:

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



;display outputmessage

mov rax, 0
mov rdi, input1message
call printf


;Begin scan f block 

push qword 0
mov rax, 0
mov rdi, valuestring1
mov rsi, rsp
call scanf
movsd xmm15, [rsp]

pop rax

;scan f block 2
push qword 0
mov rax, 0
mov rdi, valuestring2
mov rsi, rsp
call scanf
movsd xmm14, [rsp]

pop rax

mov rax, 0
mov rdi, input2message
call printf

;scanf block
push qword 0
mov rax, 0
mov rdi, valuestring3
mov rsi, rsp
call scanf
movsd xmm13, [rsp]

pop rax



;scanf 2nd part
push qword 0
mov rax, 0
mov rdi, valuestring4
mov rsi, rsp
call scanf
movsd xmm12, [rsp]



;======================Arithmatic part===================================

;distance between A and B is √(𝑎1−𝑏1)^2+(𝑎2−𝑏2)^2

subsd xmm15, xmm13  ;a1 - b1

mulsd xmm15, xmm15 ; (a1-b1)^2

subsd xmm14, xmm12 ;a2-b2

mulsd xmm14, xmm14 ; (a2-b2)^2

addsd xmm15, xmm14 ; (a1-b1)^2 + (a2 - b2) ^2

sqrtsd xmm11, xmm15  ; √(𝑎1−𝑏1)^2+(𝑎2−𝑏2)^2

;============================final messages================================


;output the distance


mov rax, 1
mov rdi, mathmessage
movsd xmm0, xmm11
call printf



mov rax, 0
mov rdi, endingmessage
call printf



pop rax
pop rax

movsd xmm0, xmm11 


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
