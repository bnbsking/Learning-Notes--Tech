#include <iostream>
#include <vector>	//no push_back nor pop_back
using namespace std;

class bobo
	{
		private:
			int s=1;
		public:
			void print(vector <int> V)
				{
					for(int k=0;k<V.size();k++) cout << V.at(k) << " ";	//V.at() access with check boundary 
					cout << endl;
				} 
			vector <int> :: iterator i;
			void print_i(vector <int> V)
				{
					for(i=V.begin();i!=V.end();i++) cout << *i << ' ';
					cout << endl;
				}
	};

int main() {

	vector <int> V;
	bobo obj;

	for(int k=1;k<=10;k++)	V.push_back(k);		obj.print(V);//1
	V.pop_back();								obj.print(V);//2						
	V.insert(V.begin()+2,5,99); 				obj.print(V);//3
	V.erase(V.begin()+10-1);					obj.print(V);//4
	
	cout << "First element: " << V.front() << " or " << *V.begin() << endl;
	cout << "Last element: " << V.back() << endl;
	cout << endl << "size: " << V.size() << endl;
	cout << "vector capacity: " << V.capacity() << endl;	//cap=2^floor(log n)
	cout << "empty: " << V.empty() << endl;					//1true 0false
	cout << "capacity: " << V.capacity() << endl;
	//V.clear();	 										//clear all
	
	system("pause");
	return 0;
}
