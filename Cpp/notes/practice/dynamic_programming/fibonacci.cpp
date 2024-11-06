#include<iostream>
using namespace std;
	
int main()
{
	int A[40];
	A[0]=0, A[1]=1;
	cout << A[0] << endl << A[1] << endl;
	for(int i=2;i<=40;i++)
		{
			A[i]=A[i-1]+A[i-2];
			cout << A[i] << endl;
		}
	return 0;
}