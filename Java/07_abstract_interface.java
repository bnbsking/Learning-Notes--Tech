abstract class Animal {
    int legs = 0;
    abstract void makesound();
}

class Cat extends Animal{
    public void makesound()
        {
            System.out.println("Meow");
        }
}

interface Animal2 {  //abstract class within abstract method only. 
    public void eat();
    public void makesound();
}

class Dog implements Animal2 {   //the inteface can be multiple "implement", but the superclass can be "inheritance" only once. 
    public void makesound()
        {
            System.out.println("Woof");
        }
    public void eat()
        {
            System.out.println("omnomn");
        }
}


public class MyClass {
    public static void main(String args[]) {
        
        Cat c = new Cat();
        c.makesound();
        
        Dog d = new Dog();
        d.makesound(); 
        d.eat();
        
    }
}

