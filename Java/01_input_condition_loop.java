import java.util.Scanner;

public class MyClass {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);
        int x1, x2, x3;
        System.out.println("Enter two numbers:");
        x1 = sc.nextInt();
        x2 = sc.nextInt();
        x3 = sc.nextInt();
        
        if(x1>x2) System.out.println("x1 is bigger");
        else if(x1==x2) System.out.println("same");
        else System.out.println("x2 is bigger");

        if(2>1 && 2>0 || 2==1) System.out.println("OK");
        
        switch(x3)
            {
                case 0:
                    System.out.println("The number is 0");
                    break;
                case 1:
                    System.out.println("The number is 1");
                    break;
                default:
                    System.out.println("Neither 0 or 1");
            }
        
        int x=5;
        while(x>0)
            {
                System.out.println(--x);
            }
        
        for(int j=1;j<=5;j++)
            {
                System.out.println("Bobo upgrade X " + j);
            }
        
        int y=0;  
        do
            {
                y++;
                if(y==3) continue;
                if(y==16) break;
                System.out.println(y++);
            }while(y<20);
    }
}
