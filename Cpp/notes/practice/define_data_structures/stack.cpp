
#include <iostream>
using namespace std;

class bobo										
	{
		private:								
			int top=0, cap=3;						//stack A[0~2], top is always empty
			int *A= new int ();
		public:
			bool is_full()
				{
					if (top==cap) return 1;
				}
			bool is_empty()
				{
					if (top==0) return 1;
				}
			void push(int x)
				{
					if(is_full()==0) A[top++]=x;	//A[top]=x, top=top+1
				}
			int pop()
				{
					if(is_empty()==0) return A[--top];
				}
			
			void print()
				{
					int s=0;
					for(int i=0;i<top;i++)
						{
							cout << A[i] << endl;
							s++;
						};
					cout << "size: " << s << endl;
					cout << "capacity: " << cap << endl;
				}
			void des() 					//only dynamic memory can be deleted 
				{
					delete A;
				}
	};

int main() {	
	bobo t;
	t.push(7);
	t.push(8);
	t.push(9);
	t.push(10);
	t.pop();
	t.push(11);
	t.print();
	
	t.des();
	system("pause");
	return 0;
}
