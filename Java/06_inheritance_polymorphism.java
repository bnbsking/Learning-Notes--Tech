class Animal {
    protected int leg;
    public void fun(String x)
        {
            System.out.println(x + " has " + leg + " legs.");
        }
    
    public void makesound()
        {
            System.out.println("Grr...");
        }
    
}

class Dog extends Animal {
    Dog()
        {
            leg = 4;
        }
}

class Cat1 extends Animal {
    public void makesound()
        {
            System.out.println("Meow1");
        }
}

class Cat2 extends Animal {
    public void makesound()
        {
            System.out.println("Meow2");
        }
} 

public class MyClass {
    public static void main(String args[]) {
        
        Dog d = new Dog();
        d.fun("dog");
        
        Animal a = new Cat1(); //polymorphism: 1 method with different implementation
        Animal b = new Cat2();
        a.makesound();
        b.makesound(); 

    }
}
