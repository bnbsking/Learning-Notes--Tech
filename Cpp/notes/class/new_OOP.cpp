#include <iostream>
using namespace std;

class Animal{
    private:
        int price=5;
    public:
        int leg;
        char* name;
        Animal(int x, char* y):leg(x), name(y){
            cout << "leg=" << leg << endl;
            cout << "name=" << name << endl;
            cout << "price=" << price << endl;
        }
        void setPrice(int x){
            price = x;
        }
        void printPrice(){
            cout << price << endl;
        }
};

class Dog: public Animal{
    public:
        string species;
        Dog(int x, char* y, string z):Animal(x,y), species(z){
            cout << "HI\n";
            printPrice();
        }
};


int main()
{
    cout<<"Hello World";
    Animal obj(4,"abc");
    obj.setPrice(100);
    obj.printPrice();
    
    Dog obj2(4,"def","corgi");
    cout << obj2.name;
    
    
    return 0;
}
