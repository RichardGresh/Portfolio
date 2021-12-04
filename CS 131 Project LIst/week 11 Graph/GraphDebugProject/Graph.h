#pragma once
#include <string>
#include<list>
#include<unordered_map>
#include<iostream>
#include <queue>
#include <map>

/*****************************************************************************************************************************************

This copy of Graph is intentionally broken.  The assignment is to read and understand it so you can debug and fix it.
It doesn't compile, first of all.  But then when you fix that the algorithm implementations are also wrong.

****************************************************************************************************************************************/

// 		for( auto iter = container.begin(); iter != container.end(); ++iter ) {
// I can't stress enough how important that line is.  Every container has the ability to be looped through.  It's one of the reasons we have containers.
// But why do I access the item with (*iter) instead of iter-> ?  Because if your container is full of pointers you can't do iter->->, but you can do (*iter)->

class Graph {
	struct Edge;
	struct Vertex {
		std::string _data;		// Could make the data a T, but it's an extra step we don't really need.  And by not being a template it is easier to debug.  (Hey, you should start every template homework as not template and change it after!
		std::list<Edge*> _ins; //what arrow points to us.
		std::list<Edge*> _outs; //what our vertex arrow is pointing to

		int _hasLoopIns;// Used by HasLoopInternal
	};
	struct Edge {
		int _weight; //our edge pathing cost
		Vertex* _from;
		Vertex* _to;
	};
	std::unordered_map<std::string, Vertex*> _mainData;// We want lookup speed, not range searching, so we didn't pick Map

	bool HasLoopInternal() //gonna keep track of how many hasLoopins are pointing at someone.
	{
		// The style of solution where you modify the components themselves.  You can clean up after or just init each time.
		for (auto mapIter = _mainData.begin(); mapIter != _mainData.end(); ++mapIter) {
			//loops through the data. with the Iterator looking at the second part of map the value
			//its a vertex pointer, uses pointer to change int hasloopvalue to keep track of how many edges are pointing to it.
			
			(*mapIter).second->_hasLoopIns = (*mapIter).second->_ins.size();
			

			
		}

		bool found = false;
		do {
			for (auto mapIter = _mainData.begin(); mapIter != _mainData.end(); ++mapIter) {
				found = false;
				
				Vertex* current = (*mapIter).second; //looking at the vertex (in map) we are currently on (in for loop)
				
				if (current->_hasLoopIns == 0) {  //if it has orignally no  sides
				//outer Iter is looking at current Vertex's LIST of edges that current Vertex is pointing out to
					for (auto outIter : current->_outs) { //enhanced for loop.
						(*outIter)._to->_hasLoopIns--; //decrementing our counter of edges pointing to it.
						
					}
					
						current->_hasLoopIns = 0;
						found = true;
						break;
				
				}
			}
			break;
		} while (!found);

		for (auto mapIter = _mainData.begin(); mapIter != _mainData.end(); ++mapIter) {//looping through the data stating 
			 
			if ((*mapIter).second->_hasLoopIns > 0)//if there are more than 0 has loopin's then its a loop
			{
				
				return true;
			}
		}

		return false;
	}

	bool HasLoopExternal()
	{
		// The kind of solution where you use an external score pad to keep track of the algo's progress.
		std::map<std::string, int> hasLoopIns;

		for (auto mapIter = _mainData.begin(); mapIter != _mainData.end(); ++mapIter) { //loops through the data stating that hasLoopsin key is equal to its value ins size.
			hasLoopIns[(*mapIter).first] = (*mapIter).second->_ins.size();
		}

		bool found = false;           //sets bool found to false
		do {
			for (auto iter = hasLoopIns.begin(); iter != hasLoopIns.end(); ++iter) { //loops through hasloopsin map.
				found = false;
				if ((*iter).second == 0) { //if its value equals 0
					Vertex* current = _mainData[(*iter).first]; //set our pointer to it
					for (auto outIter : current->_outs) { //for loop through our edges
						hasLoopIns[(*outIter)._to->_data] = hasLoopIns[(*outIter)._to->_data] - 1; //decrements it by 1.
					}
					if (hasLoopIns[current->_data] > 0) //if it is greater than one.
					{
						found = true; //set found to true
						break; //exit the loop.
					}
				}
			}
		} while (found); //while there is still data

		for (auto iter = hasLoopIns.begin(); iter != hasLoopIns.end(); ++iter) {
			if ((*iter).second > 0) //if value is greater than 0 we know its true.
				return true;
		}

		return false; //else return false.
	}

