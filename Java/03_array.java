public class MyClass {   
    public static void main(String args[]) {
        
        int A[] = {1,2,3,4,5};
        int[] B = {2,4,6,8,10}; 
        int[] C = new int [5];
        for(int j=0;j<5;j++)    System.out.println(A[j] + " " + B[j] + " " + C[j]);
        for(int j:B)    System.out.println(j);
        System.out.println("length of A is " + A.length + "\n");
        
        int[][] D = {{1,2,3},{4,5,6}};
        for(int j:D[0])    System.out.println(j);
        
    }
}
