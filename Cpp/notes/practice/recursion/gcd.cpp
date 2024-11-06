#include <iostream>
using namespace std;

int GCD(int n,int m)
	{
		if(n>m)
			{
				if(n%m==0) return m;
				else return GCD(m,n%m);
			}
		else if(n==m) return n;
		else return GCD(m,n);
	}

int main() {

	cout << GCD(36,24) << endl;
	cout << GCD(24,24) << endl;
	cout << GCD(24,36) << endl;

	system("pause");
	return 0;
}