// GraphStart.cpp : Defines the entry point for the console application.
//


#include "Graph.h"
#include <iostream>

using namespace std;

int main()
{
	Graph myGraph;
	myGraph.Add("A");
	myGraph.Add("B");
	myGraph.Add("C");
	myGraph.Add("D");
	myGraph.Add("E");
	myGraph.Add("F");
	myGraph.Add("G");

	myGraph.Connect("A", "B", 4);
	myGraph.Connect("A", "C", 1);
	myGraph.Connect("B", "D", 3);
	myGraph.Connect("C", "F", 7);
	myGraph.Connect("C", "G", 10);
	myGraph.Connect("D", "E", 1);
	myGraph.Connect("E", "F", 2);
	myGraph.Connect("F", "G", 1);

	myGraph.Dump();

	std::list<std::string> path;
	cout << "Path A to G is 9: " << myGraph.BestDistance("A", "G", &path) << endl;
	for (auto step : path)
		cout << step << " ";
	cout << endl;
	cout << "Path A to F is 8: " << myGraph.BestDistance("A", "F", &path) << endl;
	for (auto step : path)
		cout << step << " ";
	cout << endl;
	cout << "Path B to C is Fail: " << myGraph.BestDistance("B", "C", &path) << endl;
	for (auto step : path)
		cout << step << " ";
	cout << endl;

	myGraph.Disconnect("F", "G");
	cout << "Path A to G is now 11: " << myGraph.BestDistance("A", "G", &path) << endl;
	for (auto step : path)
		cout << step << " ";
	cout << endl;
	cout << "There is " << (myGraph.HasLoop() ? "a bug." : "not a loop.") << endl;//if true print a bug, if not print not a loop. shouldn't be a bug since the Disconnect doesn't prevent our graph from accessing it.
	myGraph.Connect("G", "A", 5);
	cout << "There is now " << (myGraph.HasLoop() ? "a loop." : "a bug.") << endl;

	myGraph.Dump();

	myGraph.Disconnect("G", "A");
	
	cout << "Max Flow A to G is 1: " << myGraph.MaxFlow("A", "G") << endl;
	myGraph.Connect("B", "E", 20);
	myGraph.Connect("E", "G", 5);
	cout << "Max Flow A to G is now 5: " << myGraph.MaxFlow("A", "G") << endl;

	myGraph.Dump();

	Graph answerGraph;
	int value = myGraph.FindMinimalCover(&answerGraph);
	cout << "Minimal Cover dump with value 16: " << value << endl;
	answerGraph.Dump();
	myGraph.Connect("A", "F", 2);
	value = myGraph.FindMinimalCover(&answerGraph);
	cout << "Minimal Cover dump with new value 14: " << value << endl;
	answerGraph.Dump();

	system("pause");

	return 0;
}

