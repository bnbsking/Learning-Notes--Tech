
#include <iostream>
using namespace std;

void swap(char &X, char &Y)
	{
		char temp=X;
		X=Y;
		Y=temp;
	}

void perm(char A[3], int i=1, int n=3)
	{
		if(i==n) for(int j=1;j<=n;j++) cout << A[j-1];
		else	{
					for(int j=i;j<=n;j++)
						{
							swap(A[i-1],A[j-1]);
							perm(A,i+1,n);
							cout << endl;
							swap(A[i-1],A[j-1]);
						}
				}
	}

int main() {
	
	char A[3]={'A','B','C'};
	perm(A);
		
	system("pause");
	return 0;
}
