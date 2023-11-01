/*
Author: Samson Oloruntola
Program: ex2-discount.c
Input: A product, followed by the amount, price and promotion.
Output: The total amount of money to be paid, including discount.
*/

// Necessary libraries:

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struct prototypes:

typedef struct Product products;

// Function prototypes:

void assign_values(int*, char*[], products*);
void calculate_price(int*, products*);

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
    int total = 0; // Variable to hold total price

    products Products[product_amount]; // Initialize struct array.
    products *pPointer = Products; // Create struct pointer to struct array.

    for(int i = 1; i < argc; i+=4, position++){
        assign_values(&i, argv, (pPointer + position)); // Assigns values
        calculate_price(&total, (pPointer + position)); // Calculates price
    }

    printf("%d\n", total); // Print total

    return 0;
}

// Function that assigns appropriate variables to struct members:

void assign_values(int *i, char *argv[], products *pPointer){

    strcpy(pPointer->item, *(argv + *i)); // Assign product name
    pPointer->amount = atoi(*(argv + (*i + 1))); // Assign product quantity
    pPointer->price = atof(*(argv + (*i + 2))); // Assign product price
    pPointer->promotion = atoi(*(argv + (*i + 3))); // Assign product status

}

// Function that calculates the price:

void calculate_price(int *total, products *pPointer){

    if(pPointer->promotion){
        // Loop from the 1st amount to the amount purchased.
        for(int i = 1; i != pPointer->amount; ++i){
            if(i % 3 == 0){ // If there are three items, add the price of two to the total.
                *total += pPointer->price * 2; 
            }
        }
        // Add the remaining product price to the total.
        *total += (pPointer->amount % 3) * pPointer->price;

    }

    else{
        // Add the money sum of the product if there's no sale.
        *total += pPointer->amount * pPointer->price;
    }

}