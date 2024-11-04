using System;
using System.Text;
using System.Net.Sockets;   //NetworkStream, TcpClient

namespace TestNetworkClient {
    class Program {                                 //宣告網路資料流變數
        NetworkStream myNetworkStream;              //宣告 Tcp 用戶端物件
        TcpClient myTcpClient;
        static void Main(string[] args) {
            Program myNetworkClient = new Program();        //Constructor
            Console.WriteLine("輸入連接機名稱 : ");
            string hostName = Console.ReadLine();            
            Console.WriteLine("輸入連接通訊埠 : ");
            int connectPort = int.Parse(Console.ReadLine());
            
            myNetworkClient.myTcpClient = new TcpClient();  //建立 TcpClient 物件
            try {   
                myNetworkClient.myTcpClient.Connect(hostName, connectPort); //測試連線至遠端主機
                Console.WriteLine("連線成功 !!\n");
            }
            catch {
                Console.WriteLine("主機 {0} 通訊埠 {1} 無法連接  !!", hostName, connectPort);
                return;
            }
            myNetworkClient.WriteData();
        }
        void WriteData() {
            int i=0;
            while(true){
            String strTest = String.Format("test string {0}", i);
            byte[] myBytes = Encoding.ASCII.GetBytes(strTest);  //encode string to byte
            myNetworkStream = myTcpClient.GetStream();          //建立網路資料流
            myNetworkStream.Write(myBytes, 0, myBytes.Length);  //寫入網路資料流
            System.Threading.Thread.Sleep(2000);
            i++;
            }
        }
    }
}
