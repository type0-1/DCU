/*

Program: lab2-print-day.c
Author: Samson Oloruntola
Input: A single integer command-line argument.
Output: The name of the day based on input.

*/

// Library necessary to run the program:

#include <stdio.h>
#include <stdlib.h>

// The main function:

int main(int argc, char *argv[]){
    
    // Create char array which contains days of the week.
    
    char days[7][10] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    
    // Int variable that stores the value of the first command-line argument - 1 to get the array index.
    
    int index = atoi(argv[1])-1;
    
    // Prints day of the week.
    
    printf("%s\n", days[index]);
    
    return 0; // Exit program.
}

