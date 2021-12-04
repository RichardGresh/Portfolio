
#pragma once
#include <string>
#include<iostream>
using namespace std;
class Student
{
public:
	string myname;
	double gpa;
	double studentDebt;



	Student()
	{

	}

	Student(string name, int gpa, int debt)
	{
		this->myname = myname;
		this->gpa = gpa;
		this->studentDebt = studentDebt;

	}
	
	




	
		
};
bool operator<(const Student& first, const Student& second)
{
	return first.gpa < second.gpa;
}


struct CompareBYDebt
{
	bool operator() (const Student& first, const Student& second)
	{
		return first.studentDebt > second.studentDebt;
	}
};




