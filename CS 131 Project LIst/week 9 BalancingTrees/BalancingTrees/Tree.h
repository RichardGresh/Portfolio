#pragma once
#include <list>
#include <iostream> // For debugging

template <typename T>
class Tree
{
	struct TreeNode
	{
		enum BalanceType
		{
			AVL_OK,
			AVL_LEFT_LEFT,
			AVL_LEFT_RIGHT,
			AVL_RIGHT_RIGHT,
			AVL_RIGHT_LEFT
		};
		T mData;
		TreeNode *mLeft;
		TreeNode *mRight;
		int mHeight;

		TreeNode()
		{
			mLeft = nullptr;
			mRight = nullptr;
			mHeight = 0;
		}
		TreeNode(T tData) : TreeNode()
		{
			mData = tData;
			mLeft = nullptr;
			mRight = nullptr;
			mHeight = 0;
		}
		BalanceType GetBalanceType()
		{
			int tLeft = mLeft ? mLeft->mHeight : -1;
			int tRight = mRight ? mRight->mHeight : -1;

			if (tRight - tLeft >= 2)
			{
				//Right...
				int tRightLeft = mRight->mLeft ? mRight->mLeft->mHeight : -1;
				int tRightRight = mRight->mRight ? mRight->mRight->mHeight : -1;

				if (tRightLeft > tRightRight)
					return TreeNode::AVL_RIGHT_LEFT;
				else
					return TreeNode::AVL_RIGHT_RIGHT;
			}
			else if (tLeft - tRight >= 2)
			{
				int tLeftLeft = mLeft->mLeft ? mLeft->mLeft->mHeight : -1;
				int tLeftRight = mLeft->mRight ? mLeft->mRight->mHeight : -1;

				if (tLeftLeft > tLeftRight)
					return TreeNode::AVL_LEFT_LEFT;
				else
					return TreeNode::AVL_LEFT_RIGHT;
			}

			return TreeNode::AVL_OK;
		}
		void UpdateHeight()
		{
			int tLeft = mLeft ? mLeft->mHeight : -1;
			int tRight = mRight ? mRight->mHeight : -1;
			mHeight = tLeft > tRight ? tLeft + 1 : tRight + 1;
		}
	};
	TreeNode *mHead;

	bool BalanceTree(TreeNode *tNode)
	{
		if (tNode == nullptr)
			return false;

		// This is no longer recursive yay!  The logic hasn't changed.  We are just called on a single node now.

		typename TreeNode::BalanceType tCheck = tNode->mLeft ? tNode->mLeft->GetBalanceType() : TreeNode::AVL_OK; // We look ahead one level because if we go down the tree, we can't reconnect back up.  Remove does the same.
		if (tCheck != TreeNode::AVL_OK)
		{
			TreeNode *tTarget = tNode->mLeft;
			if (tCheck == TreeNode::AVL_LEFT_LEFT)
				tNode->mLeft = RotateLeftUp(tTarget);
			else
			{
				tTarget->mLeft = RotateRightUp(tTarget->mLeft);
				tNode->mLeft = RotateLeftUp(tTarget);
			}
			return true;
		}
		tCheck = tNode->mRight ? tNode->mRight->GetBalanceType() : TreeNode::AVL_OK;
		if (tCheck != TreeNode::AVL_OK)
		{
			TreeNode *tTarget = tNode->mRight;
			if (tCheck == TreeNode::AVL_RIGHT_RIGHT)
				tNode->mRight = RotateRightUp(tTarget);
			else
			{
				tTarget->mRight = RotateLeftUp(tTarget->mRight);
				tNode->mRight = RotateRightUp(tTarget);
			}
			return true;
		}

		if (tNode == mHead)// Nobody could look ahead at us since we are at the top.  So head is a special case
		{
			typename TreeNode::BalanceType tCheck = mHead->GetBalanceType();
			if (tCheck != TreeNode::AVL_OK)
			{
				if (tCheck == TreeNode::AVL_LEFT_LEFT)
					mHead = RotateLeftUp(mHead);
				else if (tCheck == TreeNode::AVL_LEFT_RIGHT)
				{
					mHead->mLeft = RotateRightUp(mHead->mLeft);
					mHead = RotateLeftUp(mHead);
				}
				else if (tCheck == TreeNode::AVL_RIGHT_RIGHT)
					mHead = RotateRightUp(mHead);
				else
				{
					mHead->mRight = RotateLeftUp(mHead->mRight);
					mHead = RotateRightUp(mHead);
				}
				return true;
			}
		}

		return false;
	}

