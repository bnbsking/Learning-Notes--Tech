#include <iostream> 
using namespace std; 

int main() {
    
    int x=1;
    cout << "--Address--" << endl; 
	cout << x  << endl; //content of x
    cout << &x << endl; //address of x
    
    cout << endl << "--Reference--" << endl; 
	int& k=x;			//not address but reference. Let k and x be equivalent
	cout << k << endl;
	cout << &k << endl; 
    
    cout << endl << "--Pointer--" << endl;
    int* p=&x;			//declare a pointer at once
    cout << p  << endl; //content of p = address of x 
    cout << *p << endl; //content of x
	*p=20;				
	cout << x  << endl;
	cout << &x << endl; 
    cout << p  << endl;
    cout << *p << endl;
		//error p=20 
    
    cout << endl << "--Constant--" << endl;
    const int y=1;
		//error y=20 
    cout << y << endl;
	const int* q=&y;
		//error int *q=&y 
	cout << q  << endl;			
    cout << *q << endl;
    	//error *q=20 
    
    cout << endl << "--void type pointer--" << endl; //store address only
    int z=5;
	void* r=&z;
	cout << r  << endl;
		//error cout << r* << endl; 

	system("pause");
	return 0;
}