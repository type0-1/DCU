#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node node;

node *create_list(char *argv[], int*);

void find_ireland_products(node*);
void update_prices(node*);
void print_products(node*);

struct Node{
    char *code;
    char *country;
    unsigned int price;
    node *next;  
};


int main(int argc, char *argv[]){

    node *head = NULL;

    head = create_list(argv, &argc);
    
    node *curr = head;

    find_ireland_products(curr);

    curr = head;

    print_products(curr);

    free(head);
    curr = NULL;

    return 0;
}

node *create_list(char *argv[], int *size){
    
    node *head = (node*)calloc(1, sizeof(node)), *current = NULL;
    current = head;


    for(int i = 1; i < *size; i += 3){

        current->code = (char*)calloc(strlen(argv[i]), sizeof(char));
        current->country = (char*)calloc(strlen(argv[i+1]), sizeof(char));

        strcpy(current->code, argv[i]);
        strcpy(current->country, argv[i+1]);
        current->price = atoi(argv[i+2]);

        current->next = (node*)calloc(1, sizeof(node));
        current = current->next;

    }

    return head;

}

void find_ireland_products(node *curr){
    while(curr->next){
        if(strcmp(curr->country, "Ireland") == 0){
            update_prices(curr);
        }
        curr = curr->next;
    }
}

void update_prices(node *curr){
    curr->price = curr->price + (curr->price * .20);
}

void print_products(node *curr){
    while(curr->next){
        printf("%s\n%s\n%d\n", curr->code, curr->country, curr->price);
        curr = curr->next;
    }
}