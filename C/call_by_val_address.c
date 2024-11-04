#include <stdio.h>
#include <stdlib.h>
//cbv: call by value 		(非指標變數，複製獨立一份)
//cba: call by address/pointer 	(指標變數，建立捷徑)

//a add 1 call by value
int cbv_int(int x){         	//int x = a, x為獨立一份
	x = x+1;                //改x不影響a
	return x;               //return改過的x(要用a去接)
}

//a add 1 call by address
void cba_int(int* ptr){     	//int* ptr = &a, ptr為a之地址, *ptr即a
	*ptr = *ptr + 1;        //改*ptr就是改a, 所以不須回傳
}

//arr add 1 call by address
void cba_arr(int* ptr, int n){	//int* ptr = arr, ptr即arr即陣列第0個元素地址, *ptr為陣列第0個元素
	int i;
	for(i=0; i<n; i++) ptr[i] = ptr[i]+1; //改*ptr就是改*arr, 因此不須回傳
}

int ga = 3;			//global variable
//global a add 1 call by none
void cbn_int(){
	ga = ga+1;
}

int* garr;
//global arr add 1 call by none
void cbn_arr(){
	int i=0;
	for(i=0; i<=3; i++) garr[i]+=1;
}

int main()
{
	int a=5;		//獨立於global a
	a = cbv_int(a);
	printf("%d \n", a);

	cba_int(&a);
	printf("%d \n", a);
    
	int* arr = calloc(3, sizeof(int));	//arr是陣列第0個元素地址, *arr=arr[0]=陣列第0個元素
	cba_arr(arr, 3);
	int i;
	for(i=0; i<3; i++) printf("%d ", arr[i]); printf("\n");
	
	cbn_int();
	printf("%d", ga);
	
	garr = calloc(3, sizeof(int));
	cbn_arr();
	for(i=0; i<3; i++) printf("%d ", garr[i]); printf("\n");

    	return 0;
}
