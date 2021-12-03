#!/bin/bash


#Author: Richard Gresham
#Program name: Root Calculator

rm *.o
rm *.out

echo "This is program <Root Calculator>"
#-l Quadratic.lis

echo "Assemble the module Quadratic.asm"
nasm -g -f elf64 -l Quadratic.lis -o Quadratic.o Quadratic.asm

echo "Compile the C++ module Quad_library.cpp"
g++ -g -c -m64 -Wall -o Quad_library.o Quad_library.cpp -fno-pie -no-pie -std=c++17

echo "Compile the C++ module isfloat.cpp"
g++ -g -c -m64 -Wall -o isfloat.o isfloat.cpp -fno-pie -no-pie -std=c++17

echo "Now compiling Second_degree.c"
gcc -g -c -Wall -m64 -no-pie -o Second_degree.o Second_degree.c -std=c18

echo "Now linking all the o files"
g++ -m64 -no-pie -o Quadraticio.out Quadratic.o Quad_library.o isfloat.o Second_degree.o 

echo "Run the program Root Calculator"
./Quadraticio.out

echo "The bash script file is now closing."
