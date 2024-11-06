#include <iostream>
#include <list> 				//double linked list
using namespace std;

class bobo
	{
		private:
			int s=1;
		public:
			list <int> :: iterator i;
			void print(list <int> L)		//print from front(leftist) to back(right) 
				{
					cout << s << ": ";		
					for(i=L.begin();i!=L.end();i++)	cout << *i << " ";
					cout << endl << endl;
					s++;
				}
			void mid_ins(list <int> *L, int k, int m, int x)//insert x after k^th data with multiplicity m
				{
					i=(*L).begin();
					advance(i,k);
					(*L).insert(i,m,x);
				}
			void mid_era(list <int> *L, int k)
				{
					i=(*L).begin();
					advance(i,k-1);
					(*L).erase(i);
				}
			void front_splice(list <int> *L, list <int> *M)
				{
					i=(*L).begin();
					(*L).splice(i,*M);
				}
	};

int main() {

	cout << "FILO data structure" << endl;
	list <int> L;
	bobo obj;
	
	//L.clear();//remove all
	for(int i=1;i<=5;i++) L.push_front(i);			obj.print(L);//1
	L.pop_front();									obj.print(L);//2
	L.push_back(8);									obj.print(L);//3
	L.pop_back();									obj.print(L);//4
	L.remove(1);									obj.print(L);//5
	obj.mid_ins(&L,2,5,99);							obj.print(L);//6
	obj.mid_era(&L,4);								obj.print(L);//7
	L.unique();										obj.print(L);//8
	L.reverse();									obj.print(L);//9
	L.sort();										obj.print(L);//10

	list <int> M;
	for(int i=1;i<=5;i++) M.push_front(i);
	//M.sort();
	cout << "List M "; 	obj.print(M);//11 
	cout << "Merge ";	L.merge(M);	obj.print(L);//12	//insert M into L at first accurate place O(n)
														//merge is suit for sorted data
	
	for(int i=1;i<=5;i++) M.push_front(i*10);
	cout << "List M "; 	obj.print(M);//13
	cout << "Splice ";   obj.front_splice(&L,&M);	obj.print(L);//14
	
	cout << "Front: " << L.front() << " or " << *L.begin() << endl;
	cout << "Back: " << L.back() << endl;
	cout << "Empty: " << L.empty() << endl;
	cout << "Size: " << L.size() << endl;
	
	system("pause");
	return 0;
}
