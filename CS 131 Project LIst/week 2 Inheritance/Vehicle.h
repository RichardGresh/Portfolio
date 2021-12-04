#pragma once

#include <iostream>
using namespace std;
class Vehicle  //parent class
{



public:
    virtual void Price() = 0;  //pure virtual functions
    virtual void Doors() = 0;
    virtual void Trunk() = 0;
    void Startcar()    //method that all "children" of vehicle will inherit
    {
        cout << "The car has started" << endl;
    }

};

