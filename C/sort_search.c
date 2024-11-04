#include <stdio.h>
#include <stdlib.h>

int* mergeSort(int n, int* arr){
    if(n==1) return arr;
    int i=0;
    int* left = malloc(n/2*sizeof(int));
    for(i=0; i<n/2; i++) left[i] = arr[i];
    int* right = malloc((n-n/2)*sizeof(int));
    for(i=0; i<n-n/2; i++) right[i] = arr[n/2+i];
    
    left = mergeSort(n/2, left);
    right = mergeSort(n-n/2, right);
    
    int* ans = malloc(n*sizeof(int));
    int l=0, r=0;
    char sign='l';
    for(i=0; i<n; i++){
        if(l>=n/2) sign='r';
        else if(r>=n-n/2) sign='l';
        else{
            if(left[l]<=right[r]) sign='l';
            else sign='r';
            }

        if(sign=='l'){
            ans[i]=left[l];
            l+=1;
        }
        else{
            ans[i]=right[r];
            r+=1;
        }
    }
    return ans;
}

int* gptr;
int gn;
int target;

int binSearch_rec(int l, int r){
    if(l==r){
        if(gptr[l]==target) return l;
        else return -1;
    }
    int m = (l+r)/2;
    if(gptr[m]==target) return m;
    else if(gptr[m]>target) return binSearch_rec(l,m-1);
    else return binSearch_rec(m+1,r);
}

int binSearch_itr(int* arr, int n){
    if(n==1){
        if(arr[0]==target) return 0;
        else return -1;
    }
    int l=0, r=n-1;
    while(l<=r){
        int m = (l+r)/2;
        if(arr[m]==target) return m;
        else if(arr[m]>target) r=m-1;
        else l=m+1;
    }
    return -1;
}

int main()
{
    int i=0, n=10;
    int* r = malloc(n*sizeof(int));
    srand(3);
    for(i=0; i<n; i++) r[i] = rand()%10;
    printf("random arr: ");
    for(i=0; i<n; i++) printf("%d ", r[i]); printf("\n");

    printf("merge arr: ");
    r = mergeSort(n, r);
    for(i=0; i<n; i++) printf("%d ", r[i]); printf("\n");

    gptr = r;
    gn = n;
    target = 4;
    int ans = binSearch_rec(0,gn-1);
    printf("recusrion binsearch %d: %d\n", target, ans);
    
    int ans2 = binSearch_itr(r,n);
    printf("iteration binsearch %d: %d\n", target, ans2);
    
    return 0;
}