	bool HasLoopCopy()
	{
		// The type of solution where you make a whole copy of the graph so you can mangle it and throw it away.
		Graph copyGraph = *this; //makes a graph copy.

		std::queue<Vertex*> myQueue;
		for (std::unordered_map<std::string, Vertex*>::iterator mapIter = copyGraph._mainData.begin(); mapIter != copyGraph._mainData.end(); ++mapIter) { //goes through an unordered map iterator mapIter that runs throuhg copyGraph.
		
			if (mapIter->second->_ins.size() == 0) {           //if vertex size is equal to 0, push it into the queue.
				
				myQueue.push(mapIter->second);
			}
		}
		
		while (myQueue.size() != 0) { //while the vertex queue is not empty.
			Vertex* topVertex = myQueue.front(); //set a vertex pointer to the front of the queue.
			for (std::list<Edge*>::iterator edgeIter = topVertex->_outs.begin(); edgeIter != topVertex->_outs.end(); ++edgeIter) {//goes through my vertex's out's begin to end. 
				if ((*edgeIter)->_to->_ins.size() == 1) { //if number of arrows pointing toward me is one push it into my edgequeue.
					myQueue.push((*edgeIter)->_to);
				}
			}
			myQueue.pop(); //pop to empty the queue.
			copyGraph.Remove(topVertex->_data); //remove the data inside of topVertex.
		}
		if (copyGraph._mainData.size() == 0) //if size of my copyGraph is 0 return false else true.
			return false;
		else
			return true;
	}

public:
	Graph() { //big 3. copy assignment and delete.
	}
	Graph(const Graph& other) { //copy constructor
		for (std::unordered_map<std::string, Vertex*>::const_iterator mapIter = other._mainData.begin(); mapIter != other._mainData.end(); ++mapIter) {//while going through the iterator of our unordered map add first piece of data.
			Add(mapIter->first);
		}
		for (std::unordered_map<std::string, Vertex*>::const_iterator mapIter = other._mainData.begin(); mapIter != other._mainData.end(); ++mapIter) {//this connects our vertexes together.
			for (auto inIter : mapIter->second->_ins) {
				Connect(inIter->_from->_data, inIter->_to->_data, inIter->_weight);
			}
			for (auto outIter : mapIter->second->_outs) { 
				Connect(outIter->_to->_data, outIter->_from->_data, outIter->_weight);
			}
		}
	}
	Graph& operator = (const Graph& tRhs) { //Assignment Constructor
		Clear(); //clears the original graph and assigns new values to it plus connects the path together.
		for (auto mapIter = tRhs._mainData.begin(); mapIter != tRhs._mainData.end(); ++mapIter) {
			Add(mapIter->first);
		}
		for (auto mapIter = tRhs._mainData.begin(); mapIter != tRhs._mainData.end(); ++mapIter) {
			for (auto inIter : mapIter->second->_ins) {
				Connect(inIter->_from->_data, inIter->_to->_data, inIter->_weight);
			}
			for (auto outIter : mapIter->second->_outs) {
				Connect(outIter->_to->_data, outIter->_from->_data, outIter->_weight);
			}
		}
		return *this;
	}
	~Graph() { //destructor clears the graph.
		Clear(); //clear to delete the graph.
	}
	void Clear() { //clear should empty out and delete our graph. 
		for (auto mapIter = _mainData.begin(); mapIter != _mainData.end(); ++mapIter) {
			int amountLoop = mapIter->second->_ins.size();
			for (int i = 0; i < amountLoop; i++) { //when it loops through the entire grpah.
				Edge* tempEdge = mapIter->second->_ins.front();
				Disconnect(tempEdge->_from->_data, tempEdge->_to->_data); //disconnects the data in our data.
			}
		}
		int amountLoop = _mainData.size(); //make it equal to size of graph data.
		for (int i = 0; i < amountLoop; i++) { //while looping through delete everything in our mainData.
			delete _mainData[_mainData.begin()->first];
			_mainData.erase(_mainData.begin());
		}
	}
	void Add(std::string nodeName) {
		if (_mainData.find(nodeName) != _mainData.end())// Reject dupes
			return;
		Vertex* newVert = new Vertex();
		
		newVert->_data = nodeName; //added newVert->_data = nodeName; which added nodename into its data, then set _mainData[nodeName] = to it.
		_mainData[nodeName] = newVert;
		
	}
	void Remove(std::string nodeName) {
		if (_mainData.find(nodeName) == _mainData.end())// Stop if we don't have it
			return;
		for (auto inIter : _mainData[nodeName]->_ins) {// Since the vertex is going, all edges in and out are going, so tell the vertices at the other end
			inIter->_from->_outs.remove(inIter);
			delete inIter;
		}
		for (auto outIter : _mainData[nodeName]->_outs) {
			outIter->_to->_ins.remove(outIter);
			delete outIter;
		}
		delete _mainData[nodeName];
		_mainData.erase(nodeName);
	}
	void Connect(std::string from, std::string to) {// "Overloading" like this prevents copypaste, and the BestDistance method needs weights
		Connect(from, to, 1);
	}
	void Connect(std::string from, std::string to, int weight) {
		if (_mainData.find(from) == _mainData.end() || _mainData.find(to) == _mainData.end()) // Check if both exists if start or end do not exist it will exit the function. 
			return;

		Edge* newEdge = new Edge();			// One edge exists per arrow on the white board.  Each vertex has a pointer to it
		newEdge->_weight = weight;			//sets the weight of the edge on arrow.
		newEdge->_from = _mainData[from];  //sets newEdge from = to main data from. thus linkinng them
		newEdge->_to = _mainData[to];   //does the same as above.

		_mainData[from]->_outs.push_back(newEdge); //changed to to from
		_mainData[to]->_ins.push_back(newEdge);    //changed from to to.
	}
	void Disconnect(std::string from, std::string to) { //removes the arrow pointing from one another thus making it unaccessable from there.
		if (_mainData.find(from) == _mainData.end() || _mainData.find(to) == _mainData.end())
			return;
		for (auto inIter : _mainData[to]->_ins) {// Disconnecting leaves the vertices in place, but deletes the edge after removing it
			if (inIter->_from == _mainData[from]) {
				inIter->_from->_outs.remove(inIter);
				_mainData[to]->_ins.remove(inIter);
				delete inIter;
				break;
			}
		}
	}
	void Dump() { //prints out the ins and outs of the program telling you what your vertex points to and from.
		for (auto mapIter : _mainData) {
			std::cout << mapIter.first << ") Ins:";  
			for (auto inIter : mapIter.second->_ins)
				std::cout << inIter->_from->_data << " ";
			std::cout << "Outs: ";
			for (auto outIter : mapIter.second->_outs)
				std::cout << outIter->_to->_data << " ";
			std::cout << std::endl;
		}
		std::cout << std::endl;
		std::cout << std::endl;
		std::cout << std::endl;
	}

