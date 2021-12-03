;Richard Gresham
;rgresham@csu.fullerton.edu
;CS 240-7

;===== Begin code area ========================================================================================================

extern printf
extern scanf




global HarmonicSumio



Segment .data
prompt1 db "Enter the number of terms desired: " , 0

prompt2 db "Enter the frequency of the processor as positive integer: ",0

intformat1 db "%ld", 0

time1 db "The time is now: %ld ticks" , 10, 0
sol1 db "k = %ld"  ,0
sol2 db "   sum = %.9lf" , 10 , 0

harmonic1 db "The harmonic algorithm executed for a total time = %ld ticks",0
harmonic2 db " on a %ld Hz machine." ,10,0

Segment .bss



Segment .text




HarmonicSumio:


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

push qword 0
mov rax, 0
mov rdi,intformat1
mov rsi, rsp
call scanf
pop rax

mov r12, rax ;holds user input for k of my harmonic sum.

mov rax, 0
mov rdi, prompt2
call printf

push qword 0
mov rax, 0
mov rdi,intformat1
mov rsi, rsp
call scanf

pop rax
mov r11, rax ;holds the processor hz

cvtsi2sd xmm15, r11 ;stores my processor hz since I'm having issues with volatility I'm keeping this in an xmm register and going to convert back to int later.

;gets the value of the cpu clock.
cpuid
rdtsc
shl rdx,32
or rax, rdx

mov r13, rax ;clock speed by ticks

push qword 0
mov rax, 1
mov rdi, time1 ;prints out clock speed
mov rsi, r13
call printf
pop rax





;divide the value user entered by 10 to get when to print every tenth harmonic sum
mov rax, r12
mov r14, 10
cqo 
div r14
mov r14, rax ;this has the tenth value

mov rbp, r14



mov r15, 1

mov rax, 0
cvtsi2sd xmm13, rax ;make sure xmm13 is zero
mov rax, 1
cvtsi2sd xmm14, rax ;set up values for my comparison of xmm14, xmm12 to prevent more than 10 values excluding the final value from printing.
mov rax, 10
cvtsi2sd xmm12, rax


begin_loop:
cmp r15, r12
jg finish_loop


mov rbx, 1
cvtsi2sd xmm10, r15
cvtsi2sd xmm11, rbx

;divide xmm11 by xmm10 as required by formula and add it onto the total value
divsd xmm11, xmm10
addsd xmm13, xmm11

;print out the value every tenth of teh value entered
cmp r15,r14
jne check_ifequal

ucomisd xmm14, xmm12 ;did it so that it didn't print an 11th value such as 77 for a value of 78. It will skip print
ja skip_print

;prints out tenth value of harmonic sum
push qword 0
mov rax, 1
mov rdi, sol1
mov rsi, r15
call printf
pop rax

push qword 0
mov rax, 1
mov rdi, sol2
movsd xmm0, xmm13
call printf
pop rax


skip_print:
mov rax, 1
cvtsi2sd xmm9, rax
addsd xmm14, xmm9 ;increment my xmm counter by 1 so that it won't print more than 10 values excluding the final one.

add r14, rbp ;adds r14 by rbp which both contain a tenth of the code so that the tracker can keep going.

jmp dont_print

check_ifequal:
cmp r15, r12
jne dont_print

push qword 0
mov rax, 1
mov rdi, sol1
mov rsi, r15
call printf
pop rax

push qword 0
mov rax, 1
mov rdi, sol2
movsd xmm0, xmm13
call printf
pop rax

jmp dont_print



dont_print:
inc r15

jmp begin_loop




finish_loop:


;gets the value of the cpu clock.
cpuid
rdtsc
shl rdx,32
or rax, rdx

mov r15, rax


push qword 0
mov rax, 1
mov rdi, time1
mov rsi, r13
call printf
pop rax

sub r15, r13 ;holds total tick ran

push qword 0
mov rax, 1
mov rdi, harmonic1
mov rsi, r15
call printf
pop rax


cvtsd2si r14, xmm15 ;converts my hz back into int



push qword 0
mov rax, 1
mov rdi, harmonic2 ;prints my hz as an int
mov rsi, r14
call printf
pop rax




movsd xmm0, xmm13 ;return sum of Harmonic

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


