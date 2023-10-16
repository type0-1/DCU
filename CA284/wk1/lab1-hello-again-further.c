/*

Program: lab1-hello-again-further.c
Author: Samson Oloruntola
Input: A character array displaying my full name "Samson Oloruntola".
Output: A welcome message with the two words "Hello 
                                              Samson Oloruntola" printed.
                                              

*/

// Libraries needed to use the program.

#include <stdio.h>
#include <stdlib.h>

// The main function.

int main(int argc, char *argv[]){
    
    char full_name[20]; // Creating a string/character array, assigning memory of size "20".
    fgets(full_name, 20, stdin); // Reading input from the user using fgets to read pass whitespace.
    
    printf("Hello\n%s\n", full_name); // Prints the final output, the greeting followed by a newline character.
                                      // Then it prints the full name and then a newline character again.
    
    return 0; // Exits the main function.
}