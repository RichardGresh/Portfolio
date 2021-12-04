#include <iostream>
#include "Maze.h"
#include<stack>

using namespace std;
int main()
{
	// Tiny little tst case on my hardcoded maze
	Maze tTestMaze;
	std::stack<Maze::Cell*> tPath;
	tPath = tTestMaze.SolveMaze();
	

}
