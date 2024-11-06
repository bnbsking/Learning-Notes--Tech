#include <iostream>
#include <stack>
using namespace std;

class bobo
	{
		private:
			int s=1;
		public:
			void print(stack <int> S) 				//print from top to bottom 
				{
					cout << s << ": ";		
					int a = S.size();
					for(int i=0 ; i<a ; i++)
						{
							cout << S.top() << " ";
    						S.pop();
    					}
    				cout << endl << endl;
					s++;
				}
	};

int main() {

	stack <int> S;
	bobo obj;
	
	for(int i=1;i<=5;i++) S.push(i);				obj.print(S);//1
	cout << "Empty: " << S.empty() << endl;		
	
	system("pause");
	return 0;
}
