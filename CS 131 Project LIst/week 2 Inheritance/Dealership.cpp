#include <iostream>
#include "Vehicle.h"
#include "Hatchbacks.h"
#include "Sedans.h"

using namespace std;




void SalesPerson(Vehicle* tWhat);


void Accountant(Vehicle* tWhat);


int main()
{
	Sedans* aSedan = nullptr; //sets aSedan and ahatchback pointer to null
	Hatchbacks* aHatchback = nullptr;

	aSedan = new Sedans; //dynamically create object
	aHatchback = new Hatchbacks;
	

	Accountant(aSedan); 
	SalesPerson(aSedan);

	SalesPerson(aHatchback);
	Accountant(aHatchback);

	delete aSedan;
	delete aHatchback;

	aSedan = nullptr;
	aHatchback = nullptr;
}


void SalesPerson(Vehicle* tWhat)
{



}

void Accountant(Vehicle* tWhat)
{
	tWhat->Price();
	tWhat->Doors();
	tWhat->Trunk();
	tWhat->Startcar();
}