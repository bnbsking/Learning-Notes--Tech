import java.io.File;
import java.util.Scanner;
import java.util.Formatter;


public class MyClass {
    public static void main(String args[]) {
            
        File f = new File ("C:\\Users\\Asus\\Desktop\\a.txt");
        if(f.exists())
            {
                System.out.println(f.getName());
            }
        else
            {
                System.out.println("Not exist");   
            }
        
        try
            {
                File x = new File ("C:\\Users\\Asus\\Desktop\\a.txt");  //Read
                Scanner sc = new Scanner(x);
            }
        catch(Exception e)
            {
                System.out.println("Not exist");
            }
        
        try
            {
                Formatter o = new Formatter ("C:\\Users\\Asus\\Desktop\\a.txt");  //Create & Write
                o.format("%s %s %s","1","John","Smith \r\n");
                o.format("%s %s %s","2","Lisa","Brown");
                o.close();
            }
        catch(Exception e)
            {
                System.out.println("Not exist");
            }
           
    }
}
