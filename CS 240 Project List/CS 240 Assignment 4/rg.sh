#!/bin/bash


#Author: Richard Gresham
#Program name: rectangle



echo "This is program <Demonstrate Numeric IO>"

echo "Assemble the module interview.asm"
nasm -f elf64 -l interview.lis -o interview.o interview.asm -g -gdwarf

echo "Compile Main.cpp"
g++ -c -m64 -Wall -o Main.o Main.cpp -fno-pie -no-pie -std=c++17 -g

echo "Link the two object files already created"
g++ -m64 -o interviewi.out interview.o Main.o -fno-pie -no-pie -std=c++17 -g

echo "Run the GDB for the program interview."
echo "Build process complete."





echo "The bash script file is now closing."