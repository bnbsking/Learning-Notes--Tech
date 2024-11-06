#include <iostream>
using namespace std;

class queue
	{
		private:
			int front=0, rear=0, cap=5;					//queue A[0~4]
														//effect data: front+1~rear
			int* A = new int();
		public:
			queue()										//initialize
				{
					for(int i=0;i<cap;i++)	A[i]=0;	
				}
			void enqueue(int x)
				{	
					rear=(rear+1)%cap;
					if(rear==front)
						{
							rear=(rear+cap-1)%cap;
							cout << "is_full" << endl;
						}
					else A[rear]=x;
				}
			int dequeue()
				{
					if(front==rear) cout << "is_empty" << endl;
					else
						{
							front=(front+1)%cap;
							int x = A[front];
							A[front]=0;
							return x;
						}
				}
			void print()
				{
					cout << "front: " << front << " rear: " << rear << endl;
					for(int i=0;i<cap;i++) cout << A[i] << " ";
					cout << endl << endl; 
			 	}
	};


int main() {
	
	queue obj;
	obj.print();
	
	for(int i=1;i<=5;i++)
		{
			obj.enqueue(i+10);
			obj.print();
		}
	for(int i=1;i<=5;i++)
		{
			obj.dequeue();
			obj.print();
		}
	
	system("pause");
	return 0;
}