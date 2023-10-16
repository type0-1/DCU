/*

Program: lab2-draw-empty-square.c
Author: Samson Oloruntola
Input: An integer determining the size of the square.
Output: An empty square.

*/

// Library necessary to run the program:

#include <stdio.h>
#include <stdlib.h>

// Function prototypes:

void draw_square(int);

// The main function:

int main(int argc, char *argv[]){

    int square_size = atoi(argv[1]);
    draw_square(square_size);
    
    return 0; // Exit program.
}

// Function that draws the empty square:

void draw_square(int square_size){
    
    for(int i = 0; i < square_size; ++i){ // Loop 1 which iterates from 1 to square_size.
        
        if(i == 0 || i == square_size-1){ // Checks if we're at the start or end of square.
            for(int j = 0; j < square_size; ++j){ // If so, print every spot with an asterisk.
                printf("*");
            }
            
        }
        
        else{
            
            printf("*"); // Print an asterisk at the start
            for(int j = 0; j < square_size-2; ++j){
                printf(" "); // Print (square_size-2) spaces, (because two asterisks are printed at the start and end).
            }
            printf("*"); // Print an asterisk at the end
            
        }
        printf("\n"); // Newline character.
    }
    
}

