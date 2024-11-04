using System;
using NModbus;

namespace C_
{
    class Program
    {
        static int twice(int x){
            return 2*x;
        }
        static void passByReference(ref int r, out int o){
            r=10;
            o=20;
        }
        class Car{
            public int wheel, price; //must declare out instead of in constructor //default:static protected 
            public Car(int x, int y){
                wheel = x;
                price = y;
            }       //attribute/property needs to be specified grant
        }
        
        //?//ModbusSerialMaster CreateRtu( SerialPort serialPort);

        static void Main(string[] args)
        {
            Console.WriteLine("How old are you?");
            string age = Console.ReadLine();            //comment /*multiple comment*/
            int ageint = Convert.ToInt32(age);
            Console.WriteLine("Your twice age is {0}, {1} \n", age, twice(ageint));
            //var num; //error (must assign)
            //x+=5; x/2; x%2; x++; ++x; >,<=,==,!=; if else switch(mustbreak last)
            //while; do while; for(int i=0; i<5; i++); continue; break; &&; ||
            //msg = (age >= 18) ? "Welcome" : "Sorry"; function; overloading
            //function parameter order can shuffle f(y:1, x:1)

            int x=5, y;                        //ref must pre-defined, but out don't
            passByReference(ref x, out y);     //passByReference needs &r=&x
            Console.WriteLine("{0} {1}", x, y); //print one directly or string transform

            Car c = new Car(4,25);
            c.wheel = 6;
            Console.WriteLine("{0} {1}", c.wheel, c.price);

            //normal method must "static"
            //instance method must not "static" must "public"
            
            //memory
            //global: global var
            //stack: function, local var
            //heap: pointer, array, class
            int[] arr = new int[5]{1, 2, 5, 8, 9};  //default dynamic type[] size[]
            int[] arr2 = new int[3];                //must specify all or neither
            int[] arr3 = {1,2,3};                   //also be dynamic
            int[,] arr4 = new int[2,4];
            for(int i=0; i<arr.Length; i++) Console.Write(arr[i]+" "); Console.WriteLine();
            //?//Console.WriteLine("{0} {1} {2} {3}", arr.Rank, arr.Max(), arr.Min(), arr.Sum());
            foreach(int i in arr) Console.Write(i+" ");
        }
    }
}

/*
environment setting
install dotnet.sdk and setting its env variable
VScode:
    install C# extension
    select an empty folder
    new console
    dotnet run <file.cs>
    ctrl+shift+P: NuGet if outer package is needed
*/
