#include <iostream>
using namespace std;

class bobo
	{
		private:
			int x=1; 
		public:
			void print()
				{
					cout << x << endl;
				}
		friend func();
	};

void func(bobo& obj)	{
							obj.print();
						};


int main() {
	
	bobo t;
	func(t);
	
	system("pause");
	return 0;
}