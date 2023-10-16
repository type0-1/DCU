/*

Program: lab2-cylinder-area.c
Author: Samson Oloruntola
Input: Two command-line arguments consisting of a radius and height.
Output: The area computed, using the radius and height.

*/

// Libraries necessary to run the program:

#include <stdio.h>
#include <stdlib.h>

// "#define" used to declare the constant variable "PI".

#define PI 3.1415

// Function prototypes used in the program.

int check_arguments(int, char*[]);
int check_negatives(char*[]);
float compute_area(int, int);

// The main function:

int main(int argc, char *argv[]){
    
    if(check_arguments(argc, argv)){
        return 0; // Exit program if insufficient argument amount.
    }
    else if(check_negatives(argv)){
        return 0; // Exit program if either argument is negative.
    }
    
    int radius = atoi(argv[1]);
    int height = atoi(argv[2]);
    
    printf("%.2f\n", compute_area(radius, height)); // Run the function to compute the area and prints it.
    
    return 0; // Exit program.
}

// Function that calculates and returns the area.

float compute_area(int radius, int height){
    
    float area = 0.0;
    
    area = (2*PI*radius*height) + (2*PI*(radius*radius));
    
    return area; // Returns the area.
}

// Function that checks for the right argument amount.

int check_arguments(int argc, char *argv[]){
    
    if(argc == 1){
        printf("No input given!\n");
        return 1; // Number to exit program if argument(s) is insufficient.
    }
    else if(argc == 2){
        printf("Two arguments needed!\n");
        return 1; // Number to exit program if argument(s) is insufficient.
    }
    
    return 0; // Exit function
    
}

// Function that checks if an argument is negative.

int check_negatives(char *argv[]){
    
    if(atoi(argv[1]) < 0 || atoi(argv[2]) < 0){
        printf("The radius or height cannot be negative!\n");
        return 1; // Number to exit program if argument(s) is insufficient.
    }
    
    return 0; // Exit function.
}