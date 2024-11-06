#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> vec;
    for(int i=0; i<5; i++) vec.push_back(i*i);
    vec.pop_back();
    for(vector<int>::iterator it=vec.begin(); it!=vec.end(); it++) cout << *it << " ";

    return 0;
}
