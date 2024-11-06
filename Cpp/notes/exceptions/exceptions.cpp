#include <iostream>
using namespace std;


int main() {
	
	try
		{
			int a=10, b=0;
			if(b==0) throw 0;
			if(b==0) throw 0;
			cout << "Result: " << a/b << endl;		
		}
	
	catch(int x)
		{
			cout << x << endl;
		}
	catch(...)
		{
			cout << "Zero divisor!" << endl;
		}
	
	system("pause");
	return 0;
}