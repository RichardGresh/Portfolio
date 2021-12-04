#pragma once

class HotDog;// Forward declaration/prototype

class Grill
{
public:
	Grill();
	~Grill();
	//Give Grill a method that takes a hotdog pointer
	// returnType name(arg list);
	void CookHotDog(HotDog *tDog);
};

