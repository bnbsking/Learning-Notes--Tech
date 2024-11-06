#include <iostream>
using namespace std;

class Car{
    public:
        int wheel;
        int price;
        Car(int x, int y){
            wheel = x;
            price = y;
        }
};

class Bike{
    public:
        int wheel, price;
        Bike(int x, int y): wheel(x), price(y){
            cout << "wheel=" << wheel << endl;
        }
};

int main(){
    Car bus(8,100);
    bus.price = 200;
    cout << bus.wheel << " " << bus.price << endl;
    
    Car* taxi = new Car(4,25);
    taxi->price = 50;
    cout << taxi->wheel << " " << taxi->price << endl;

    Bike giant(2,1);
}
