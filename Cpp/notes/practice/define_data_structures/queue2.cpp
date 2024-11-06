#include <iostream>
using namespace std;

class node
	{
		public:
			int data;
			node* next;
			node(int x):data(x),next(0){};
	};
	
class linklist
	{
		public:
			node* front;
			node* rear;
			linklist()							//front(dequeue) 1st data
												//rear(enqueue) last data			
				{
					front=0;
					rear=0;
				}
			void enqueue(node* t)
				{
					if(front==0) front=t;
					else rear -> next = t;
					rear = t;
				}
			int dequeue()
				{
					if(front==0) cout << "is_empty" << endl;
					else
						{
							node* t = front;
							front = front -> next;
							int x = t -> data;
							delete t;
							return x; 
						}
				}
			void print()
				{
					node* ptr = front;
					int s = 0;
					while(ptr!=0)
						{
							cout << ptr->data << " ";
							ptr=ptr->next;
							s++;
						};
					cout << endl << "size: " << s << endl;
				}
	};


int main() {
	
	linklist Q;
	
	node *n1 = new node(5);
	node *n2 = new node(8);
	node *n3 = new node(12);
    
	
	Q.enqueue(n1);
	Q.enqueue(n2);
	Q.enqueue(n3);
	Q.print();
	
	Q.dequeue();
	Q.print();

	system("pause");
	return 0;
}