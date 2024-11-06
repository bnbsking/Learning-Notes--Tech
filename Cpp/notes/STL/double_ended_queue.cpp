#include <iostream>
#include <deque>							//double ended queue
using namespace std;

class bobo
	{
		private:
			int s=1;
		public:
			deque <int> :: iterator i;
			void print(deque <int> D)		//print from front to rear 
				{
					cout << s << ": ";		
					for(i=D.begin();i!=D.end();i++)	cout << *i << " ";
					cout << endl << endl;
					s++;
				}
	};

int main() {

	deque <int> Q;
	bobo obj;
	
	for(int i=1;i<=5;i++) Q.push_back(i);			obj.print(Q);//1
	Q.push_front(10);								obj.print(Q);//2
	Q.pop_back();									obj.print(Q);//3
	Q.pop_front();									obj.print(Q);//4
	
	cout << "Front: " << Q.front() << endl;		
	cout << "Rear: "  << Q.back()  << endl;
	cout << "Empty: " << Q.empty() << endl; 
	
	system("pause");
	return 0;
}
