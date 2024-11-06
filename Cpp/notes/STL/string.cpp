#include <iostream>
#include <string>
using namespace std;

int main() {
	
	string A = "Hello world";
	for(int i=A.size()-1;i>=0;i--)	cout << A[i];    //reverse string 
	
	cout << endl << A[11] << endl;
	if(A[11]==0) cout << "Exceed size" << endl;     //Exceed size
	
	cout << sizeof(A) << endl;                      //byte size
	cout << A.empty() << endl;
	cout << A.find("llo") << endl;
	
	string B;
	B.assign(A,0,5);
	cout << B << endl;
	B.append(A,0,5);
	cout << B << endl;
	B.insert(5,"SSS");
	cout << B << endl;	
	cout << B.size() << " " << B.length();
	
	return 0;
}
