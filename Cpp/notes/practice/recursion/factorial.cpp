#include <iostream>
using namespace std;

int fac(int x)
	{
		if (x==0) return 1;
		else return x*fac(x-1);
	}

int main() {
	
	cout << fac(5);
	
	return 0;
}
