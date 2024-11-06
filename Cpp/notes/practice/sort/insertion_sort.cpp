#include <iostream>
#include <vector>
using namespace std;

class insertion_sort
	{
		private:
		public:
			void print (vector <int> V)
				{
					for(int j=0;j<V.size();j++) cout << V.at(j) << " ";
					cout << endl;
				}
			void ins(vector <int>* V, int x)
				{	
					int k=0;
					if((*V).size()!=0)
						{
							while((*V).at(k)<x)
							{
								k=k+1;
								if (k==(*V).size())	break;
							}
						}
					(*V).insert((*V).begin()+k,1,x);
				}
	};

int main() {
	
	vector <int> V;
	insertion_sort obj;
	
	obj.ins(&V,2);
	obj.ins(&V,3);
	obj.ins(&V,1);
	obj.ins(&V,7);
	obj.ins(&V,4);
	obj.ins(&V,5);
	obj.ins(&V,6);
	
	obj.print(V);
	
	system("pause");
	return 0;
}
