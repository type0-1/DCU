#include <stdio.h>
#include <stdlib.h>

void assign_values(int n, int matrix[][n], char*[], int);
void compute_diagonal(int n, int matrix[][n], int*);

int main(int argc, char *argv[]){
    
    int n = atoi(argv[1]);
    int matrix[n][n];
    int result = 0;
    
    assign_values(n, matrix, argv, argc);
    compute_diagonal(n, matrix, &result);
    printf("%d\n", result);
    
    return 0;
}

void assign_values(int n, int matrix[][n], char *argv[], int argc){
    
    int pos = 2;
    
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            *(*(matrix + i) + j) = atoi(argv[pos]);
            pos++;
        }
    }
}

void compute_diagonal(int n, int matrix[][n], int *result){
    
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j, ++i){
            *result += *(*(matrix + i) + j);
        }
    }
    
}
