#include <iostream>
using namespace std;

int bin(int n, int m)
	{
		if(n==m || m==0) return 1;
		else return bin(n-1,m)+bin(n-1,m-1);
	}

int main() {
	
	cout << bin(10,2);
	
	system("pause");
	return 0;
}