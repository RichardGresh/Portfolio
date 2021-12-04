#include <string>
#include <unordered_map>
#include <map>
#include <queue>

class Huffman
{
	// Used in the creation of the tree, but not kept afterwards.  We only keep mProcessed.
	struct HuffNode
	{
		HuffNode *mZero = nullptr; // You can think of it as Left if you want
		HuffNode *mOne = nullptr; // And this is right
		std::string mData; // A single character if this is a leaf, or a collection of all the characters that made this inner node
		std::string mCode; // The 100010100 or whatever std::string.  (Not int or we lose leading 0's)
		int mWeight = 0;

		struct ComparePointers
		{
			bool operator() (HuffNode* &tLHS, HuffNode* &tRHS)
			{
				//???
			}
		};
	};

	// Traveling through a whole tree, so it's recursive
	void RecursiveProcess(HuffNode *tNode, std::string tCodeSoFar)
	{
		// If I have a left, RecursiveProcess them with an extra 0
		// If I have a right, RecursiveProcess them with an extra 1
		// If I have neither, I am real data!  Put me in the real mProcessed map with my code.
	}

public:
	// Returns the number of bytes in the compressed file
	int ProcessFile(std::string tFileName)
	{
		// First read the file one character at a time and make...
		std::unordered_map<std::string, int> tCharCounts;

		// Then iterate that and make HuffNodes for the...
		std::priority_queue<HuffNode*, std::vector<HuffNode*>, HuffNode::ComparePointers> tHeap;
		// Remember in a stl declaration, that's a class name in spot three. Not an object. Objects are in algorithms.

		// Pop off two nodes, combine them in to a new node, and put only that new node back in the queue

		// When the queue is empty, it means you are holding on to the official head node!  
		HuffNode *tHead = nullptr;// Your final pointer parenting everything

		// We need to create the bit std::strings for each leaf node.  Recursively travel down the tree and when you hit a leaf,
		// put that leaf in the official mProcessed map.
		mProcessed.clear();
		RecursiveProcess(tHead, "");

		// CharCounts has the number of each character.  mProcessed has the code for each character.
		// Calculate the final size of the compressed file.
		return 0;
	}

	std::string GetTableDump()
	{
		// Since our final processed data is in a map, we can just iterate it to get the chars out in order

		std::string tAnswer;
		// Loop through the map and make a nice std::string like this:
		//A  010
		//C  1000
		//G  001111
		//.
		//. 
		//.
		return tAnswer;// Main will print this.  Classes shouldn't cout things - not portable
	}
private:

	std::map<std::string, std::string> mProcessed; // Map of character to bit std::string. This is all that is persistent.
	//... If you are going for the extra credit, you'll want another container.  Maybe a reversed map of the same two data?
};




// And now some words from our sponsors.  @!*$&&#^!%#$|~`````````````````
																				