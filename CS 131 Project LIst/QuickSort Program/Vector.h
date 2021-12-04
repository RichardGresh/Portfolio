#pragma once
template <typename T>
class Vector
{
	T* mData; // Dynamically allocated array
	int mSize;// In use
	int mCapacity;// Allocated

	void Reserve(int tHowMuch)
	{
		T* tOld = mData;
		mData = new T[tHowMuch];
		for (int i = 0; i < mSize; i++)
		{
			mData[i] = tOld[i];
		}
		mCapacity = tHowMuch;
		if (tOld)
			delete[] tOld;
	}

public:
	Vector()
	{
		mData = nullptr;
		mSize = 0;
		mCapacity = 0;
		Reserve(10);
	}
	Vector(const Vector& tOther)
	{
		mData = nullptr;
		mSize = 0;
		mCapacity = 0;
		Reserve(tOther.mCapacity);

		for (int i = 0; i < tOther.mSize; i++)
		{
			mData[i] = tOther.mData[i];
		}
		mSize = tOther.mSize;
	}
	Vector& operator = (const Vector& tRHS)
	{
		Clear();
		for (int i = 0; i < tRHS.mSize; i++)
		{
			mData[i] = tRHS.mData[i];
		}
		mSize = tRHS.mSize;
		return *this;
	}
	~Vector()
	{
		if (mData)
			delete[] mData;
	}

	void PushFront(const T& tWhat)
	{
		if (mSize == mCapacity)
			Reserve(2 * mCapacity);
		for (int i = mSize; i > 0; i--)
		{
			mData[i] = mData[i - 1];
		}
		mData[0] = tWhat;
		mSize++;
	}
	void PopFront()
	{
		for (int i = 0; i < mSize - 1; i++)
		{
			mData[i] = mData[i + 1];
		}
		mSize--;
	}
	T& Front()
	{
		return mData[0];
	}

	void PushBack(const T& tWhat)
	{
		if (mSize == mCapacity)
			Reserve(2 * mCapacity);
		mData[mSize] = tWhat;
		mSize++;
	}
	void PopBack()
	{
		mSize--;
	}
	T& Back()
	{
		return mData[mSize - 1];
	}

	int Size()
	{
		return mSize;
	}
	void Clear()
	{
		mSize = 0;
	}

	T& At(int tWhere) const
	{
		return mData[tWhere];
	}
	///////////////////////////////////////////////////////////////////Iterators
	class ConstIterator
	{
	public:
		ConstIterator()
		{
			mCurrent = 0;
		}
		ConstIterator(int tStart, Vector<T>* tMyVector)
		{
			mCurrent = tStart;
			mMyVector = tMyVector;
		}
		const T& GetData() const
		{
			return mMyVector->mData[mCurrent];
		}
		void Next()
		{
			mCurrent++;
		}
		bool IsEqual(const ConstIterator& rhs) const
		{
			return mCurrent == rhs.mCurrent && mMyVector == rhs.mMyVector;
		}
	protected:
		int mCurrent;
		Vector<T>* mMyVector;
	};
	class Iterator : public ConstIterator
	{
		friend Vector<T>;
	public:
		Iterator(int tStart, Vector<T>* tMyVector)
		{
			this->mCurrent = tStart;
			this->mMyVector = tMyVector;
		}
		T& GetData()
		{
			return this->mMyVector->mData[this->mCurrent];
		}
	};

	void Erase(Iterator tWhat)
	{
		for (int i = tWhat.mCurrent; i < mSize - 1; i++)
			mData[i] = mData[i + 1];
		mSize--;
	}
	Iterator Begin()
	{
		return Iterator(0, this);
	}
	Iterator End()
	{
		return Iterator(mSize, this);
	}
	ConstIterator Begin() const
	{
		return ConstIterator(0, this);
	}
	ConstIterator End() const
	{
		return ConstIterator(mSize, this);
	}

	// Do note this is not how stl does it.  sort is external to the class since it works with all containers.
	// That is, it is in <algorithm> not <vector>.  I put it here to be a little easier and to show the cool
	// thing of having templated methods in templated classes.
	template<class C>
	void Sort(C tComparator)
	{
		// Note the C is an object.  Sort uses an object, where templates that take a C in their declaration take a class name.
		// map< K, V, C > for instance.
		RecursiveSort(0, mSize - 1, tComparator);
	}

private:
	template<class C>
	void RecursiveSort(int tFrom, int tTo, C tComparator)
	{
		int keeptrack = tTo;


		if (tFrom == tTo) //if tTo and tFrom are in the same place
		{
		
			keeptrack = keeptrack - 1;
			tFrom = 0;
			tTo = keeptrack;
			bool sorted = true;
			for (int i = 0; i < mSize - 1; i++) {
				if (tComparator(mData[i], mData[i + 1])) {
			
				}
				else {
					sorted = false;
					break;
				}
			}
			if (sorted == false) {
				RecursiveSort(tFrom, tTo, tComparator);
			}
			else {
				
			}

		}
		else if (tComparator(mData[tTo], mData[tTo - 1]))
		{
		
			Book temp;
			temp = mData[tTo - 1];
			mData[tTo - 1] = mData[tTo];
			mData[tTo] = temp;
			
			
			
			RecursiveSort(tFrom, tTo, tComparator);
			}
		else if(tComparator(mData[tTo - 1], mData[tTo]))
		{
			
			Book temp;
			temp = mData[tFrom];
			mData[tFrom] = mData[tTo - 1];
			mData[tTo - 1] = temp;

			
			tFrom = tFrom + 1;
			
			RecursiveSort(tFrom, tTo, tComparator);
		}
		

		


		
	};
};

