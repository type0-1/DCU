#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

struct Node{
    int val;
    node *next;
};

node *create_list(char*[], int*);

void pop_node(node*);
void push_node(node*, int number);
void print_list(node*);

int main(int argc, char *argv[]){

    node *head = NULL;
    int size = atoi(argv[1]);

    head = create_list(argv, &size);

    int numbers_to_add = (argc - 2) - size;

    for(int i = 0; i < numbers_to_add + 1; ++i){
        pop_node(head);
    }

    for(int i = size + numbers_to_add; i < argc; ++i){
        push_node(head, atoi(argv[i]));
    }

    print_list(head);
    
    return 0;
}

node *create_list(char *argv[], int *size){
    node *head, *current;

    head = (node*)calloc(1, sizeof(node));
    current = head;

    for(int i = 0; i < *size; ++i){
        current->val = atoi(argv[i+2]);
        current->next = (node*)calloc(1, sizeof(node));
        current = current->next;
    }

    return head;
}

void pop_node(node *head){
    node *remove = head;
    node *temp = NULL;

    for(; remove != NULL; remove = remove->next){
        if(!remove->next){
            temp->next = remove->next;
            free(remove);
            remove = temp;
        }
        temp = remove;
    }

}

void push_node(node *head, int value){
    node *push = head;
    node *new_node = (node*)calloc(1, sizeof(node));
    

    for(; push->next != NULL; push = push->next){
    }

    push->next = new_node;
    new_node->val = value;
    new_node->next = NULL;

}

void print_list(node *head){
    node *phead = head;

    for(; phead != NULL; phead = phead->next){
        printf("%d\n", phead->val);
    }
}