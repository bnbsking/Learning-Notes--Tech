#include <iostream>
using namespace std;

class bobo
	{
		public:
			int var;
			bobo(){}
			bobo(int a):var(a){}
			bobo operator+(bobo& obj)
				{
					bobo t;
					t.var=this->var+obj.var;
					return t;
				}
	};

int main() {
	
	bobo obj1(12), obj2(55);
	bobo t = obj1+obj2;
	cout << t.var;
	
	system("pause");
	return 0;
}