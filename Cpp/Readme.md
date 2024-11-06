# Introduction

This is the quick review of c++.

1.	symbols
    + `::`: namespace, classFurtherDefine
    + `.`: object
    + `->`: pointerToObject
    + `:`: constructor, after public or private, inheritance
    + `;`:
        + class and commands must include it
        + for, while, and function are optional

2.	`use namespace std`: make `cout` and `cin` more concise.

3.	`for(......;i++)` same as `for(......;++i)`

4.	array:
    + `int A[2][3] = {{1,2,3},{4,5,6}};`
    + `char C[5] = {'a','b','c','d','e'};`
    + but `char C[5]="abcde"` is **NOT** available

5.	get space in byte unit:
    + sizeof:
        + 1: char
        + 4: int, NULL
        + N: length N char array
        + N+1: length N string
        + N\*4: length N int array
    + string_variable.size()
        + N

6.	pointers
    + int* pointer; *a value; int& alias; &a address
    ```cpp
    int* ptr = &a;
    int* ptr = new int; int* ptr = new int(5); delete ptr
    int* ptr = new int[5]; delete [] ptr;
    int A[3]={1,2,3}; int* ptr = A
    ```
    + but `int* ptr = {1,2,3}` is **NOT** available

7.	int argument in function:
    + CBV: `f(int x)` or `f(x)` 
    + CBA: `f(int* x)` or `f(&x)`
    + CBR: `f(int& x)` or `f(x)`

8.	array argument in function:
    + `f(A)`
        + where `A` is `&A` is `&A[0]`
        + Therefore, must input address and size
    + CBA, `f(int* A)` or `f(int A[])`
        + then call function by `f(A)`

9.	struct, struct-constructor:
    + definition:
        ```cpp
        typedef struct{
            int leg;
            int eye;
        }Animal;
        ``` 
    + instantiation object:
        ```cpp
        Animal obj = {4,2}
        Animal obj = {.leg=4, .eye=2}.
        ```
    + instantiation pointer: `Animal* ptr = malloc(1*sizeof(Animal))`;

10.	(C++)
    + function overloading: same different input types can be defined and used simultaneously
    + function overriding: overwrite parent class method

11.	constructor vs destructor:
    + definition:
        + constructor: Predefine class attributes that different from the input, then assign the values. e.g. ```int x, y; ListNode(int cx, int cy):x(cx),y(cy){}```
        + destructor: `~ListNode(){}`
    + instantiation object:
        ```cpp
        ListNode obj1 = {1,2};
        ListNode obj2 = {.x=1, .y=2};
        ListNode obj3 = ListNode(1,2);
        ListNode obj4(1,2);
        ```
    + instantiation pointer: `ListNode* ptr = new ListNode(1,2);`
    + constructor have parameters but destructor havn't
    + constructor can be overloaded but destructor can't
    + both of them cannot return
    + If no constructor, instantiation needs () as well. i.e. `Animal obj = Animal();`

12.	Operator overloading:
    + `myClass operator + (myClass& obj){return ...}`

13.	Encapsulation | access specifier:
    + public: everyone
    + private:
        + class itself
        + friend function. i.e. `friend void f(myClass& obj)`
    + protected: similar to private but allow child and friend class's child to access

14.	Inheritance: based class - Animal | derived class - Dog
    + public inheritance: `class Dog: public Animal`
        + public-public
        + protected-protected
    + protected inheritance: `class Dog: protected Animal`
        + public-protected
        + protected-protected
    + (default) private inheritance: `class Dog: private Animal`
        + public-private
        + protected-private
    + constructor and destructor are not inherited. However, they will be called<br>
    i.e AnimalConstruct->DogConstruct->DogDeconstruct->AnimalDeconstruct <br>
    `Dog(int y) : Animal (y) {cout<<"Dog"<<endl;}`

15.	Polymorphism:
    + Dog, Cat inherit from Animal but override a method in different ways
    + Virtual function (for optional overridden) in Animal: `virtual void f(){};`. It can also be implemented. Hence it is just reminder;
    + Pure virtual function (for mandatory overridden) in Animal: `virtual void f()=0;`<br>
    Must be implemented in Dog and Animal cannot be instantiated. i.e. Virtual class

