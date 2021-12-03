#!/bin/bash


#Author: Richard Gresham
#email: rgresham@csu.fullerton.edu
#CS 240-07
rm *.out
rm *.o

echo "this is program <Harmonic Sum>"
#-l Control.lis


echo "Assemble the module HarmonicSum"
nasm -g -gdwarf -f elf64 -l HarmonicSum.lis -o HarmonicSum.o HarmonicSum.asm 

echo "Assemble the module main"
g++ -g -c -m64 -Wall -o main.o main.cpp -fno-pie -no-pie -std=c++17

echo "link all o files"
g++ -m64 -o runio.out HarmonicSum.o main.o -fno-pie -no-pie -std=c++17

echo "Run the program Harmonic Sum"
./runio.out


