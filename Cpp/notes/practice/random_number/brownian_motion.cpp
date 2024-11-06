#include<iostream>   
#include<math.h>  
#include<stdlib.h> 
#include<stdio.h>
#include<time.h>
#include<fstream>
using namespace std;  
int main(){    
                                                      
	srand((unsigned)time(NULL));
	ofstream file ;
	int k, i, j;
	cout << "Brownian motion for 10000 particles" << endl;
	cout << "Please enter the number of steps" << endl;
	cout << "100, 500 or 1000 ? ";
	cin  >> k;
	file.open("D:\Brown2_.txt");
	float A[10000], a=0, x=0;
	for(j=0;j<10000;j++)
		{for(i=0;i<k;i++)
			{a=rand()/32767.0-0.5;
		     if(a>0) x++; 
			 else    x--;}
		 A[j]=x;	  
		 file << A[j] << endl;
		 x=x*0;}
	    
	system("pause");
	return 0 ;} 