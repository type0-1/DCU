#include <stdio.h>
#include <stdlib.h>

// Function prototypes
void assign_dimensions(int*, int*, int*, int*, char*[]);
void assign_values(int n, int m, int a, int b, int matrix1[][m], int matrix2[][b], char*[]);
void output_multiple(int n, int m, int a, int b, int matrix1[][m], int matrix2[][b]);

int main(int argc, char *argv[]){
    
    int n, m, a, b;
    
    // Parse command line arguments to get matrix dimensions
    assign_dimensions(&n, &m, &a, &b, argv);
    
    // Declare two matrices with the specified dimensions
    int matrix1[n][m];
    int matrix2[a][b];
    
    // Fill the matrices with values from command line arguments
    assign_values(n, m, a, b, matrix1, matrix2, argv);
    
    // Calculate the product of the two matrices and print the result
    output_multiple(n, m, a, b, matrix1, matrix2);
    
    return 0;
}

// Function to parse command line arguments and extract matrix dimensions
void assign_dimensions(int *n, int *m, int *a, int *b, char *argv[]){
    
    // Convert command line arguments to integers and assign them to n, m, a, and b
    *n = atoi(*(argv + 1));
    *m = atoi(*(argv + 2));
    *a = atoi(*((argv + 3) + (*n * *m)));
    *b = atoi(*((argv + 4) + (*n * *m)));
    
}

// Function to fill matrices with values from command line arguments
void assign_values(int n, int m, int a, int b, int matrix1[][m], int matrix2[][b], char *argv[]){
    
    int pos = 0;
    
    // Fill the first matrix with values from command line arguments
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            *(*(matrix1 + i) + j) = atoi(*(argv + pos + 3));
            pos++;
        }
    }
    
    pos = n * m;
    
    // Fill the second matrix with values from command line arguments
    for(int i = 0; i < a; ++i){
        for(int j = 0; j < b; ++j){
            *(*(matrix2 + i) + j) = atoi(*(argv + pos + 5));
            pos++;
        }
    }
    
}

// Function to calculate the product of two matrices and print the result
void output_multiple(int n, int m, int a, int b, int matrix1[][m], int matrix2[][b]){
    
    int total = 0;
    int final_matrix[n][b];
    
    // Calculate the product of the matrices and store the result in final_matrix
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < b; ++j){
            for(int k = 0; k < m; ++k){
                total += *(*(matrix1 + i) + k) * *(*(matrix2 + k) + j);
            }
            
        *(*(final_matrix + i) + j) = total;
        
        total = 0;
        
        }
    }
    
    // Print the result matrix
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < b; ++j){
            if(j+1 == b){
                printf("%d", *(*(final_matrix + i) + j));
            }
            else{
                printf("%d ", *(*(final_matrix + i) + j));
            }
        }
        printf("\n");
    }
}
