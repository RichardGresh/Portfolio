#pragma once
#include <iostream>
#include "Vehicle.h"


using namespace std;

class Hatchbacks :public Vehicle
{
private:
	int cost = 20000;
	int numdoors = 5;
	int trunksize = 30;
public:
	int Getprice()
	{
		return cost;
	}
	int Getdoors()
	{
		return numdoors;
	}
	int Gettrunksize()
	{
		return trunksize;
	}

	virtual void Price();
	virtual void Doors();
	virtual void Trunk();
	


};

