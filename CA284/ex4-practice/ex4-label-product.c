#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node node;

node *create_list(int*, char*[]);
void assign_code(char**, char*);
void calculate_average(int*, node*);
void update_status(int*, node*);
void print_countries(node*);

struct Node{
    char *code;
    float price;
    unsigned int items;
    int status;
    node *next;
};

int main(int argc, char *argv[]){
    node *head = NULL, *curr = NULL;
    int average = 0;

    head = create_list(&argc, argv);
    curr = head;

    calculate_average(&average, curr);
    
    average /= (argc / 3);
    curr = head;

    update_status(&average, curr);

    curr = head;

    print_countries(curr);

    return 0;
}

node *create_list(int *argc, char *argv[]){

    node *head = calloc(1, sizeof(node)), *curr = NULL;
    curr = head;

    for(int i = 1; i < *argc; i+=3){
        assign_code(&curr->code, *(argv + i));
        curr->price = atof(*(argv + i + 1));
        curr->items = atoi(*(argv + i + 2));
        curr->status = 0;

        if(i + 1 == *argc){
            curr->next = NULL;
        }
        else{
            curr->next = calloc(1, sizeof(node));
        }

        curr = curr->next;

    }

    return head;

}

void assign_code(char **code, char *string){

    char comparison[3] = {string[0], string[1], '\0'};

    if(strcmp("IE", comparison) == 0){
        *code = calloc(7, sizeof(char));
        strcpy(*code, "Ireland");
    }
    else if(strcmp("FR", comparison) == 0){
        *code = calloc(6, sizeof(char));
        strcpy(*code, "France");
    }
    else if(strcmp("SP", comparison) == 0){
        *code = calloc(5, sizeof(char));
        strcpy(*code, "Spain");
    }
    else if(strcmp("US", comparison) == 0){
        *code = calloc(3, sizeof(char));
        strcpy(*code, "USA");
    }
    else{
        *code = calloc(6, sizeof(char));
        strcpy(*code, "Russia");
    }
}

void calculate_average(int *average, node *curr){
    while(curr->next){
        *average += curr->price * curr->items;
        curr = curr->next;
    }
}

void update_status(int *average, node *curr){
    while(curr->next){
        if((curr->price * curr->items) > *average){
            curr->status = 1;
        }
        curr = curr->next;
    }
}

void print_countries(node *curr){
    while(curr->next){
        printf("%d\n%s\n", curr->status, curr->code);
        curr = curr->next;
    }
}