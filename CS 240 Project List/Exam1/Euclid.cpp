// Author: Richard Gresham
// CPSC 240-7 Test 1
#include <stdio.h>
#include <stdint.h>    //Library not used
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;

extern "C" double distanceio();

int main()
{
 double* distance_number = new double;

 printf("%s", "Welcome to the Euclidean Distance Finder Programmed by Richard Gresham. \n");

*distance_number = distanceio();

printf("The Euclid module received this number %lf ,and has decided to keep it \n", *distance_number);

printf("A 0 will be returned to the operating system. ");

printf("Be safe and well. \n");

printf("Have a great weekend professor. \n");
return 0;




}