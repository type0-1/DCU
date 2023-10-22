/*

Program: ex1-is-symmetric.c
Author: Samson Oloruntola
Input: A single string.
Output: "yes" or "no" depending if the string is symmetric.

*/

// Libraries necessary:

#include <stdio.h>
#include <string.h>

// Function prototypes:

int check_symmetry(char[], int);
void print_result(int);

// Main function:

int main(int argc, char *argv[]){

	int size = strlen(argv[1]); // Get string length
	char string[size];
	strcpy(string, argv[1]); // Copy input to char array

	int symmetric = check_symmetry(string, size); // 1 if symmetric, 0 otherwise

	print_result(symmetric); // Prints the result

	return 0;
}

// Function that checks for string symmetry:

int check_symmetry(char string[], int size){

	int symmetric = 0;

	// For loop checking that opposite positions are the same letter

	for(int i = 0; i < size / 2; ++i){ 
		if(string[i] != string[size - i - 1]){
			return 0; // Return not symmetric
		}
	}

	return 1; // Return is symmetric

}

// Function that prints if symmetric or not:

void print_result(int symmetric){

	if(symmetric){
		printf("yes\n");
	}
	else{
		printf("no\n");
	}

}