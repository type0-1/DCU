#include <stdio.h> // Stdin.io 
#include <stdlib.h> // Stdin Library
#include <string.h> // String library


/* Declaration of a "float" function which gets the largest float number.
   This is done so via comparison of which number is bigger*/

float getLargest(float number, float largest){ // Takes two float parameters:-> (The next number to compare to, The current largest number)
    if (number > largest){
        largest = number; // Change float variable "largest" to bigger number.
    }
    return largest;
}

/* Declaration of a "float" function which gets the smallest float number.
   This is done so via comparison of which number is smaller*/

float getSmallest(float number, float smallest){ // Takes two float parameters:-> (The next number to compare to, The current smallest number)
    if (smallest > number){
        smallest = number; // Change float variable "smallest" to smaller number.
    }
    return smallest;
}

/* The main function, which is called when the program is ran. */

int main(int argc, char*argv[]){
    if (strcmp(argv[1], "largest") == 0){ // Compares argv[1], which is a string to see if it is the same as "largest".
        float largest = atof(argv[2]);
        for (int i = 2; i < argc; ++i){ // Loops through each float number in the command-line arguments passed.
          largest = getLargest(atof(argv[i]), largest);  // Make float number "largest" = to the biggest number obtained from "getLargest" function.
        }
        printf("%.2f\n", largest); // Prints largest number.
    }
    else if (strcmp(argv[1], "smallest") == 0){ // Compares argv[1], which is a string to see if it is the same as "smallest".
        float smallest = atof(argv[2]);
        for (int i = 2; i < argc; ++i){ // Loops through each float number in the command-line arguments passed.
            smallest = getSmallest(atof(argv[i]), smallest); // Make float number "smallest" = to the biggest number obtained from "getSmallest" function.
        }
        printf("%.2f\n", smallest); // Prints smallest number.
    }
    return 0;
}