#include<iostream>  
#include<math.h>  
#include<stdlib.h> 
#include<stdio.h>
#include<time.h>
using namespace std;  
int main(){                                                          

srand((unsigned)time(NULL));                           //亂數函數:輸入rand()會有介於1~32767的整數 
float n, i=0, x=0, y=0, I=0, Prob;
cout << "Please enter the amount of random number : ";
cin  >> n;

while(i<=n){                                           //while迴圈, 條件式, 和for不同 次數由cin決定 變數可覆蓋 遞迴最後  
x=2*(double)rand()/32767-1;                            //把亂數轉為座標 
y=2*(double)rand()/32767-1;                            //定義亂數x,y 故意不打cout << x << endl << y <<endl;以免輸出過長  
if(pow(x,2)+pow(y,2)<=1)  I=I+1;                       //若x,y落在單位圓內 則I必須加一 I即落在圓內次數 
i++;}

Prob=(double)I/n;  
cout << endl;
cout << "number in circle = " << I      << endl;                                  
cout << "Probability = "      << Prob   << endl;       //機率=圓內次數/亂數總數
cout << "Area = "             << Prob*4 << endl;       //面積=機率*邊長為二的正方形面積  
cout << "error= "             << double(1-Prob*4/M_PI);//誤差=1-面積/實際面積 
 
system("pause");
return 0 ;} 