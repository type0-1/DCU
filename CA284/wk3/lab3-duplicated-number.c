/*

Program: lab3-duplicated-number.c
Author: Samson Oloruntola
Input:  A number to search for, followed by a sequence of numbers.
Output: The duplicated numbers, if none found, print "no duplicated found".

*/

// Libraries necessary:

#include <stdio.h>
#include <stdlib.h>

// Function prototypes:

void assign_values(int, int[], char*[]);
void find_duplicate(int, int, int[]);

// Main Function:

int main(int argc, char *argv[]){

	int size = argc-2; // Get the input size of the command-line arguments.
	int search = atoi(argv[1]); // The number we're searching for.
	int num_array[size]; // Initialize int array.

	assign_values(size, num_array, argv);
	find_duplicate(search, size, num_array);

	return 0;
}

// Function that assigns command-line arguments to int array:

void assign_values(int size, int num_array[], char *argv[]){

	for(int i = 0; i < size; ++i){
		num_array[i] = atoi(argv[i+2]);
	}

}

// Function that searches through int array to find duplicate.

void find_duplicate(int search, int size, int num_array[]){

	int flag = 0; // Flag that confirms if there's a duplicate or not.

	for(int i = 0; i < size; ++i){
		if(search == num_array[i]){
			printf("%d\n", search);

			flag = 1; // Duplicate number found.
		}
	}
	
	if(flag == 0){
		printf("no duplicated number\n");
	}

}