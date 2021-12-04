#include "Sedans.h"
#include <iostream>

using namespace std;

 void Sedans::Price()
{
	Getprice(); //going to receive the price of the sedan from private
	cout << "The cost of the car is $" << cost << "." << endl;
	
}
 void Sedans::Doors()
 {
     Getdoors(); //receive num of doors from private
     cout << "The number of doors is " << numdoors << "." << endl;
 }
 void Sedans::Trunk()
 {
     Gettrunk(); //receive size of trunk from private
     cout << "The size of the trunk is " << trunksize << " cubic feet." << endl;
 }

