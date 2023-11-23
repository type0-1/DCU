#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

node *assign_nodes(char*[], int*);

void remove_initial_evens(node**);
void remove_evens(node*);
void add_odds(node*, int*);
void push_node(node*, int*);

struct Node{
    int val;
    node *prev;
    node *next;
};

int main(int argc, char *argv[]){
    int size = argc-1, total = 0;
    node *head = assign_nodes(argv, &size);

    remove_initial_evens(&head);

    node *curr = head;

    remove_evens(curr);

    add_odds(head, &total);

    push_node(curr, &total);
    
    curr = head;

    while(curr != NULL){
        printf("%d\n", curr->val);
        curr = curr->next;
    }

    free(head);
    
    curr = NULL;
    return 0;
}

node *assign_nodes(char *argv[], int *size){

    node *head = (node*)calloc(1, sizeof(node));
    node *current = head, *prev = NULL;
    
    for(int i = 0; i < *size; ++i){
        current->prev = prev;
        current->next = (node*)calloc(1, sizeof(node));
        current->val = atoi(argv[i+1]);
        prev = current;
        current = current ->next;
    }

    return head;
}

void remove_initial_evens(node **head){
    while((*head)->val % 2 == 0){
        (*head) = (*head)->next;
        free((*head)->prev);
        (*head)->prev = NULL;
    }
    (*head)->prev = NULL;
}

void remove_evens(node *curr){
    while(curr->next){
        if(curr->val % 2 == 0){
            curr->prev->next = curr->next;
            curr->next->prev = curr->prev;
            node *temp = curr->prev;
            free(curr);
            curr = temp;
        }
        curr = curr->next;
    }

}

void add_odds(node *head, int *total){
    node *curr = head;

    while(curr->next){
        *total += curr->val;
        curr = curr->next;
    }

}

void push_node(node *curr, int *total){

    while(curr->next->next != NULL){
        curr = curr->next;
    }

    node *new_node = (node*)calloc(1, sizeof(node));

    new_node->prev = curr;
    new_node->val = *total;
    new_node->next = NULL;

    curr->next = new_node;

}