#!/bin/bash


#Author: Richard Gresham
#Program name: Sum of an Array


echo "this is program <Sum of an Array>"
#-l Control.lis

echo "Assemble the module Control.asm"
nasm -g -gdwarf -f elf64 -l Control.lis -o Control.o Control.asm

echo "Compile the C++ module Display.cpp"
g++ -g -c -m64 -Wall -o Display.o Display.cpp -fno-pie -no-pie -std=c++17

echo "Assemble the module Fill.asm"
nasm -g -gdwarf -f elf64 -l Fill.lis -o Fill.o Fill.asm

echo "Assemble the module Sum.asm"
nasm -g -gdwarf -f elf64 -l Sum.lis -o Sum.o Sum.asm

echo "Now compiling Main.c"
gcc -g -c -Wall -m64 -no-pie -o Main.o Main.c -std=c18

echo "Now linking all the o files"
g++ -m64 -no-pie -g -o Arrayio.out Control.o Display.o Fill.o Sum.o Main.o

echo "Run the program Sum of Array"
./Arrayio.out

echo "The bash script file is now closing."
