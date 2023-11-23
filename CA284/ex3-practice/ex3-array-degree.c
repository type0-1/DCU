#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

node *create_linked_list(char*[], int*);

void sort_list(node*);
void find_degree(node*, int*);

struct Node{
    int val;
    node *next;
};

int main(int argc, char *argv[]){

    node *head = NULL, *curr = NULL;
    int size = (argc-1), degree = 1;

    head = create_linked_list(argv, &size);

    curr = head;
    sort_list(curr);
    
    curr = head;
    
    find_degree(curr, &degree);

    printf("%d\n", degree);

    free(head);
    curr = NULL;

    return 0;
}

node *create_linked_list(char *argv[], int *size){
    node *head = (node*)calloc(1, sizeof(node)), *curr = NULL;
    curr = head;

    for(int i = 0; i < *size; ++i){
        curr->val = atoi(argv[i+1]);
        curr->next = (node*)calloc(1, sizeof(node));
        curr = curr->next;
    }

    curr->next = NULL;

    return head;
}

void sort_list(node *curr){
    
    while(curr->next){
        node *next_node = curr->next;

        while(next_node->next){

            if(curr->val > next_node->val){
                int temp = curr->val;
                curr->val = next_node->val;
                next_node->val = temp;
            }

            next_node = next_node->next;

        }

        curr = curr->next;
    }

}

void find_degree(node *curr, int *degree){

    int n = curr->val, count = 0;

    while(curr->next){
        if(n == curr->val){
            count++;
        }
        else{
            if(count > *degree){
                *degree = count;
            }
            count = 1;
            n = curr->val;
        }
        curr = curr->next;
    }

    if(count > *degree){
        *degree = count;
    }
    
}