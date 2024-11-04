public class MyClass {
    
    static void pstring(String x)
        {   
            System.out.println(x);
        }
        
    static void pint(int x)
        {
            System.out.println(x);
        }
    
    static int sum(int x, int y)
        {
            return x+y;
        }
    
    static int addone(int x)
        {
            return x+1;
        }
    
    public static void main(String args[]) {
        
        pstring("Hello");
        pint(sum(3,5));
        
        int a=3;
        pint(addone(a));
    }
}
