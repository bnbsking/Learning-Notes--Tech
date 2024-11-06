#include<iostream>  
#include<math.h>
#define _USE_MATH_DEFINES
using namespace std;  
int main(){                                           //必備:標頭檔+名稱空間+主函數 

float fx(float x);                                    //定義函數 應變數fx 自變數x 
float n;
											                                
cout << "How many pieces of Riemann sum cut: ";
cin  >> n;                                                       
float h=2/n;                                          //將區間切成n等分後, 每分的寬度 
float i=0, sum=0;  
for(i=-1;i<=1;i+=h)                                   //for迴圈(起始值;執行條件;每次必須加多少) 
	{sum=sum+fx(i)*h;}                                //總計面積=小計面積+函數值*寬度 
cout << "Sum  area = " << sum    << endl;
cout << "Real area = " << M_PI/2 << endl; 
float c=1-sum/(M_PI/2);	
cout << "Error     = " << c << endl;   
    
system("pause");                                      //必備:停止 
return 0 ;} 

float fx(float x){                                    //定義函數 
return pow(1-pow(x,2),0.5);}