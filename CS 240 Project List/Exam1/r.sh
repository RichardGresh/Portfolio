
# Richard Gresham
# CPSC 240-7 Test 1
rm *.o
rm *.out

echo "This is program <Euclid Distance>"

echo "Assemble the module Distance.asm"
nasm -f elf64 -l Distance.lis -o Distance.o Distance.asm

echo "Compile Euclid.cpp"
g++ -c -m64 -Wall -o Euclid.o Euclid.cpp -fno-pie -no-pie -std=c++17

echo "Link the two object files already created"
g++ -m64 -o Distanceio.out Distance.o Euclid.o -fno-pie -no-pie -std=c++17

echo "Run the program Basic Float Operations"
./Distanceio.out

echo "The bash script file is now closing."