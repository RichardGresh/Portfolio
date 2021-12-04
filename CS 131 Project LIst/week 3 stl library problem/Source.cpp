
#include<iostream>
#include <vector>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include "Student.h"




using namespace std;


int main()
{
	list <int> tnumbers;
	for (int i = 1; i <= 10; i++)
	{
		tnumbers.push_back(i);
	}

	Student* Sarah = nullptr;
	Sarah = new Student;
	Student* Michael = nullptr;
	Michael = new Student;
	Student* Emma = nullptr;
	Emma = new Student;
	Student* Jacob = nullptr;
	Jacob = new Student;

	std::vector <Student*> objects;
	objects.push_back(Sarah);
	objects.push_back(Michael);
	objects.push_back(Emma);
	objects.push_back(Jacob);


	stack<Student*> tstacker;

	for (int i = 0; i < 10; i++)
	{
		Student* aStudent = new Student;

		tstacker.push(aStudent);


	}
	for (int i = 0; i < 10; i++)
	{

		Student* athing = tstacker.top();
		tstacker.pop();
		delete athing;


	}
	set<int> tset;
	for (int i = 0; i < 10; i++)
	{
		tset.insert(i);
	}

	map<string, int> tmap;
	tmap.insert(std::pair<std::string, int>("California", 1));
	tmap.insert(std::pair<std::string, int>("Nevada", 2));

	unordered_map<string, int> tumap;

	tumap.insert(std::pair<std::string, int>("North Dakota", 3));
	tumap.insert(std::pair<std::string, int>("South Dakota", 4));

	priority_queue<Student> tMyGpa;

	tMyGpa.push(Student("Emma", 4, 500));
	tMyGpa.push(Student("Michael", 3, 650));
	tMyGpa.push(Student("Sarah", 2, 600));
	tMyGpa.push(Student("Jacob", 1, 700));

	while (!tMyGpa.empty())
	{
		Student athing = tMyGpa.top();
		tMyGpa.pop();
		cout << athing.myname << " " << athing.gpa << athing.studentDebt << endl;
	}

	priority_queue<Student, vector<Student>, CompareBYDebt> tDebt;

	tDebt.push( Student("Emma", 4, 500));
	tDebt.push( Student("Michael", 3, 650));
	tDebt.push( Student("Sarah", 2, 600));
	tDebt.push( Student("Jacob", 1, 750));
	while (!tMyGpa.empty())
	{

		Student athing = tDebt.top();
		tDebt.pop();
		cout << athing.myname << " " << athing.gpa << " " << athing.studentDebt << endl;



	}
	


}
