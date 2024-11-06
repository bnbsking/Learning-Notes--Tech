/*
Basic data types: int, long int, unsigned int; float, double; bool; char
    + conversion by (dtype)x or dtype(x)
    + float,bool,char can convert to int and vice versa
    + int<->float and any<->bool same as Python; int<->char by ascii, int+char=char

Advanced data types: string, vector (must include), auto
    + string
        + 3 initialization: string s="abc"; string s(3,'a); string s("haha")
        + stoi, stof <-> to_string 
        + string and bool cannot convert to each other
        + 1-length string to char: s[0]; char to 1-length string: string(""+c)
        + char* to str: string("abc")
        + 3 forward traversal, 2 backward traversal
        + concatenate, .substr, .find != string::pos, count, sort
    + vector
        + 3 initialization
        + 3 forward traversal, 2 backward traversal
        + push_back, pop_back, concatenate, slideing, find != V.size(), count, sort, min_element, max_element 

Built-in: int(sizeof(...))
*/
#include <iostream> // std::cout, std::cin // not everything can be printed
#include <typeinfo> // typeid(...).name() // i:int, d:double, c:char, etc. // string: NSt7...
#include <vector>
#include <algorithm> // count, reverse, sort, for_each, copy_if // for vector: find(in/not in), min_element, max_element
using namespace std;

void printV(vector<int>& V){
    for(int i=0;i<V.size();i++) cout << V[i] << ","; cout << endl;
}

int main(){
    // inline
    bool x = (4>2)? true : false; cout << x << endl;
    auto add1 = [](int x){return x+1;}; cout << add1(2) << endl; // auto not int

    // copy of basic type
    int a = 5;
    cout << &a << "|"; a=6; cout << &a << endl; // dynamic (address remains when reassign) // same as python
    // cout << &(a+1) << endl; error since not assigned // different from python
    int* ptr = &a; // pointer
    int b = a;     // deep copy
    int& c = a;    // shallow copy
    *ptr=6; cout << a << "|" << &a << endl;              // 6
    b=8;    cout << a << "|" << &a << "|" << &a << endl; // 6
    c=9;    cout << a << "|" << &a << "|" << &a << endl; // 9

    // string
    string s="abcdefb", t(3,'-'), u("haha");
    cout << s + 'x' + t + u << endl; // concatenate
        // forward
    for(int i=0;i<s.size();i++) cout << s[i]; cout << endl;
    for(auto& it:s) cout << it; cout << endl;
    for(string::iterator it=s.begin(); it!=s.end(); it++) cout << *it; cout << endl;
        // backward
    for(int i=s.size()-1;i>-1;i--) cout << s[i]; cout << endl;
    for(string::reverse_iterator it=s.rbegin(); it!=s.rend(); it++) cout << *it; cout << endl;
        // methods
    cout << s.substr(2,3) << endl; // s[2:2+3]
    cout << bool(s.find("bcd") != string::npos) << "|" << bool(s.find("bcx") != string::npos) << endl; // in -> 1; not in ->0
    cout << string("abcbe").find('b') << " | " << s.find("bcd") << "|" << s.find("xyz") << endl;       // .index // not found -> garbled
    cout << count(s.begin(), s.end(), 'b') << endl; // (algorithm) .count of char
    reverse(s.begin(), s.end()); cout << s << endl; // .reverse
    sort(s.begin(),s.end()); cout << s << endl;     // .sort
    sort(s.rbegin(),s.rend()); cout << s << endl;
        // copy
    cout << &s << "|"; s[0] = 'm'; cout << &s << "|" << s << endl; // string index can be reassigned // address remains
    string* ptr2 = &s; // pointer
    string v = s;      // deep copy
    string& w = s;     // shallow copy
    *ptr2 = "ppp"; cout << s << "|" << &s << endl;          // ppp
    v = "vvv"; cout << s << "|" << &v << "|" << &s << endl; // ppp
    w = "www"; cout << s << "|" << &w << "|" << &s << endl; // www

    // vector
    vector<int> V={1,2,3,8,0,8}, W(3,9), U{1,2,3,4,5}; // cannot print directly
        // forward
    for(int i=0;i<V.size();i++) cout << V[i]; cout << endl;
    for(auto& it:V) cout << it; cout << endl;
    for(vector<int>::iterator it=V.begin(); it!=V.end(); it++) cout << *it; cout << endl;
        // backward
    for(int i=V.size()-1;i>-1;i--) cout << V[i]; cout << endl;
    for(vector<int>::reverse_iterator it=V.rbegin(); it!=V.rend(); it++) cout << *it; cout << endl;
        // methods // push_back, pop_back same as python
    V.insert( V.begin()+2, 100 ); printV(V); // insert
    V.erase( V.begin()+2 ); printV(V);       // pop(idx)
    V.erase( find(V.begin(),V.end(),1) ); printV(V); // remove(x)
    V.insert( V.end(), W.begin(), W.end() ); printV(V); // concatenate
    vector<int> X(V.begin()+1, V.begin()+2); printV(X); // V[1:2]
    cout << bool(find( V.begin(), V.end(), 8)!=V.end()) << "|" << bool(find( V.begin(), V.end(), -1)!=V.end()) << endl; // in -> 1; not in ->0
    cout << find(V.begin(), V.end(), 8)-V.begin() << "|" << find(V.begin(), V.end(), -1)-V.begin() << endl; // .index // must -V.begin(), not found -> l+1
    cout << count(V.begin(), V.end(), 8) << endl; // .count
    reverse(V.begin(), V.end()); printV(V);       // .reverse
    sort(V.begin(), V.end()); printV(V);          // .sort
    sort(V.rbegin(), V.rend()); printV(V);
    sort(V.begin(), V.end(), [](int& x, int& y){return x%3>y%3;}); printV(V); // cmp sort
    cout << *min_element(V.begin(), V.end()) << "|" << *min_element(V.begin(), V.end(), [](int& x, int& y){return x%3>y%3;}) << endl; // min, cmp min
    cout << *max_element(V.begin(), V.end()) << "|" << *max_element(V.begin(), V.end(), [](int& x, int& y){return x%3>y%3;}) << endl; // max, cmp max
    for_each(V.begin(), V.end(), [](int& x){x++;}); printV( V ); // map self
    vector<int> Y;
    copy_if(V.begin(), V.end(), back_inserter(Y), [](int& x){return x>=5;}); printV(Y); // filter copied
        // copy
    vector<int> Z = V; // deep copy if V is 1-d vector
    Z[0] = 100; printV(V);

    return 0;
}
// unordered_map, map, multimap
// unordered_set, set, multiset
// new
// class, OOP, template
// file, exception
// include