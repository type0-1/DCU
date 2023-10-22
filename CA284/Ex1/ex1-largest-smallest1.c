/*

Program: ex1-largest-smallest.c
Author: Samson Oloruntola
Input: A string (smallest or largest), followed by float numbers.
Output: The smallest or largest float number.

*/

// Libraries necessary:

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes:

void assign_values(char*[], float[], int);
float compare_string(char[], float[], int);
float smallest(float[], int);
float largest(float[], int);

// Main function:

int main(int argc, char *argv[]){

	int size = argc-2;
	float nums[size];

	assign_values(argv, nums, size); // Assign values to float array

	char string[50];
	strcpy(string, argv[1]); // Copy string from argument to char array
 
	float number = compare_string(string, nums, size); // Resulting number

	printf("%.2f\n", number); // Print number

	return 0;
}

// Function that assigns float numbers to array:

void assign_values(char* argv[], float nums[], int size){
	
	for(int i = 0; i < size; ++i){
		nums[i] = atof(argv[i+2]); // Skipping program name and string.
	}

}

// Function that checks if string is smallest or largest:

float compare_string(char string[], float nums[], int size){

	float number = 0.0;

	if(strcmp("smallest", string) == 0){
		number = smallest(nums, size); // Get smallest number
	}
	else if(strcmp("largest", string) == 0){
		number = largest(nums, size); // Get largest number
	}

	return number; // Return final number

}

// Function that returns the smallest float number:

float smallest(float nums[], int size){
	
	float smallest = nums[0];

	for(int i = 0; i < size; ++i){
		if(smallest > nums[i]){ // If smaller is bigger, update smallest
			smallest = nums[i];
		}
	}

	return smallest; // Return smallest
}

// Function that returns the largest float number:

float largest(float nums[], int size){
	
	float largest = nums[0];

	for(int i = 0; i < size; ++i){
		if(largest < nums[i]){ // If largest is smaller, update largest
			largest = nums[i];
		}
	}

	return largest; // Return largest
}
