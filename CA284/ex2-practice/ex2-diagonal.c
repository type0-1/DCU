/*
Author: Samson Oloruntola
Program: ex2-diagonal.c
Input: First number being the dimension, the rest is a sequence of digits.
Output: The anti-diagonal sum of the matrix.
*/

// Necessary libraries:

#include <stdio.h>
#include <stdlib.h>

// Function prototypes:

void assign_values(int *size, int matrix[][*size], char*[]);
void calculate_diagonal(int *size, int *total, int matrix[][*size]);

// Main function:

int main(int argc, char *argv[]){

    int total = 0; // Used to hold the sum;
    int size = atoi(*(argv + 1)); // Size for matrix.
    int matrix[size][size]; // Integer matrix

    assign_values(&size, matrix, argv);
    calculate_diagonal(&size, &total, matrix);
    printf("%d\n", total);

    return 0;
}

void assign_values(int *size, int matrix[][*size], char *argv[]){

    int pos = 2; // Used to index the command-line arguments.

    for(int i = 0; i < *size; ++i){
        for(int j = 0; j < *size; ++j){

            *(*(matrix + i) + j) = atoi(*(argv + pos)); // Assign number to matrix.
            
            pos++; // Increment to move onto the next command-line argument.

        }
    }
}

// Function that calculates the sum of the anti-diagonal in the matrix.

void calculate_diagonal(int *size, int *total, int matrix[][*size]){

    // Loop through matrix

    for(int i = 0; i < *size; ++i){
        for(int j = *size - i - 1; j > -1; --j){

            // Add the number at the diagonal position to sum.

            *total += *(*(matrix + i) + j);

            break; // Skip to the next diagonal position.
        }
    }
}