	// Part two of the balance homework needs you to update the heights of the nodes when you do these rotations.
	TreeNode *RotateRightUp(TreeNode *tNode)
	{
		// Using variable names from book pg 257 to make easier to read:
		TreeNode *P = tNode;
		TreeNode *Q = P->mRight;

		P->mRight = Q->mLeft;
		Q->mLeft = P;

		// Need to keep this up to date so Balance and Measure don't need to be recursive.
		// Draw this out and you'll see which nodes actually end up with a different height.
		P->UpdateHeight();

		return Q;
	}

	TreeNode *RotateLeftUp(TreeNode *tNode)
	{
		TreeNode *P = tNode;
		TreeNode *Q = P->mLeft;

		P->mLeft = Q->mRight;
		Q->mRight = P;

		P->UpdateHeight();

		return Q;
	}

	void CopyTree(TreeNode *tNode)
	{
		if (tNode != nullptr)
		{
			Add(tNode->mData);
			CopyTree(tNode->mLeft);
			CopyTree(tNode->mRight);
		}

	}
	void DeleteTree(TreeNode *tNode)
	{
		if (tNode != nullptr)
		{
			DeleteTree(tNode->mLeft);
			DeleteTree(tNode->mRight);
			delete tNode;
		}
	}
	void DumpTree(std::list<T> *tLeftToRight, TreeNode *tNode, int tLevel, bool tWithDebug) const
	{
		if (tNode != nullptr)
		{
			std::string tSpaces = "";
			for (int i = 0; i < 10 * tLevel; i++)
				tSpaces.append(" ");

			DumpTree(tLeftToRight, tNode->mRight, tLevel + 1, tWithDebug);

			// To help debug avl balancing, I'm going to make this thing output.  THis is generally a naughty thing to do outside of main because it makes a dependency between your code and the console.
			if(tWithDebug)
				std::cout << tSpaces << tNode->mData << "\n";

			if (tLeftToRight)
				tLeftToRight->push_front(tNode->mData);

			DumpTree(tLeftToRight, tNode->mLeft, tLevel + 1, tWithDebug);
		}
	}
	void PrivateRemove(TreeNode **tNodePtr)
	{
		// Speaking of, now we are changing it to a double pointer.  Arg is pointing at the last pointer before the change.
		// int x = Process(x); 
		// Process(&x);
		// Those are the same.  That's all this is.

		TreeNode *tNode = (*tNodePtr);
		if (tNode->mLeft == nullptr && tNode->mRight == nullptr)
		{
			delete tNode;
			(*tNodePtr) = nullptr;
		}
		else if (tNode->mLeft != nullptr && tNode->mRight == nullptr)
		{
			TreeNode *tSubRoot = tNode->mLeft;
			delete tNode;
			(*tNodePtr) = tSubRoot;
		}
		else if (tNode->mLeft == nullptr && tNode->mRight != nullptr)
		{
			TreeNode *tSubRoot = tNode->mRight;
			delete tNode;
			(*tNodePtr) = tSubRoot;
		}
		else
		{
			TreeNode *tNextHighest = tNode->mRight;
			TreeNode *tTrailer = tNextHighest;

			while (tNextHighest->mLeft != nullptr)
			{
				tTrailer = tNextHighest;
				tNextHighest = tNextHighest->mLeft;
			}

			tNode->mData = tNextHighest->mData;// Swap the data

			if (tNextHighest != tNode->mRight)// I went left all the way.
				tTrailer->mLeft = tNextHighest->mRight;// Null if 0 child at end
			else
				tNode->mRight = tNextHighest->mRight;// My right had no lefts, so just jump it.  Might be null.

			delete tNextHighest;
			(*tNodePtr) = tNode;
		}
	}

public:
	Tree()
	{
		mHead = nullptr;
	}
	Tree(const Tree & tOther) : Tree()
	{
		std::list<T> tAllNodes;
		tOther.Dump(&tAllNodes);// I'm using dump instead of copy to intentionally force balances to happen in a reliable order.  Just for grading balances.

		for (auto iter = tAllNodes.begin(); iter != tAllNodes.end(); ++iter)
			Add(*iter);
	}
	Tree & operator= (const Tree & tRHS)
	{
		DeleteTree(mHead);
		mHead = nullptr;

		std::list<T> tAllNodes;
		tRHS.Dump(&tAllNodes);

		for (auto iter = tAllNodes.begin(); iter != tAllNodes.end(); ++iter)
			Add(*iter);

		return *this;
	}
	~Tree()
	{
		DeleteTree(mHead);
	}

