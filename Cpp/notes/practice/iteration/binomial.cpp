#include <iostream>
using namespace std;

int fac(int x)
	{
		int s=1;
		for(int i=1;i<=x;i++)
			{
				s=s*i;	
			}
		return s;
	}

int bin(int n,int m)
	{
		return(fac(n)/(fac(m)*fac(n-m)));
	} 

int main() {
	
	cout << bin(10,2) << endl;
	
	system("pause");
	return 0;
}