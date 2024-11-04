import java.util.ArrayList; //dynamic array
import java.util.LinkedList;
import java.util.Collections;
import java.lang.Math;
import java.util.Iterator;

public class MyClass {
    public static void main(String args[]) {
        
        ArrayList<Double> A = new ArrayList<Double>();
        
        for(int j=1;j<=10;j++) A.add(Math.pow(-1,j)*j*2);
        A.remove(4);
        
        System.out.println("ArrayList: " + A);
        System.out.println("Size = " + A.size() );
        System.out.println("Is there 8 in ArrayList? " + A.contains(8));
        System.out.println("A[3]: " + A.get(3));
        Collections.sort(A);
        System.out.println("Sorted ArrayList: " + A);
        System.out.println("Max:" + Collections.max(A));
        System.out.println("Min:" + Collections.min(A));
        Collections.reverse(A);
        System.out.println("Reverse ArrayList: " + A);
        Collections.shuffle(A);
        System.out.println("Shuffle ArrayList: " + A);
        
        //
        System.out.println();
        LinkedList<Double> B = new LinkedList<Double>();
        
        for(int j=1;j<=10;j++) B.add(Math.pow(-1,j)*j*2);
        B.remove(4);
        
        System.out.println("LinkedList: " + B);
        System.out.println("Size = " + B.size() );
        System.out.println("Is there 8 in ArrayList? " + B.contains(8));
        System.out.println("B[3]: " + B.get(3));
        Collections.sort(B);
        System.out.println("Sorted LinkedList: " + B);
        System.out.println("Max:" + Collections.max(B));
        System.out.println("Min:" + Collections.min(B));
        Collections.reverse(B);
        System.out.println("Reverse ArrayList: " + B);
        Collections.shuffle(B);
        System.out.println("Shuffle ArrayList: " + B);
        
        Iterator<Double> it = B.iterator();
        it.next();
        System.out.println(it.next() + " " + it.hasNext());
        System.out.println(B);
        it.remove();
        System.out.println(B);
        
        System.out.println();
        Iterator<Double> it2 = B.iterator();
        while(it2.hasNext())
            {
                System.out.println(it2.next());
            }
    }
}
