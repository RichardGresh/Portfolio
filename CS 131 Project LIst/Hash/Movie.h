#pragma once
#include <string>
#include <iostream>

class Movie
{
	std::string mTitle;
	int mYear;
	int mMinutes;

public:
	Movie(std::string tTitle, int tYear, int tMinutes);
	Movie();
	~Movie();

	struct Hashor
	{
		// Remember, you can't use this ascii * 37 loop from the slides.  It only gets a 64 anyway.  (Higher - more unique is better.)
		unsigned int operator()(const Movie& tWhat)
		{
			unsigned int tRunningTotal = 0;
			unsigned int tMagic = 0;
			for (int i = 0; i < tWhat.mTitle.length(); i++)
			{
				tRunningTotal = tRunningTotal ^ (tWhat.mTitle[i]) ;
			for (int i = 0; i < tWhat.mMinutes; i++)
			{
					tMagic = tMagic * i + tWhat.mTitle.length();
					tRunningTotal = tMagic * tRunningTotal + tWhat.mYear;
				}
				
			}

			
			//for (int i = 0; i < tWhat.mTitle.size(); i++)
			//	tRunningTotal = (int)tWhat.mTitle[i] + 37 * tRunningTotal;
			
			
			std::cout << tWhat.mTitle << " : " << tRunningTotal;// Naughty to have console in class.  This is debugging

			return tRunningTotal;
		}
	};
	struct Equalitor
	{
		bool operator()(const Movie& tLHS, const Movie& tRHS)
		{
			return (tLHS.mTitle == tRHS.mTitle) && (tLHS.mYear == tRHS.mYear) && (tLHS.mMinutes == tRHS.mMinutes);
		}
	};
};

