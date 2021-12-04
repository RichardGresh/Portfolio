#pragma once
#include "Vehicle.h"
#include <iostream>


using namespace std;
class Sedans :public Vehicle
{
private:
	int cost = 30000;   //private member variables
	int numdoors = 4;
	int trunksize = 20;
public:
	int Getprice()   //getting them from the private member variables to be used in the public methods.
	{
		return cost;
	}
	int Getdoors()
	{
		return numdoors;
	}
	int Gettrunk()
	{
		return trunksize;
	}
	virtual void Doors(); //prototypes of the methods of sedans
	virtual void Price();
	virtual void Trunk();
	
};

