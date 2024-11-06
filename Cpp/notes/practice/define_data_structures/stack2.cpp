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
			node* head;
			linklist()
				{
					head=0;
				}
			
			void push(node* t)
				{
					t->next=head;
					head=t;
				}
			void pop()
				{
					node* ptr = head -> next;
					delete head;
					head = ptr;
				}	
				
			void print()
				{
					node* ptr = head;
					int s = 0;
					while(ptr!=0)
						{
							cout << ptr->data << " ";
							ptr=ptr->next;
							s++;
						};
					cout << endl << "size: " << s << endl;
				}
			void reverse()
				{
					node* p = head;
					node* q = 0;
					while(p!=0)	
						{
							node *r=q;
							q=p;
							p=p->next;
							q->next=r;
						}
					head=q;
				}
	};


int main() {
	
	linklist S;
	
	node *n1 = new node(5);
	node *n2 = new node(8);
	node *n3 = new node(12);
    
	
	S.push(n1);
	S.push(n2);
	S.push(n3);
	S.pop();

	S.print();

	system("pause");
	return 0;
}