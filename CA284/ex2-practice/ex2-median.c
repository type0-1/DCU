/*
Author: Samson Oloruntola
Program: ex2-median.c
Input: Sequence of numbers provided in the command-line arguments
Output: The median of the provided sequence of numbers.
*/

// Necessary libraries:

#include <stdio.h>
#include <stdlib.h>

// Function prototypes:

void assign_values(int*, int*, char*[]);
void sort_array(int*, int*);
void find_median(int*, int*);
void print_median(int*, int*);

// Main function:

int main(int argc, char *argv[]){
    
    int size = (argc-1); // Size of the array;

    int num_array[size]; // Num array.

    assign_values(&size, num_array, argv);
    sort_array(&size, num_array);
    find_median(num_array, &size);

    return 0;
}

// Function that assigns values to the integer array.

void assign_values(int *size, int *num_array, char *argv[]){

    for(int i = 0; i < *size; ++i){
        *(num_array + i) = atoi(*(argv + (i + 1)));
    }

}

// Function that sorts the array using bubble sort.

void sort_array(int *size, int *num_array){

    // Goal is to swap the array in ascending order.

    for(int i = 0; i < *size; ++i){
        for(int j = i+1; j < *size; ++j){

            if(*(num_array + i) > *(num_array + j)){
                // Swap if number at position i is bigger than number at position j.
                int tmp = *(num_array + i);
                *(num_array + i) = *(num_array + j);
                *(num_array + j) = tmp;

            }
        }
    }
}

// Function that finds the two median numbers.

void find_median(int *num_array, int *size){

    int i = 0;

    // Increment i until the median is reached.

    while(i + 1 != *size / 2){
        ++i;
    }
    
    // Print the two median numbers.

    print_median(num_array + i, num_array + (i + 1));

}

// Function that prints the two median numbers.

void print_median(int *n1, int *n2){
    printf("%d\n%d\n", *n1, *n2);
}