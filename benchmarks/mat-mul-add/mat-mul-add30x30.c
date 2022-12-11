#include <stdio.h>
#include <stdlib.h>
#include"hpm.h"
#define SEED 6
#define R1 30 // number of rows in Matrix-1
#define C1 30 // number of columns in Matrix-1
#define R2 30 // number of rows in Matrix-2
#define C2 30 // number of columns in Matrix-2

void mul_add(int A[R1][C1], int B[R2][C2], int C[R1][C2]){
    for (int i = 0; i < R1; i++) {
        for (int j = 0; j < C2; j++) {
            for (int k = 0; k < R2; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}


int main(){
    int m1[R1][C1], m2[R1][C1], c[R1][C1];
    srand(SEED);
    for (int i = 0; i < R1; i++){
        for (int j = 0; j < C1; j++){
            m1[i][j] = rand();
            m2[i][j] = rand();
            c[i][j] = rand();
        }
    }
    for (int i = 0; i < R1; i++)
        printf("%d, ", m1[i][0]);
    hpm_init();
    mul_add(m1, m2, c);
    hpm_print();
}