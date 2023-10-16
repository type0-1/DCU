/*

Program: lab2-find-even-number.c
Author: Samson Oloruntola
Input: Command-line arguments consisting of numbers.
Output: The index of an even number along with the number found. 

Format: ("index - number").

*/

// Library necessary to run the program:

#include <stdio.h>
#include <stdlib.h>

// Function prototypes:

void assign_values(int, int*, char*[]);
void find_even_numbers(int, int*);

// The main function:

int main(int argc, char *argv[]){
    
    int size = argc-1; // Sets the size of the array minus the program name.
    
    int num_array[size]; 
    
    assign_values(size, num_array, argv); // Assign command-line arguments to array.
    
    find_even_numbers(size, num_array); // Find all even numbers in num_array.
    
    return 0; // Exit program.
}

// Function that assigns command-line arguments to num_array.

void assign_values(int size, int *num_array, char *argv[]){
    
    for(int i = 1; i <= size; ++i){ // i=1 and not 0, as argv[0] is the program name.
        num_array[i-1] = atoi(argv[i]); 
    }
    
}

// Function that finds all even numbers and prints to format.

void find_even_numbers(int size, int *num_array){
    
    for(int i = 0; i < size; ++i){
        if(num_array[i] % 2 == 0){ // If an even number is found, print index and number.
            printf("%d - %d\n", i, num_array[i]);
        }
    }
}


