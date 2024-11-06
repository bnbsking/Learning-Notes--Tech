#include <iostream>
using namespace std;

class bobo
	{	
		private:
			int x=3;
			const int y=4;
		public:
			bobo(int a, int b):x(a),y(b)	//colon op. 1.must be constructor 2.means x=a y=b
				{
				};
			void print()
				{
					cout << x << " " << y << endl;
				}		
	};

int main() {
	
	bobo t(1,2);
	t.print();
	
	system("pause");
	return 0;
}