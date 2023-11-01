/*
Author: Samson Oloruntola
Program: ex2-show-cart.c
Input: A product, followed by the amount, price and promotion.
Output: Each products information in each line.
*/

// Necessary libraries:

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struct prototypes:

typedef struct Product products;

// Function prototypes:

void assign_values(int*, char*[], products*);
void print_item(products*);

// Struct initialisation:

struct Product{
    char item[20];
    unsigned int amount;
    float price;
    int promotion;
};

// Main function:

int main(int argc, char *argv[]){

    int product_amount = (argc-1)/4; // The amount of products in the command-line.
    int position = 0; // To iterate through struct array.

    products Products[product_amount]; // Initialize struct array.
    products *pPointer = Products; // Create struct pointer to struct array.

    for(int i = 1; i < argc; i+=4, position++){
        assign_values(&i, argv, (pPointer + position)); 
        print_item((pPointer + position)); // Prints current product
    }

    return 0;
}

// Function that assigns appropriate variables to struct members:

void assign_values(int *i, char *argv[], products *pPointer){

    strcpy(pPointer->item, *(argv + *i)); // Assign product name
    pPointer->amount = atoi(*(argv + (*i + 1))); // Assign product quantity
    pPointer->price = atof(*(argv + (*i + 2))); // Assign product price
    pPointer->promotion = atoi(*(argv + (*i + 3))); // Assign product status

}

// Function that prints the product:

void print_item(products *pPointer){

    if(pPointer->promotion){ // Print item being on sale (On Sale)
        printf("%s, %d, %.2f, On Sale\n", pPointer->item, pPointer->amount, pPointer->price);
    }
    else{ // Print item not being on sale (No Sale)
        printf("%s, %d, %.2f, No Sale\n", pPointer->item, pPointer->amount, pPointer->price);
    }

}