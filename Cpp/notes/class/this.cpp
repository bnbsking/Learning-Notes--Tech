#include <iostream>
using namespace std;

class bobo
	{
		private:
			int var;
		public:
			bobo(int a):var(a){};
			void print()
				{
					cout << var			<< endl;
					cout << this->var	<< endl;
					cout << (*this).var << endl;
				}
	};

int main() {
	
	bobo t(1);
	t.print();
	
	system("pause");
	return 0;
}