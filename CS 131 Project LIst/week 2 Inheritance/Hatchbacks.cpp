#include "Hatchbacks.h"
#include <iostream>
using namespace std;

void Hatchbacks::Price()
{
	Getprice();
	cout << "The cost of the car is $" << cost << "." << endl;
}
void Hatchbacks::Doors()
{
	Getdoors();
	cout << "The number of doors this car has is " 
		<< numdoors <<"." << endl;

}
void Hatchbacks::Trunk()
{
	Gettrunksize();
	cout << "The size of the turnk in this car is " << trunksize << " cubic feet." << endl;
}

