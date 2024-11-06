#include <iostream>
using namespace std;

class bobo										//identity
	{
		private:
			int f=0;							//attribute, shared varible, cannot call by main	
		public:									//attribute
			bobo(int a)							//constructor
				{
					cout << "object create sucessful" <<endl;
				};			
			void func1()						//method
				{
					cout << "sucess 1" << endl;
				}
			void func2();
			void add()
				{
					f=f+1;
					cout << f << endl;
				}
	};
void bobo::func2()								//selection operator
	{								
		cout << "sucess 2" << endl; 
	}

int main() {	

	bobo t(1);										//t is object
	
	cout << "There are 3 methods to call function in class" << endl;
	
	cout << endl << "1st: dot operator" << endl;
		t.func1();
		t.func2();
	
	cout << endl << "2nd: arrow selection operator" << endl;
		bobo* p=&t;
		p->func1();
		p->func2();
	
	cout << endl << "3rd: pointer dereference" << endl;
		bobo* q=&t;
		(*q).func1();
		(*q).func2();
	
	cout << endl << "Share memory" << endl;
		t.add();
		t.add();
	
	cout << endl << "constant object" << endl;
		const bobo s(1);
		//failure: s.func1();
	
	system("pause");
	return 0;
}