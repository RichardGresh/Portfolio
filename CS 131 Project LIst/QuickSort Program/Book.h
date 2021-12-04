#pragma once
#include <string>
class Book
{
	std::string mTitle;
	int mPages;

public:
	Book() {}
	Book(std::string tTitle, int tPages);
	~Book() {}

	std::string GetTitle() {
		return mTitle;
	}

	int GetPages() {
		return mPages;
	}
	struct CompareByPages {
		bool operator() (const Book& first, const  Book& second) const {
			return first.mPages < second.mPages;
		}
	};
	struct CompareByTitle {
		bool operator() (const Book& first, const Book& second) const {
			return first.mTitle < second.mTitle;
		}
	};
	// I want a Title Comparator

	// And I want a Pages Comparator

	// Making a < operator is a little easier, but it only allows you to ever sort in one way.
};