16.	Template:
    + function: `template<class T,class U> T sum(T a, T b){return a+b;}` 
    + class: `template<class T> class myClass{}; myClass<T> obj = myClass<T>();`
    + template overloading: `template<> class myClass<char>{};`

17.	Exception:
    + `try{ throw 99; } catch(int ball){}`
    + `catch(...)`: catch all types of error

18.	File:
    + `#include <fstream>`

19.	Include and file extension:
    + header (.h): interface. guardInclude and namespace-class-attrMethod only
    + source (.cpp): program without main. include �xxx.h� and implement. e.g. `void myClass::f(){}`
    + main (.cpp):
        + `include "xxx.h"`
        + Compile command `g++ source.cpp main.app`
        + `out.exe`

20.	pointer vs iterator:
    + usages are almost the same. But pointer is for array, iterator is for STL.
    + For ordered data: both `*(ptr+i)` and `*(it+i)` are i^th element
    + iterator begins from 0th element and ends at last+1 element

21.	string:
    + `string s = "apple"; s.substr(1,2); string s(5,'0')`
    + `for(auto ele: container){}`
    + `s.find()`
    + `s.push_back('a')`
    + `s.size()`
    + `stoi()`, `stol`, `stoll()`, `to_string()`

22.	unordered_map (hashtable) vs map (hashtable+BST) vs multimap (BST)
    ```cpp
    unordered_map<int,int> H = {{"apple",20},{"banana",10}};
    for(auto it=H.begin();it!=H.end();++it) cout << it->first << " " << it->second;
    ```
    + auto is the abbreviation of `unordered_map<int,int>::iterator`
    + `H.find("apple")==H.end()` same as `not in`
    + erase can input an element of iterator
        ```cpp
        H["apple"]=30
        H.erase("apple")
        ```
        + if erase something in multimap, all will be deleted.
        + if want to erase just one: `auto it=H.find(); H.erase(it)`
    + `H.size()`

23.	unordered_set (hashtable) vs set (hashtable+BST) vs multiset (BST)
    ```cpp
    unordered_set<int> S = {1,2,3,4,5};
    for(auto it=S.begin();it!=S.end();++it) cout << *it;
    S.find(1)==S.end() // same as not in
    S.insert(6)
    S.erase(5)
    S.size()
    ```
    + for ordered set: `min=*S.begin(), max=*S.rbegin()`

24.	vector
    ```cpp
    vector<int> V = {1,2,3}; vector<int> V(100,0);
    for(int i=0;i<V.size();i++) cout << V[i];
    for(auto it=V.begin();it!=V.end();++it) cout << *it;
    
    V.push_back(100) // O(1)
    V.insert(V.begin()+i,100) // O(N), become i-th element after insertion
    V.pop_back() // O(1)
    V.erase(V.begin()+4) // O(N), delete i-th element. erase is for iterator only.
    V.size()`: O(1) 
    ```

25.	algorithm in vector
    ```cpp
    find(V.begin(), V.end(), item) != vec.end()
    auto it = find(V.begin(), V.end(), item);
    int index = (it==V.end())? -1 : it-V.begin();
    count(V.begin(), V.end(), item)
    *min_element(V.begin(), V.end())
    *max_element(V.begin(), V.end())
    sort(V.begin(), V.end(), [](int a, int b){return abs(a)<abs(b)});
    ```
    + Heap
        ```cpp
        H = make_heap(V.begin(), V.end());
        pop_heap(V.begin(),V.end()); V.pop_back();
        H.push_back(9); push_heap(V.begin(),V.end());
        ```

26. Basic of class
```cpp
class C{
    public:
        int x, y;
        C(int ix, int iy):x(ix),y(iy){}
};

int main(){
    C obj = C(3,5);
    cout << obj.x << obj.y << endl;
    C* ptr = new C(3,5);
    cout << ptr->x << ptr->y << endl;
}
```

# VSCode Environment setting
+ install vscode
+ create folder
+ open folder by vscode and edit code
+ install "C/C++ Extension Pack" via VsCode ( at /usr/bin/g++ )
+ click icon and select "C/C++:g++ build and debug active file"