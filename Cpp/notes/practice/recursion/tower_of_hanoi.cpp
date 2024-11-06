#include <iostream>
using namespace std;

void Hanoi(int n, char A, char B, char C)
	{
		if(n==1) cout << "move " << A << " to " << C << endl;
		else{
				Hanoi(n-1,A,C,B);
				Hanoi(1,A,B,C);
				Hanoi(n-1,B,A,C);	
			}		
	}

int main() {
	
	char A = 'A';
	char B = 'B';
	char C = 'C';
		
	Hanoi(4,A,B,C);
	
	system("pause");
	return 0;
}