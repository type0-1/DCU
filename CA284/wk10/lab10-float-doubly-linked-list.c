#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

node *create_list(char*[], int*);
void print_values(node*);


struct Node{
    float val;
    node *next;
    node *prev;
};

int main(int argc, char *argv[]){

    node *head = NULL;
    int size = atoi(argv[1]);

    head = create_list(argv, &size);
    print_values(head);

    return 0;
}

node *create_list(char *argv[], int *size){
    node *head, *current, *prev;

    head = (node*)calloc(1, sizeof(node));
    head->prev = NULL;
    current = head;


    for(int i = 0; i < *size; ++i){
        prev = current;
        current->val = atof(argv[i+2]);
        current->next = (node*)calloc(1, sizeof(node));
        current = current->next;
        current->prev = prev;
    }

    return current->prev;

}

void print_values(node *head){
    node *phead= head;

    for(; phead != NULL; phead = phead->prev){
        printf("%.2f\n", phead->val);

    }
}