#include <iostream>
using namespace std;

class father						//base class
	{
		private:
			int a=1;
		public:
			void func()
			{
				cout << a << endl;
			}
		protected:					//just like private but can be access by derived class
				int var;
	};
	
class son : public father			//derived class
	{
		private:
		public:
	};

//public inheritance	(most used):	public->public	protected->protected
//private inheritance	(default):		public+protected->private
//protected inheritance	:				public+protected->protected

int main() {
	
	son t;
	t.func();
	
	system("pause");
	return 0;
}