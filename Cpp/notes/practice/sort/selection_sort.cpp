#include <iostream>
#include <vector>
using namespace std;

class selection_sort{
	public:
		void print(vector <int> V)
			{
				for(int k=0;k<V.size();k++) cout << V.at(k) << " ";
				cout << endl << endl;
			}
		int f(vector <int> V, int s)	//find min index from s^th data to last data
			{
				int id = V.size()-1;
				for(int k=s;k<V.size();k++) if(V.at(k)<V.at(id)) id=k;
				return id;
			}
		void ss(vector <int> *V)
			{
				for(int k=0;k<(*V).size();k++)
					{
						int& x = (*V).at(k);
						int& y = (*V).at(f((*V),k));
						SWAP(&x,&y);
						print(*V);
					};
			}
		void SWAP(int* x, int* y)
			{
				int temp = *x;
				*x=*y;
				*y=temp;
			}
};

int main() {
	
	vector <int> V;
	selection_sort S;

	V.push_back(2);	
	V.push_back(7);
	V.push_back(6);
	V.push_back(4);
	V.push_back(1);
	V.push_back(8);
	V.push_back(9);
	V.push_back(3);
	V.push_back(5);

	S.print(V);
	S.ss(&V);

	system("pause");
	return 0;
}
