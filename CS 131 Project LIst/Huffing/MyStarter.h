#pragma once
#include <string>
#include <unordered_map>
#include <map>
#include <queue>
#include <fstream>
#include <iostream>
#include <vector>
#include <sstream>
class Huffman
{
	// Used in the creation of the tree, but not kept afterwards.  We only keep mProcessed.
	struct HuffNode
	{
		HuffNode* mZero = nullptr; // You can think of it as Left if you want
		HuffNode* mOne = nullptr; // And this is right
		std::string mData; // A single character if this is a leaf, or a collection of all the characters that made this inner node
		std::string mCode; // The 100010100 or whatever std::string.  (Not int or we lose leading 0's)
		int mWeight = 0;

		struct ComparePointers
		{
			bool operator() (HuffNode*& tLHS, HuffNode*& tRHS)//compares our numbers and gives our best one priority, done by weight.
			{
				if (tLHS->mWeight == tRHS->mWeight)
				{
					return tLHS->mData > tRHS->mData;
				}
					return (tLHS->mWeight) > (tRHS->mWeight);


			}
		};
	};

	// Traveling through a whole tree, so it's recursive
	void RecursiveProcess(HuffNode* tNode, std::string tCodeSoFar)
	{
		
		if (tNode->mZero != nullptr) // If I have a left, RecursiveProcess them with an extra 0
		{
			
			RecursiveProcess(tNode->mZero, tCodeSoFar + "0"); 
		}
		// If I have a right, RecursiveProcess them with an extra 1
		if (tNode->mOne != nullptr)
		{
		RecursiveProcess(tNode->mOne, tCodeSoFar + "1");
		}
		// If I have neither, I am real data!  Put me in the real mProcessed map with my code.

		if (tNode->mOne == nullptr && tNode->mZero == nullptr) 
		{
			mProcessed.insert(std::pair<std::string, std::string>(tNode->mData, tCodeSoFar));
		}
		
		
		
	}

public:
	// Returns the number of bytes in the compressed file
	int ProcessFile(std::string tFileName)
	{
		// First read the file one character at a time and make...
		
		
		std::unordered_map<std::string, int> tCharCounts;
		for (int i = 0; i < 255; i++)
		{
			tCharCounts[std::string(1, (char)i)] = 0;
		}

		std::ifstream fin;
		fin.seekg(0, std::ios::beg);
		fin.open(tFileName); //opens file
		while (!fin.eof()) //reads through file incrementing the value of our unordered map which is count.
		{
			char tChar;
			fin.get(tChar);
			std::string tFound(1, tChar);
			tCharCounts[tFound] += 1;
		}
		fin.close(); //closes file to prevent memory leaks.
		// Then iterate that and make HuffNodes for the...
		std::priority_queue<HuffNode*, std::vector<HuffNode*>, HuffNode::ComparePointers> tHeap;
		std::vector<HuffNode*> Huff;
		// Remember in a stl declaration, that's a class name in spot three. Not an object. Objects are in algorithms.

		
		
		for (auto titer = tCharCounts.begin(); titer != tCharCounts.end(); titer++) //iterates through tCharCounts
		{
			HuffNode* temp = new HuffNode; //creating new HuffNodes that will take in mData and mWeight
			
			temp->mData = titer->first;

			temp->mWeight = titer->second;
			if (temp->mWeight > 0) //only push in the characters that actually appeared in our file.
			{
				
				tHeap.push(temp); 
			}
		
		}
		HuffNode* tHead = nullptr; //our head pointer used for recursive function.
		
		while (!tHeap.empty()) //while our heap isn't empty loop through it.
		{
			HuffNode* root = new HuffNode; //creates a new node that we are essentially putting back into the queue.
			
			root->mWeight = 0;
			root->mZero = tHeap.top(); //gives us our zero and one pointers.
			root->mData = tHeap.top()->mData; //takes in our character into root.
			root->mWeight += tHeap.top()->mWeight;//assigns weight to our root
			tHeap.pop(); //pops our top so we can access our next top
			root->mOne = tHeap.top(); //rinse and repeat of above.
			root->mData += tHeap.top()->mData;
			root->mWeight += tHeap.top()->mWeight;
			tHeap.pop();
			if(!tHeap.empty()) //if theap not empty we push back in and run again.
			tHeap.push(root);
			if (tHeap.empty()) //if it's empty we don't need to push back in as we have our head.
			{
				tHead = root;
			}

		
		}
		
		
		// We need to create the bit std::strings for each leaf node.  Recursively travel down the tree and when you hit a leaf,
		// put that leaf in the official mProcessed map.
		
		mProcessed.clear(); //clears our map.

		RecursiveProcess(tHead,""); //puts our head into recursive function.
		 long int tBits = 0;
		for (auto tIter = mProcessed.begin(); tIter != mProcessed.end(); tIter++)
		{
			int i = tIter->second.length();
			
			 long int j = i * tCharCounts[tIter->first]; //frequency times the number of bits.
			tBits += j;
			
		}
		// CharCounts has the number of each character.  mProcessed has the code for each character.
		// Calculate the final size of the compressed file.
		return tBits;
	}
	

	std::string GetTableDump()
	{
		 std::string tTable[32] = {
		"NUL", "SOH", "STX" ,"ETX", "EOT", "ENQ","ACK","BEL","backspace", "TAB", "NewLine", "VT", "FF", "CR", "SO", "SI", "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN"
		"ETB", "CAN","EN","SUB","ESC","FS","GS","RS","US", };
		// Since our final processed data is in a map, we can just iterate it to get the chars out in order
		std::string tAnswer;
		
		for (auto tIter = mProcessed.begin(); tIter != mProcessed.end(); tIter++)
		{
			bool flag = true;//prevents duplicate coding
			for (int i = 0; i < 32; i++) //goes through the first set of invisible characters and imputs an actual name to it.
			{
				if (tIter->first == std::string(1, (char)i)) //checks if it's an invisible character.
				{
					flag = false;
					tAnswer += tTable[i] + "  " + tIter->second + "\n";
				}
			}
			if (tIter->first == std::string(1, (char)32))
			{
				std::string b = "Space";//need to create std::string so that it can read it as a string
					flag = false; 
					tAnswer += b + "  " + tIter->second + "\n";
			}
			if (tIter->first == std::string(1, (char)127))
			{
				std::string b = "DEL"; //replaces the blank one with DEL
				flag = false;
				tAnswer += b + "  " + tIter->second + "\n";
			}
			if(flag == true)
			tAnswer += tIter->first + "  " + tIter->second + "\n"; //adds on a string holding our output table.
			
		}
		tTable->clear();
		mProcessed.clear();
		return tAnswer;
		// Loop through the map and make a nice std::string like this:
		//A  010
		//C  1000
		//G  001111
		//.
		//. 
		//.
		// Main will print this.  Classes shouldn't cout things - not portable
	}
private:

	std::map<std::string, std::string> mProcessed; // Map of character to bit std::string. This is all that is persistent.
	//... If you are going for the extra credit, you'll want another container.  Maybe a reversed map of the same two data?
};




// And now some words from our sponsors.  @!*$&&#^!%#$|~`````````````````

