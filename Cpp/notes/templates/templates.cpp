
#include <iostream>
using namespace std;

template <class T>
T sum(T x,T y)
	{
		return x+y;
	}

template <class T, class U>
double smaller(T x,U y)
	{
		return(x<y?x:y);	//ternary operator. If x<y return x, else return y.
	}

template <class T, class U>
class bobo
	{
		private:
			T first;
			U second;
		public:
			bobo(T x, U y):first(x),second(y){};
			T bigger();
	};

template <class T, class U>		//repeat template 
T bobo<T,U>:: bigger()			//repeat type
	{
		return (first>second? first:second);
	}

int main() {
	
	int a=3, b=5;
	double c=0.2, d=0.8;
	
	cout << sum(a,b) << endl;
	cout << sum(c,d) << endl;
	//failed: cout << sum(a,c) << endl;
	cout << smaller(a,c) << endl;
	
	bobo <int,double> obj(123,132.5);
	cout << obj.bigger();
	
	system("pause");
	return 0;
}
