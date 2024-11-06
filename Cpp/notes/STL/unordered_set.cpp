#include <iostream>
#include <unordered_set>
using namespace std; 
  
int main() 
{ 
    unordered_set<string> stringSet ; 

    stringSet.insert("code") ; 
    stringSet.insert("in") ; 
    stringSet.insert("c++") ; 
    stringSet.insert("is") ; 
    stringSet.insert("fast") ; 

    string key = "slow";
    if (stringSet.find(key) == stringSet.end()) cout << key << " not found" << endl << endl ; 
    else cout << "Found " << key << endl << endl ; 

    key = "c++";
    if (stringSet.find(key) == stringSet.end()) cout << key << " not found\n" ; 
    else cout << "Found " << key << endl ; 
  
    cout << "\nAll elements : "; 
    for (unordered_set<string>::iterator itr=stringSet.begin(); itr!=stringSet.end(); itr++) 
        cout << (*itr) << endl; 
}
