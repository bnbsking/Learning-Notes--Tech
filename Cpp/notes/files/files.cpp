#include <iostream>
#include <fstream>		//file header 
using namespace std;

int main() {
	
	fstream obj;
	obj.open("bobofile.txt");
	obj << "AMAZING!!!!!" << endl;

	fstream obj2("bobofile2.txt");
	obj2.close();
	if (obj2.is_open())	obj2 << "WOW" << endl;
	else cout << "Something went wrong" << endl;

	fstream obj3("bobofile3.txt", ios::out);
	obj3 << "HI" << endl; 	
 	
	/*Open file in different mode
	ios::app	ios::ate	ios::binary		ios::in		ios::out	ios:trunc
 	*/
 	
	system("pause");
	return 0;
}