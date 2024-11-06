#include <iostream>
using namespace std;

void swap_ref(int& x, int& y){
    int temp = x;
    x = y;
    y = temp;
}

void swap_ptr(int* x, int* y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main() {
    int a=1;
    int* ptr=&a;
    int& alias=a; 
    *ptr = 2;
    cout << a << endl;
    alias = 3;
    cout << a << endl;
    
    int b=1; int c=2;
    swap_ref(b,c);
    cout << "b=" << b << " c=" << c << endl;
    
    int d=1; int e=2;
    swap_ptr(&d,&e);
    cout << "d=" << d << " e=" << e << endl;

}
