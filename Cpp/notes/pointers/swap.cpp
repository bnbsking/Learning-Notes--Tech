#include <iostream>
using namespace std;

void SWAP(int& x, int& y) 	//call by reference 
	{
		int temp=x;
		x=y;
		y=temp;
	};
void SWAP2(int* x, int* y) 	//call by address/pointer
	{
		int temp=*x;
		*x=*y;
		*y=temp;
	}
void bobo()					//call by value
	{
		cout << "bobobobo" << endl;
	}

int main() {
	
	bobo();
	
	int a = 1, b=2;
	SWAP(a,b);
	cout << a << "   " << b << endl;
	
	int c=3, d=4;
	SWAP2(&c,&d);
	cout << c << "   " << d << endl;
	
	
	system("pause");
	return 0;
}