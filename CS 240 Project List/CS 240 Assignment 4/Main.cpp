//  Files in this program: Main.cpp, interview.asm 
//  Status: Finished.
//  References consulted: Seyfarth, Chapter 18
//
//Purpose
//  This program will demonstrate how to 
//  successfully take parameters into assembly,
// complete a branching interview process
// and return a answer depending upon the choices.
//This file
//  File name: Main.cpp
//  Language: C++
//  Max page width: 132 columns  [132 column width may not be strictly adhered to.]

//===== Begin code area ============================================================================================================

#include <stdio.h>
#include <stdint.h>    //Library not used
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

extern "C" double interview(char myname[], double z);
 

int main()
{

  double money = 0.0;
  char myname[50]; //sets an array of char that will hold the name
  std::cout << "Welcome to Software Analysis by Paramount Programmers, Inc." << std::endl;
  std::cout << "Please enter your first and last name and press enter: ";

cin.getline(myname, 50); //used getline because it saved the space in between first and last name


std::cout << "Thank you "<< myname << " Our records show that you applied for employment here with our agency a week ago.";
std::cout << std::endl;
std::cout << "Please enter your expected annual salary when employed at Paramount: ";
double income;

std::cin >> income; //income will hold value user posted.


std::cout << "Your interview with Ms Linder Fenster, Personnel Manager, will begin shortly." << std::endl;

money = interview(myname, income); //this runs the interview program taking two arguments, myname and income


if(money == 1000000.00) //if statement for chris sawyer
{

std::cout << "Hello Mr. Sawyer. I am the receptionist." << std::endl;
std::cout <<"This envelope has your job offer starting at 1 million annual. Please start any time you like." << std::endl;
std::cout << "In the mean time our CTO wishes to have dinner with you." << std::endl;
std::cout << "have a very nice evening Mr. Sawyer." << std::endl;
}
if(money == 88000.88) //if statement for cs major
{
 
  std::cout << "Hello " << myname << ". I am the receptionist." << std::endl;
   std::cout << std::fixed;
  std::cout << std::setprecision(2);
  std::cout << "This envelop contains your job offer with starting salary " << money << " anually. Please check back on" << std::endl << "Monday morning at 8 am." << std::endl;
  std::cout <<"Bye." << std::endl;


}
if(money == 1200.12) //if statement for social major
{
std::cout << "Hello " << myname << ". I am the receptionist." << std::endl;
std::cout << "We have an opening for you in the company cafeteria for " << money <<" anually." << std::endl;
std::cout <<"Take your time to let us know your decision." << std::endl << "Bye" << std::endl;


}
return 0;
}