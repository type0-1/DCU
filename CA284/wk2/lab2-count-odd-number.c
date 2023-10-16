/*

Program: lab2-count-odd-number.c
Author: Samson Oloruntola
Input: Command-line arguments consisting of numbers.
Output: The amount of odd numbers in the command-line arguments.

*/

// Library necessary to run the program:

#include <stdio.h>
#include <stdlib.h>

// Function prototypes:

void assign_values(int, int*, char*[]);
int count_odd_numbers(int, int*);

// The main function:

int main(int argc, char *argv[]){
    
    int size = argc-1; // Sets the size of the array minus the program name.
    
    int num_array[size]; 
    
    assign_values(size, num_array, argv); // Assign command-line arguments to array.
    
    int count = count_odd_numbers(size, num_array);
    
    printf("%d\n", count); // Print result.
    
    return 0; // Exit program.
}

// Function that assigns command-line arguments to num_array.

void assign_values(int size, int *num_array, char *argv[]){
    
    for(int i = 1; i <= size; ++i){ // i=1 and not 0, as argv[0] is the program name.
        num_array[i-1] = atoi(argv[i]); 
    }
    
}

// Function that counts the number of odd numbers in num_array.

int count_odd_numbers(int size, int *num_array){
    
    int count = 0;
    
    for(int i = 0; i < size; ++i){
        if(num_array[i] % 2){ // Checks for remainder (odd or even).
            count++;
        }
    }
    
    return count;
    
}


