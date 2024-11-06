#include <iostream>
#include <time.h>
#include <chrono>
#include <random>
#include <fstream>
#include <cmath>
#include <iostream>
#include <math.h>

using namespace std;
int main (){
    
    //mx''=2ax-4bx^3+I(t)+Asin(wt), assume a=2, b=1 
        
    ofstream file;
    file.open("SR.txt");
    long long seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::normal_distribution<double> dis01(0.0, 1); // dis01(mean, standard deviation)
    std::mt19937 generator (seed);
      
	double m=1.0, I=1, A=0.01, w=1; //parameter
	double x=0, v=0, a=0, N=0, c=0;
	double t=0, D=0.01, z=0, S=0;
	float *P = new float[1000000], Q[10000], s1=0, s2=0, s3=0;
	int i=0, j=0, k=0, l=0, y=0;
	double temp;
		
	for(t=0;t<10000;t+=D)
		{
    	N=I*dis01(generator);	
		a=(4*x-4*pow(x,3)+A*sin(w*t)+N)/m;
		v=v+a*D;
		x=x+v*D;
		P[i]=x;
		i=i+1;
		}
		
	for(j=0;j<100000;j+=10)
		{
		for(k=0;k+j<1000000;k++)
			{
			s1=s1+(P[k]*P[k+j]);
			s2=s2+pow(P[k],2);
			}
		s3=s1/s2*1.0;
		Q[l]=s3;
	    file << s3 << endl;
		l=l+1;
		s1=0;
		s2=0;
		}
	
	file << "---" << endl << endl << endl;
	for(y=0;y<10000;y++)
		{
		for(z=0;z<100;z+=0.01)
			{
			S=S+Q[y]*cos(z);
			} 
		file << S << endl;
		S=0;
		}
	cout << "finish" << endl;	
			  
	return 0;}