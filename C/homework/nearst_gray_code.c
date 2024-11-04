#include <stdio.h>
#include <stdlib.h>
#include <math.h> //floor ceil pow sqrt

int i=0, j=0;

char** gray(int n){
    if(n==1){
        char** arr = malloc(2*sizeof(char*));
        arr[0] = malloc(1*sizeof(char));
        arr[1] = malloc(1*sizeof(char));
        arr[0][0] = '0';
        arr[1][0] = '1';
        return arr;
    }
    else{
        char** prev = gray(n-1);
        char** all = malloc(pow(2,n)*sizeof(char*));
        for(i=0; i<pow(2,n); i++) all[i] = malloc(n*sizeof(char));
        
        for(i=0; i<pow(2,n); i++){
            for(j=0; j<n; j++){
                if(j==0){
                    if(i<pow(2,n-1)) all[i][0] = '0';
                    else all[i][0] = '1';
                }
                else{
                    if(i<pow(2,n-1)) all[i][j] = prev[i][j-1];
                    else all[i][j] = prev[ (int)pow(2,n)-1-i ][j-1];                    
                }
            }
        }
        return all;
    }
}

/*
n: n bit gray code. 2^n可能 
m= sqrt(2^n) = 2^(n/2)
%: modular (mod) 取餘數
floor:無條件捨去 floor(3.4)=3 floor(-3.4)=-4 
ceil:無條件進位 ceil(3.4)=4 ceil(-3.4)=-3
e.g. 10%3 = 1
/: 整數除法(無條件捨去)
e.g. 10/3 = 3 
m=4 2m=8
0 7 8  15
1 6 9  14
2 5 10 13
3 4 11 12
down %8=0,1,2,3 %8<4
up   %8=4,5,6,7

x->id1 (行數 x越大id1越大)
y->id0 (列數 y越大id0越小) 
n=2 m=2 (-1,1) 0<1>
n=4 m=4 (-3,3) -2 0 2<3>
n=6 m=8 (-7,7) -6 -4 -2 0 2 4 6<7>
n=8 m=16 (-15,15) -14 -12 ... 14<15>
n=n m=2^(n/2) (-m+1, m-1) -m+2 -m ... m m-2<m-1>
                            0 1 2 .. m-2	ceil((.+m-2)/2)
                            m-2 .. 2 1 0	ceil((m-2-.)/2)
e.g. m=4 (-3,-1,1,3) (-2,0,2)
		x-id1	y-id0
-2		0		2
-1.5	1		2
-1		1		2
-0.5	1		2
0		1		1
0.5		2		1
1		2		1
1.5		2		1
2		2		0
*/

int x2id1(int m, double x){	//2 to
	if(x<-m+2) return 0;
	else if(x>m-2) return m-1;
	else return ceil((x+m-2)/2.0);
}

int y2id0(int m, double y){
	if(y<-m+2) return m-1;
	else if(y>m-2) return 0;
	else return ceil((m-2-y)/2.0);
}

int** snake(int m){
    int** snake = malloc(m*sizeof(int*));
    for(i=0; i<m; i++) snake[i] = malloc(m*sizeof(int)); //產生一個int型的m*m 二維陣列 
    
    for(i=0; i<m*m; i++){
        if(i%(2*m)<m) snake[i%m][i/m] = i;		//0,2,4,... 行 (i遞增) e.g.m=4 i%(2*m)=0,1,2,3 
        else snake[m-1-i%m][i/m] = i;			//1,3,5,... 行 (i遞減) e.g.m=4 i%(2*m)=4,5,6,7 
    }
    return snake;
}

int bin2dec(int n, char* s){
	int i=0;
	int sum=0;
	for(i=0; i<n; i++){
		if(s[i]=='1') sum+=pow(2,n-1-i);
	}
	return sum;
	// i=0 s[0]='0'or'1' 2^(n-1)
	// i=1 s[1]='0'or'1' 2^(n-2)
	// i=i s[i]='0'or'1' 2^(n-1-i)
}

void xy2gray(int n, double x, double y){
    int m = (int)pow(2, n/2.0); //2^(n/2) //sqrt(2^n)
    printf("n=%d m=%d \n", n, m);
    int id1 = x2id1(m,x);
    int id0 = y2id0(m,y);
    
    printf("id0=%d id1=%d \n", id0, id1);
    int** s = snake(m);
    int th_gray_code = s[id0][id1];
    printf("th_gray_code=%d \n", th_gray_code);
 
    char** g = gray(n);
    char* bin = malloc(n*sizeof(char));
    for(i=0; i<n; i++) {
		printf("%c", g[th_gray_code][i]);
    	bin[i] = g[th_gray_code][i];
	}
	
    printf("\n");
    int sum = bin2dec(n,bin);
    printf("%d", sum);
}

int main()
{
	int a = 64;	
	int n = (int)sqrt(a); //include <math.h>
	
    //int n=4;
    char** g = gray(n);
    for(i=0; i<pow(2,n); i++){
        for(j=0; j<n; j++){
            printf("%c", g[i][j]);
        }
        printf("\n");
    }
    
    printf("\n snake \n");
    int m=4;
    int** s = snake(m);
    for(i=0; i<m; i++){
        for(j=0; j<m; j++) printf("%d ", s[i][j]);
        printf("\n");
    }

    printf("\n");
    double d=0;
    for(d=-2; d<=2; d+=0.5) printf("%.1lf %d %d\n", d, x2id1(4,d), y2id0(4,d));
    printf("\n");
    for(d=-7; d<=7; d+=0.5) printf("%.1lf %d %d\n", d, x2id1(8,d), y2id0(8,d));
    
    printf("\n");
    xy2gray(n,1.3,-1.5);
    
    return 0;
}
