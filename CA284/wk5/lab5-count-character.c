
/*

Program: lab5-count-character.c
Author: Samson Oloruntola
Input: A letter to find, along with a string.
Output: The amount of occurences of the letter.

*/

// Libraries necessary:

#include <stdio.h>
#include <string.h>

// Function prototypes:

void count_character(char*, char[], int*, int*);

// Main function:

int main(int argc, char *argv[]){
    
    int length = strlen(argv[2]);
    int count = 0;
    
    char string[length];
    
    strcpy(string, argv[2]);
    
    count_character(argv[1], string, &length, &count);
    
    printf("%d\n", count);
    
    return 0;
}

// Function to computes the occurences of the letter:

void count_character(char *chr, char string[], int *length, int *count){
    
    char *pos = &string[0];
    
    while(*pos != '\0'){
        if(*chr == *pos){
            *count += 1;
        }
        pos++;
    }
    
}