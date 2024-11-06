#include <iostream>
using namespace std;

int main() {
	
	int a=0, b=1, c, n=7;
	if(n==0) c=a;
	else if(n==1) c=b;
	else
		{
			for(int i=2;i<=n;i++)
				{
					c=a+b;
					a=b;
					b=c;
				}
		}
	
	cout<<c;
	
	system("pause");
	return 0;
}