#include <stdio.h>
#include <stdlib.h>

typedef struct{
	double re;
	double im;
}Complex;

Complex cproduct(Complex x, Complex y){
	Complex z;
	z.re = x.re*y.re - x.im*y.im;
	z.im = x.re*y.im + x.im*y.re;
	return z;
}

Complex csum(Complex x, Complex y){
	Complex z;
	z.re = x.re+y.re;
	z.im = x.im+y.im;
	return z;
}

//Complex* convolution(Complex* h, int m, Complex* x, int n){
int autocorr(Complex* h, int m, Complex* x, int n){
    int i=0, j=0;
    
    //reverse h
    //Complex* rh = malloc(m*sizeof(Complex));
    //for(i=0; i<m; i++) rh[i] = h[m-1-i];
	
	//padding x
	int l=2*m+n-2; 
	Complex* xp = malloc(l*sizeof(Complex));
	Complex zero = {0,0};
	for(i=0; i<m-1; i++) xp[i] = zero;
	for(i=m-1; i<m+n-1; i++) xp[i] = x[i-(m-1)];
    for(i=n+m-1; i<l; i++) xp[i] = zero;

    //convolution
    //Complex* c = malloc((m+n-1)*sizeof(Complex));
    //autocorr and find max index
    int max_index = 0;
    int max_value = 0;
    for(i=0; i<m+n-1; i++){
    	Complex sum = zero;
    	for(j=0; j<m; j++) sum = csum(sum, cproduct(h[m-j-1], xp[m-j-1+i])); //sum=sum+h[]*xp[]
		if(sum.re*sum.re+sum.im*sum.im>max_value){
		    max_value = sum.re*sum.re+sum.im*sum.im;
		    max_index = i;
		}
		//c[i] = sum;
	}
	//sum: 			2 0 1 5 4 1
	//max_value: 0  2 2 2 5 5 5
	//max_index: 0  0 0 0 3 3 3
	
    //return c;
    return max_index;
}

int main()
{
    int i=0;
    
    int m=5;
    Complex* h = malloc(m*sizeof(Complex));
    h[0].re=5; h[0].im=0;
    h[1].re=4; h[1].im=0;
    h[2].re=3; h[2].im=0;
    h[3].re=2; h[3].im=0;
    h[4].re=1; h[4].im=0;
	 
	int n=9;
	Complex* x = malloc(n*sizeof(Complex));
    x[0].re=0; x[0].im=0;
	x[1].re=1; x[1].im=0;
	x[2].re=0; x[2].im=0;
	x[3].re=1; x[3].im=0;
	x[4].re=1; x[4].im=0;
	x[5].re=1; x[5].im=0;
	x[6].re=0; x[6].im=0;
	x[7].re=1; x[7].im=0;
	x[8].re=0; x[8].im=0;
    
    //Complex* c = convolution(h, m, x, n);
    //for(i=0; i<m+n-1; i++) printf("%f+%fi \n", c[i].re, c[i].im);
    
    printf("%d ", autocorr(h, m, x, n));
    
    return 0; 
}
