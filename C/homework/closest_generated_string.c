#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void print2D(int** A, int row, int col){
    int i, j;
    for(i=0; i<row; i++){
        for(j=0; j<col; j++) printf("%d ", A[i][j]);
        printf("\n");
    }
    printf("\n");
}

int** zeroMatrix(int row, int col){
    int** Z = malloc(row*sizeof(int*));
    int i;
    for(i=0; i<row; i++) Z[i] = calloc(col, sizeof(int));
    return Z;
}

int** binaryMatrix(int n){
    int** B = zeroMatrix(pow(2,n), n);
    int i,j;
    for(i=0; i<pow(2,n); i++){
        int num = i;
        for(j=0; j<n; j++){
            if(num>=pow(2,n-1-j)){
                B[i][j] = 1;
                num-=pow(2,n-1-j);
            }
        }
    }
    return B;
}
/* n=3
000
001
010
011
100
101
110
111
*/

int** generatorMatrix(int n, int m){
    int** G = zeroMatrix(n, m);
    int i,j;
    for(i=0; i<n; i++){
        for(j=0; j<m; j++) G[i][j] = rand()%2;
    }
    return G;
}

int** matrixMult(int** A, int** B, int m, int n, int p){
    int** C = zeroMatrix(m,p);
    int i,j,k;
    for(i=0; i<m; i++){
        for(j=0; j<p; j++){
            for(k=0; k<n; k++) C[i][j] = (C[i][j] + A[i][k]*B[k][j])%2;
        }
    }
    return C;
}

int** randMatrix(int m){
    int** R = zeroMatrix(1, m);
    int i=0;
    for(i=0; i<m; i++) R[0][i] = rand()%2;
    return R;
}

void compare(int** L, int** R, int p, int m){
    int min_index=0, min_diff=m;
    int i, j =0;
    for(i=0; i<p; i++){
        int diff = 0;
        for(j=0; j<m; j++){
            if(R[0][j]!=L[i][j]) diff+=1;
        }
        if(diff<min_diff){
            min_index = i;
            min_diff = diff;
        }
    }
    printf("%d %d", min_index, min_diff);
}

int main()
{
    srand(time(0));
    
    int n = 3;
    int** B = binaryMatrix(n);
    print2D(B, pow(2,n), n);
    
    int m = 6;
    int** G = generatorMatrix(n,m);
    print2D(G, n, m);
    
    int** L = matrixMult(B, G, pow(2,n), n, m);
    print2D(L, pow(2,n), m);
    
    int** R = randMatrix(m);
    print2D(R, 1, m);
    
    compare(L, R, pow(2,n), m);
    
    return 0;
}
