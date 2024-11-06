#include <iostream>
#include <queue>							//push: enqueue
											//pop: dequeue
using namespace std;

class bobo
	{
		private:
			int s=1;
		public:
			void print(queue <int> Q)		//print from front to rear 
				{
					cout << s << ": ";		
					int a = Q.size();
					for(int i=0 ; i<a ; i++)
						{
							cout << Q.front() << " ";
    						Q.pop();
    					}
    				cout << endl << endl;
					s++;
				}
	};

int main() {

	queue <int> Q;
	bobo obj;
	
	for(int i=1;i<=5;i++) Q.push(i);				obj.print(Q);//1
	cout << "Front: " << Q.front() << endl;		
	cout << "Rear: "  << Q.back()  << endl;
	cout << "Empty: " << Q.empty() << endl; 
	
	system("pause");
	return 0;
}
