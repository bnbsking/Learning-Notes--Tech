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
			
			void insert_f(node* t)
				{
					t->next=head;
					head=t;
				}
			node* search(int x)
				{
					node* ptr = head;
					while(ptr!=0 && ptr->data!=x) ptr=ptr->next;
					return ptr;
				}
			node* delete_n(int x)
				{
					node* ptr = search(x);
					node* ptr2= head;
					if(ptr==ptr2)
						{
							head = ptr->next;
							return ptr;
						}
					else
						{
							while(ptr2->next!=ptr) ptr2=ptr2->next;
							ptr2->next=ptr->next;
							return ptr;					
						}
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
	
	linklist L;
	
	node *n1 = new node(5);
	node *n2 = new node(8);
	node *n3 = new node(12);
    
	
	L.insert_f(n1);
	L.insert_f(n2);
	L.insert_f(n3);
	L.delete_n(12);

	L.print();

	L.reverse();
	L.print();

	system("pause"); 
	return 0;
}