#include "pch.h"
#include "Person.h"
#include "HotDog.h"
#include <iostream>

void Person::CheckHotDog(HotDog *tDog)
{
	if (tDog->mCooked)
		std::cout << "Yum" << std::endl;
	else
		std::cout << "You must have gone to the cafeteria" << std::endl;
}

Person::Person()
{
}


Person::~Person()
{
}
