#include <iostream>
using namespace std;

//polymorphism: 1 function with multiple implements 
//A class is called polymorphic if it has a virtual function 
//A class is called abatract    if it has a pure virtual function

class Enemy
	{
		protected:
			int attactpower;
		public:
			void setap(int a)
				{
					attactpower=a;
				}
			virtual void attack()=0; //pure virtual function
			virtual void func(){};   //virtual function
	};
	
class Ninja: public Enemy
	{
		public:
			void attack()
				{
					cout << "Ninja -" << attactpower << endl;
				}
	};
	
class Monster: public Enemy
	{
		public:
			void attack()
				{
					cout << "Monster -" << attactpower << endl;
				}
	};

int main() {
	
	Ninja n;
	Monster m;
	Enemy* e1=&n;
	Enemy* e2=&m;
	
	e1->setap(20);
	e2->setap(80);
	
	e1->attack();
	e2->attack();
	  
	
	system("pause");
	return 0;
}