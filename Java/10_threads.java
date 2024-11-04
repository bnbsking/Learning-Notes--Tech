class Loader extends Thread {
    public void run ()
        {
            System.out.println("Hello1");
        }
}

class Loader2 implements Runnable{
    public void run()
        {
            System.out.println("Hello2");
        }
}

public class MyClass {
    public static void main(String args[]) {
        
        Loader obj = new Loader();
        obj.start();
        
        Thread t = new Thread(new Loader2());
        t.start(); 
        
    }
}
