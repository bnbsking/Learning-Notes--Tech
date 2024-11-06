#include <iostream>
using namespace std;

int main() {
    
    int a = 10;
    int* ptr = &a;
    cout << "ptr=" << ptr << endl;
    cout << "*ptr=" << *ptr << endl;
    cout << "&ptr=" << &ptr << endl;
    cout << "&*ptr=" << &*ptr << endl;
    cout << "*&ptr=" << *&ptr << endl << endl; //*&有抵銷律
    // 可替換成 char bool int float double...
    
    int arr0[]={1,2,3}; //列舉法宣告靜態陣列
    int arr[3]={3,6}; //預約法宣告靜態陣列
    for(int i=0; i<5; i++)
        {cout << "arr[i]=" << arr[i] << " ";
         cout << "&arr[i]=" << &arr[i] << " " << endl;
        }
    cout << "arr=" << arr << endl;
    cout << "&arr=" << &arr << endl;
    cout << "*arr=" << *arr << endl;
    cout << "&*arr=" << &*arr << endl;
    cout << "*&arr=" << *&arr << endl; //*&有抵銷律
    int* ptr2 = arr; //不可用&arr
    cout << "ptr2=" << ptr2 << endl;
    cout << "*ptr2=" << *ptr2 << endl;
    cout << "&ptr2=" << &ptr2 << endl << endl;
    
    char c0[] = "apple";
    char c[5] = "appl"; //最多少1
    for(int i=0; i<5; i++)
        {cout << "c[i]=" << c[i] << " ";
         cout << "&c[i]=" << &c[i] << " " << endl;
        }
    cout << "c=" << c << endl;
    cout << "&c=" << &c << endl;
    cout << "*c=" << *c << endl;
    cout << "&*c=" << &*c << endl;
    cout << "*&c=" << *&c << endl; //*&有抵銷律
    char* ptr3 = c; //不可用&arr
    cout << "ptr3=" << ptr3 << endl;
    cout << "*ptr3=" << *ptr3 << endl;
    cout << "&ptr3=" << &ptr3 << endl << endl;
    
}
