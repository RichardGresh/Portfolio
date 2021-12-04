// SortingStub.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Book.h"
#include <iostream>
#include "Vector.h"

using namespace std;
class SortStub // Just leaving this here as an example and to test compiling.  Comparators use () like this.
{
public:
	bool operator()(const int& lhs, const int& rhs)
	{
		return lhs < rhs;
	}
};

int main()
{
	Vector<Book> tMyBooks;
	tMyBooks.PushBack(Book("Hobbit", 287));
	tMyBooks.PushBack(Book("Off to Be the Wizard", 372));
	tMyBooks.PushBack(Book("Harry Potter and the Methods of Rationality", 122));
	tMyBooks.PushBack(Book("Six Wakes", 400));
	tMyBooks.PushBack(Book("The Only Pirate at the Party", 258));
	tMyBooks.PushBack(Book("Cinder", 448));
	tMyBooks.PushBack(Book("Data Structures and Algorithms", 818));
	tMyBooks.PushBack(Book("Battlestations Core Rulebook", 112));
	tMyBooks.PushBack(Book("C++ Early Objects", 1326));

	cout << "As added:" << endl;
	for (auto iter = tMyBooks.Begin(); !iter.IsEqual(tMyBooks.End()); iter.Next())
		cout << "Title: " << iter.GetData().GetTitle() << ", Pages: " << iter.GetData().GetPages() << endl;

	tMyBooks.Sort(Book::CompareByTitle());
	cout << endl << "Sorted on Title:" << endl;
	for (auto iter = tMyBooks.Begin(); !iter.IsEqual(tMyBooks.End()); iter.Next())
		cout << "Title: " << iter.GetData().GetTitle() << ", Pages: " << iter.GetData().GetPages() << endl;

	tMyBooks.Sort(Book::CompareByPages());
	cout << endl << "Sorted on Pages:" << endl;
	for (auto iter = tMyBooks.Begin(); !iter.IsEqual(tMyBooks.End()); iter.Next())
		cout << "Title: " << iter.GetData().GetTitle() << ", Pages: " << iter.GetData().GetPages() << endl;

	return 0;
}