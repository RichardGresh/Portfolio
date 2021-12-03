#!/bin/bash


#Author: Richard Gresham
#Program name: rectangle



echo "This is program <Demonstrate Numeric IO>"

echo "Assemble the module interview.asm"
nasm -f elf64 -l interview.lis -o interview.o interview.asm

echo "Compile Main.cpp"
g++ -c -m64 -Wall -o Main.o Main.cpp -fno-pie -no-pie -std=c++17

echo "Link the two object files already created"
g++ -m64 -o interviewio.out interview.o Main.o -fno-pie -no-pie -std=c++17

echo "Run the program Basic Float Operations"
./interviewio.out

echo "The bash script file is now closing."