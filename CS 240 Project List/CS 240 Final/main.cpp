
//;Richard Gresham
//;rgresham@csu.fullerton.edu
//;CS 240-7
//
//

//===== Begin code area ============================================================================================================

#include <stdio.h>
#include <stdint.h>    //Library not used
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

extern "C" double HarmonicSumio();



int main()
{


double sumofHarmonics = 0.0;

sumofHarmonics = HarmonicSumio();

cout << fixed;
cout << setprecision(9);
cout << "The main program received this number and will keep it: " << sumofHarmonics << endl;



return 0;

}