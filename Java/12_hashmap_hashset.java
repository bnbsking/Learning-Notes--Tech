import java.util.HashMap;
import java.util.HashSet;

public class MyClass {
    public static void main(String args[]) {
        
       HashMap<String,Integer> A = new HashMap<String,Integer>();
       
       A.put("Amy",154);
       A.put("Dave",42);
       A.put("Bobo",42);
       A.put("Rob",733);
       
       System.out.println(A.get("Amy"));
       System.out.println(A.get("Bobo"));
       System.out.println(A.get("Robs"));
       
       System.out.println(A.containsKey("Bobo"));
       System.out.println(A.containsValue("Bobo"));
        
       
       
       HashSet<String> B = new HashSet<String>();
       
       A.add("A");
       A.add("B");
       A.add("C");
       A.add("D");
       
       System.out.println(B);
       System.out.println(B.size());
        
    }
}
