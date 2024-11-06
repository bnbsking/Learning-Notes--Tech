#include <iostream>
using namespace std;

int bobo(int x)
	{
		return x*x;
	} 

int bobo2(int x=1, int y=2)
	{
		return x+y;
	}

int main() {
	
	cout << bobo(1)+bobo(2) << endl;
	
	cout << bobo2(10) << endl;
		
	system("pause");
	return 0;
} 