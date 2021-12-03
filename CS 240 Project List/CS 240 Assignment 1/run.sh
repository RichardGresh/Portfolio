#!/bin/bash


#Author: Richard Gresham
#Program name: rectangle

rm *.o
rm *.out

echo "This is program <Demonstrate Numeric IO>"

echo "Assemble the module perimeter.asm"
nasm -f elf64 -l perimeter.lis -o perimeter.o perimeter.asm

echo "Compile rectangle.cpp"
g++ -c -m64 -Wall -o rectangle.o rectangle.cpp -fno-pie -no-pie -std=c++17

echo "Link the two object files already created"
g++ -m64 -o perimeterio.out perimeter.o rectangle.o -fno-pie -no-pie -std=c++17

echo "Run the program Basic Float Operations"
./perimeterio.out 

echo "The bash script file is now closing."