#include "Maze.h"
#include <iostream>

using namespace std;
Maze::Maze()
{
	// Making a test maze by hand to make testing easy without giving away the extra credit of the maze maker.

	mStart = new Cell;
	mStart->mNorth = new Cell;
	mStart->mNorth->mNorth = new Cell;
	mStart->mEast = new Cell;
	mStart->mEast->mEast = new Cell;
	mStart->mEast->mEast->mNorth = new Cell;
	mStart->mEast->mEast->mNorth->mNorth = new Cell;
	mStart->mEast->mEast->mNorth->mNorth->mIsExit = true;
	// This is the big U I drew on the board.
}


Maze::~Maze()
{
	// Totally leaks
}

bool Maze::MazeRecursive(Maze::Cell* tCurrent, std::stack<Maze::Cell*>* tPath) //exraCredit one records path one takes) //mProcessed tells us that the cell has been done
{
	
	if (tCurrent->mNorth != NULL && tCurrent->mProcessed == false)
	{
		
		tCurrent->mProcessed == true;
	
		tPath->push(tCurrent);
		if (MazeRecursive(tCurrent->mNorth, tPath)) {
			
			return true;
			
		}
	
	}
	if (tCurrent->mSouth != NULL && tCurrent->mProcessed == false)
	{
		tCurrent->mProcessed == true;
		tPath->push(tCurrent);
		if (MazeRecursive(tCurrent->mSouth, tPath)) {
			
			return true;
		}
		
	}

	if (tCurrent->mEast != NULL && tCurrent->mProcessed == false)
	{
		tCurrent->mProcessed == true;
		tPath->push(tCurrent);
		
		if (MazeRecursive(tCurrent->mEast, tPath)) {
			
			return true;
		}
		
	}
	if (tCurrent->mWest != NULL && tCurrent->mProcessed == false)
	{
		tCurrent->mProcessed == true;
		tPath->push(tCurrent);
		
		if (MazeRecursive(tCurrent->mWest, tPath)) {
			
			return true;
		}
			
	
	}
	if (tCurrent->mIsExit == true)
	{
		
		return true;
	}
	
	tPath->pop();
	return false; //this is a stub 



	// This is the main part.  Just keep in mind the single sentence recursive definition:

	// "To exit a maze, I take a step and if I'm not done I exit the maze."

	// Use Processed to prevent loops.  The last cell is marked IsExit.  Using the four direction pointers
	// versus the list is up to you.  "tPath" is there for you to push cell pointers as you move.  If
	// it turns out you didn't find the exit that direction then pop it back off.  The return value
	// of true-false is how you communicate success backwards.

}

std::stack<Maze::Cell*> Maze::SolveMaze()// Driver
{
	// Don't need to change this.
	std::stack<Maze::Cell*> tAnswer;
	MazeRecursive(mStart, &tAnswer);
	return tAnswer;
}