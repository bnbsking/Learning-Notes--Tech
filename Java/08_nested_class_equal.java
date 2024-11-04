class Robot{
    int id;
    Robot(int i)
        {
            Brain b = new Brain();
            b.think();
        }
    
    private class Brain{
        public void think(){
            System.out.println(id + " is thinking!");
        }
    }
}

public class MyClass{
    public static void main(String[] args){
        
        Robot r = new Robot(1);
        Robot r2= new Robot(1);
        
        System.out.println(r==r2);
        
    }
}
