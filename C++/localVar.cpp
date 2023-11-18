#include<iostream>
using namespace std;


void StudentAge()   //local variable in c++ are defined within the block, method or constructor.
{                   // its scope is only active within that respected block itself.. outside that block that variable will be destroyed. 
  int age;          // here  age is a local variable
  
  cin >> age; 
  age = age + 5;
  cout << "Student age is:" << age << endl;
  
}
int main()
{
StudentAge();
return 0;
}
