class Animal{
    void bark(){
        System.out.println("Woof");
    }
}

class Vehicle{
    private String color;
    
    Vehicle()               //constructor with defaulf color set
        {
            this.color = "Red";
        }
    
    Vehicle(String c)       //constructor with particular color
        {
            color = c;
        }
    
    public String getColor()
        {
            return color;
        }
    public void resetColor(String c)
        {
            this.color = c;
        }
}

public class MyClass {
    public static void main(String args[]) {
        
        Animal dog = new Animal();
        dog.bark();
        
        Vehicle v = new Vehicle();
        System.out.println(v.getColor());
        v.resetColor("Blue");
        System.out.println(v.getColor());
        
        Vehicle v2 = new Vehicle("Green");
        System.out.println(v2.getColor());
        
    }
}
