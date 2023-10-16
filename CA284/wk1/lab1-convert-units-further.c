/*

Program: lab1-convert-units-further.c
Author: Samson Oloruntola
Input: The variable "lower", set to the value "30".
Output: The units converted, displayed in a 4x5 row to column layout.

*/

// Libraries needed to use the program.

#include <stdio.h>

// The main function .

int main(int argc, char *argv[]){
    
    int cm = 30; // The starting input.
    
    // Nested for loop to print out results.
    
    for(int i = 0; i < 4; ++i){ // Loop 1 -> Needed for row formatting.
    
        for(int j = 0; j < 5; ++j){ // Loop 2 -> Needed for column formatting.
        
            printf("%.2f\t ", cm/2.54); // Prints out each unit conversion using "\t" to pad space..
            
            cm++; // Increment "cm" to calculate the next value.
        }
        printf("\n"); // Newline character to print out the next row.
    }
    
    return 0; // Exits the main function.
}