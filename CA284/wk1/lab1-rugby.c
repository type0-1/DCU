/*
Program: lab1-rugby.c
Author: Samson Oloruntola

Input: 
Four values to represent the points: (try, conversion, penalty and drop-goal).


Output: The calculated score points.
*/

// Libraries needed for the program.

#include <stdio.h>
#include <stdlib.h>

// The main function.

int main(int argc, char *argv[]){

    int try = atoi(argv[1]) * 5; // Calculate try points.

    int conversion = atoi(argv[2]) * 2; // Calculate conversion points.

    int penalty = atoi(argv[3]) * 3; // Calculate penalty points.

    int drop_goal = atoi(argv[4]) *3; // Calculate drop-goal points.

    printf("%d\n", try + conversion + penalty + drop_goal); // Print the total points

    return 0; // Exit program.
}