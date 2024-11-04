class A{
    int a=0;
    void addone3()
        {
            a++;
        }
}


public class myClass{
    
    static void pint(int a)
        {
                System.out.println(a);
        }
        
    static void addone1(int a)
        {
            a++;    
        }
            
    static int addone2(int a)
        {
            return a+1;
        }
    
    public static void main(String[] args){
        
        int a=0;
        addone1(a); pint(a);
        
        a=0;
        addone2(a); pint(a); pint(addone2(a));
        
        A c = new A();
        c.addone3(); pint(c.a);
        
    } 
}
