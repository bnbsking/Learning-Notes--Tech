using System;               //Console.WriteLine
using System.Text;          //Encoding
using System.Net.Sockets;   //TcpListener, Socket(接收資料用)
using System.IO;            //File

namespace TestNetworkServer {
    class Program {
        static void Main(string[] args) {
            System.Net.IPAddress theIPAddress = System.Net.IPAddress.Parse("127.0.0.1");    //IP connection
            TcpListener myTcpListener = new TcpListener(theIPAddress, 36000);               //建立監聽物件 
            myTcpListener.Start();                                                          //啟動監聽
            Console.WriteLine("通訊埠 36000 等待用戶端連線...... !!");
            Socket mySocket = myTcpListener.AcceptSocket();                                 //建立socket

            do {    //不斷偵測client request
                try {
                    if(mySocket.Connected) Console.WriteLine("連線成功 !!");
                    while (mySocket.Connected) {
                        byte[] myBufferBytes = new byte[1000];
                        int dataLength = mySocket.Receive(myBufferBytes);
                            //將client資料取出(清空)socket，並將其命名為myBufferBytes
                            //(容量為1000byte, 長度為dataLength)
                        String data = Encoding.ASCII.GetString(myBufferBytes, 0, dataLength);   //接口/init/end
                        Console.WriteLine(data+"\n");
                        File.AppendAllText("data.txt", data+"\n");
                        System.Threading.Thread.Sleep(1000);
                    }
                }
                catch (Exception e) {
                    Console.WriteLine(e.Message + "something except");
                    mySocket.Close();
                    break;
                }
            } while (true);
        }//end main
    }//end class
}//end namespace
