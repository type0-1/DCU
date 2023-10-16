/*
Program: lab1-rugby-further.c
Author: Samson Oloruntola

Input: 

This program utilizes command-line arguments and uses functions appropriately. 
Input values - try, conversion, penalty and drop-goal.

Output: The calculated score points.
*/

// The libraries needed to run program:

#include <stdio.h>
#include <stdlib.h>

/* The function prototypes:

Double pointers of type "char" is used in the first argument to point to the command-line arguments
in the "int main()" function.

Int is used for the size of the array in the second argument.

*/

int check_negatives(char**, int);
int insufficient_args(char**, int);
int calculate_values(char**);

// The main function.

int main(int argc, char *argv[]){
    
    if(check_negatives(argv, argc)){ // Checks if there is a negative number.
        printf("A negative number has been provided!"); 
        return 0; // Exit program.
    }
    
    if(insufficient_args(argv, argc)){ // Checks if there's insufficient arguments.
        printf("Not enough arguments have been provided!"); 
        return 0; // Exit program.
    }
    
    int total_score = calculate_values(argv); // A new variable "total_score" that stores the total points accumulated.
    
    printf("%d\n", total_score); // Display final score.
    
    return 0; // Exit program.
}

// Function of type "int" that checks if a provided number is negative.

int check_negatives(char **argv, int argc){
    
    // For loop that loops through each command-line argument.
    
    for(int i = 0; i < argc; ++i){
        
        if(atoi(argv[i]) < 0){ // Checks for negative value.
            return 1; // Return "1" if negative.
        }
    }
    
    return 0; // Return "0" if non-negative.
    
}

// Function that checks if the necessary amount of arguments is provided.

int insufficient_args(char **argv, int argc){
    
    int num_of_arguments = (argc-1); // The number of arguments (argc-1) because of the program name included.
    
    if(num_of_arguments < 4){ // Checks if there are less than 4 int arguments.
        return 1; // Return "1" if there's an insufficient amount.
    }
    
    return 0; // Retunrn "0" if there is a sufficient amount.
}

// Function that calculates the total score.

int calculate_values(char **argv){
    
    int tries = (atoi(argv[1]) * 5); // Calculate tries.
    int conversion = (atoi(argv[2]) * 2); // Calculate conversions.
    int penalty = (atoi(argv[3]) * 3); // Calculate penalities.
    int drop_goal = (atoi(argv[4]) * 3); // Calculate drop-goals.
    
    return tries + conversion + penalty + drop_goal; // Return total points.
}