#include <iostream>
using namespace std;

class bobo										
	{
		private:
			int f=0;							
			int *A= new int ();					//dynamic memory	
		public:	
			void push(int item)
				{
					A[f++]=item;
				}
			void view()
				{
					for(int i=0;i<f;i++) cout << A[i] << endl;
				}
			void des()
				{
					delete A;					//only dynamic memory can be delete
				}	
	};
	


int main() {	
	bobo t;										
	t.push(7);									
	t.push(8);
	t.push(9);
	t.view();
	
	t.des();
	
	system("pause");
	return 0;
}