	bool HasLoop() {
		return HasLoopInternal() && HasLoopExternal() && HasLoopCopy(); //if all three are true essentially it could be a bug or a loop.
	}

	int BestDistance(std::string from, std::string to) {
		return BestDistance(from, to, nullptr);// Overloading again in case you don't need the path.
	}
	int BestDistance(std::string from, std::string to, std::list<std::string>* path) {
		std::map<std::string, int> currentDistance; //map that holds the string name and distance value, used to get our current value/distance
		std::map<std::string, std::string> previousNode; //map that has the data from our previous node
		std::map<std::string, bool> processed;// map that tells us if our point is processed or not.
		
		for (auto mapIter = _mainData.begin(); mapIter != _mainData.end(); ++mapIter) { //looping through the program
			
			currentDistance[(*mapIter).first] = INT_MAX; //setting current distance map to its max value
			previousNode[(*mapIter).first] = "";        //setting previous node's string to ""
			processed[(*mapIter).first] = false;//setting the processed flag in false to true.
			
		}
		currentDistance[from] = 0;  //set my first node that I start with to zero.
		
		bool found = false; //found equal to false.
		do {                         
			int bestDistance = INT_MAX; //set bestDistance to max int.
			std::string bestVertex = "";
		

			found = false;
			for (auto mapIter = _mainData.begin(); mapIter != _mainData.end(); ++mapIter) //loop through our data
			{
			
				if (currentDistance[(*mapIter).first] < bestDistance && processed.at((*mapIter).first) == false) { //if our currentDistance is less than our best one
					found = true; //we found it.
					bestDistance = currentDistance[(*mapIter).first]; //set our bestdistance to it. BestDistance could be weight.
					bestVertex = (*mapIter).first;//let our program know who had the best distance
					
					
					
			
					
				}
			}
	
			if (found) { //if a better distance was found.
				Vertex* current = _mainData[bestVertex];//set our pointer equal to its current location
				
				processed[current->_data] = true; //set this node's processed to true
				for (auto outIter : current->_outs) {


					int potential = currentDistance[current->_data] + outIter->_weight; //add on our weight to the vertex's data.


				
					if (potential < currentDistance[(*outIter)._to->_data]) { //if the potential data is less than the current distance data.
						
						currentDistance[(*outIter)._to->_data] = potential; //set the current distance map's data 
						
						previousNode[(*outIter)._to->_data] = bestVertex;//and set the previous node's list to data to bestVertex.
				
						
					}
					
				}
				

				
			}
			if (!found && currentDistance[to] == INT_MAX) //if you haven't found it and the value in your endgoal is still int_max it means that it must never meet it on the path thus it fails.
			{
				path->clear(); //clears the path
				return -1; //since it's an int i couldn't just put fail so i made it -1 to convey that it failed.
			}
			
			
			
		} 
		while (processed.at(to) == false);//when everying is processed exit the loop.;;;
		
		if (path) { //if there is a path.
			path->clear(); //clear the old one.
			if (previousNode[to] != "") { //if to value doesn't equal ""
				std::string walker = to; //set walker eqyal to to.
				path->push_front(to); //and push to into the path //the end
				do { 
					walker = previousNode[walker]; //set walker = to its previous node
					path->push_front(walker); //push that previous one into the path
				} while (walker != from);//while walker doesn't equal our start
			}
		}
		
		return currentDistance[to]; //return our current distance map from our ending location which gives us the best distance tooken.
	}

	int MaxFlow(std::string from, std::string to) //algorithm to get maximum flow
	{
		
		return 0;
	}

	int FindMinimalCover(Graph* tAnswer)//algorithm to get minimum flow.
	{
		
		return 0;
	}
};