	// Add, contain, and remove all want to know the same thing.  Where they should activate.
	// Add wants to know what the new node should attach to, contains just wants to see if it is there, and remove wants to know who to mark dead.

	// So all I did was copy the duplicated code here, remove the add/contain specific code, and return the node.

	// Then for the balance homework, I track the path I took to get to the answer, then I only call Balance on those nodes.
	// I used a list instead of a stack because I wanted to loop through it twice.  Whatever you do is fine.
	TreeNode *PrivateFind(T tWhat, std::list<TreeNode *> *tPath)
	{
		if (mHead == nullptr)
			return nullptr;

		TreeNode *tWalker = mHead;
		tPath->push_front(mHead);	// The pushes are the only thing that changed

		while (true)
		{
			if (tWalker->mData == tWhat)
				return tWalker;
			else if (tWalker->mData > tWhat)
			{
				if (tWalker->mLeft == nullptr)
					return tWalker;
				else
					tWalker = tWalker->mLeft;
				tPath->push_front(tWalker);
			}
			else
			{
				if (tWalker->mRight == nullptr)
					return tWalker;
				else
					tWalker = tWalker->mRight;
				tPath->push_front(tWalker);
			}
		}
	}

	void Add(T tWhat)
	{
		if (mHead == nullptr)
		{
			mHead = new TreeNode(tWhat);
			return;
		}

		// Conceptually a stack makes more sense, but I might need to use it twice.  Can't loop a stack twice - it's destructive
		std::list<TreeNode*> tPath;
		TreeNode *tFound = PrivateFind(tWhat, &tPath);
		if (tFound->mData == tWhat)
			return;// no dupes
		else if (tFound->mData > tWhat)
			tFound->mLeft = new TreeNode(tWhat);
		else
			tFound->mRight = new TreeNode(tWhat);

		// This is the new stuff for the balance homework.
		// Update all the heights up the path, then check for balance all the way up the path.
		// This is optimizing the heck out of the old recursive way provided.
		for (TreeNode *tOne : tPath)
		{
			tOne->UpdateHeight();
			if (BalanceTree(tOne))
				break; // Once I do a fix, nothing above me will change any more.
		}
	}

	bool Contains(T tWhat)
	{
		// No balancing if you are just looking
		std::list<TreeNode*> tPath;
		TreeNode *tFound = PrivateFind(tWhat, &tPath);
		if (tFound->mData == tWhat)
			return true;

		return false;
	}

	// I'm not setting Remove up with PrivateFind since this file is both the answer to last homework and the start of the balance homework.  We're redoing remove to actually delete nodes.
	void Remove(T tWhat)
	{
		// Harder than setting a flag.
		// Start at head.  Handle no head and head hit explicitly since the loop needs to keep a walker and a trailer and head has nothing above it.
		// We are looking one step ahead for the victim so that we have the parent pointer we need to perform surgery

		if (mHead == nullptr)
			return;
		if (mHead->mData == tWhat)
		{
			PrivateRemove(&mHead);// Using a double pointer instead of a return value, see PrivateRemove
		}

		TreeNode *tWalker = mHead;
		std::list<TreeNode*> tPath;
		tPath.push_front(mHead);

		while (true)
		{
			if (tWalker->mData > tWhat)// Want to go left
			{
				if (tWalker->mLeft == nullptr)// Can't
					break;
				else if (tWalker->mLeft->mData == tWhat)// Oh hey, that's the target. I want to point at their surviving node.
				{
					PrivateRemove(&tWalker->mLeft);
					break;
				}
				else // Keep looking
					tWalker = tWalker->mLeft;
				tPath.push_front(tWalker);
			}
			else // There isn't an equals case because if I take the step to the victim node, I don't know how to reconnect.  So stepping is looking ahead instead
			{
				if (tWalker->mRight == nullptr)
					break;
				else if (tWalker->mRight->mData == tWhat)
				{
					PrivateRemove(&tWalker->mRight);
					break;
				}
				else
					tWalker = tWalker->mRight;
				tPath.push_front(tWalker);
			}
		}

		// Same as Add.  Only balance the path and at most one node will balance.
		for (TreeNode *tOne : tPath)
		{
			tOne->UpdateHeight();
			if (BalanceTree(tOne))
				break; // Once I do a fix, nothing above me will change any more.
		}
	}

	void PrintTree() const
	{
		DumpTree(NULL, mHead, 0, true);
		std::cout << std::endl;// Naughty to have output in utility class, but need to debug
	}
	void Dump(std::list<T> *tLeftToRight) const
	{
		DumpTree(tLeftToRight, mHead, 0, false);
	}
};

