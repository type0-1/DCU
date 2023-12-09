#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

node *create_list(char*[], int*);
void remove_duplicates(node*);

struct Node{
    int val;
    node *next;
    node *prev;
};

int main(int argc, char *argv[]){
    if(argc-1 == 1){
        printf("%d\n", atoi(argv[1]));
        return 0;
    }

    node *head = NULL;
    head = create_list(argv, &argc);
    node *curr = head;

    remove_duplicates(curr);

    return 0;
}

node *create_list(char *argv[], int *argc){
    node *head = calloc(1, sizeof(node));
    node *prev = NULL;
    node *curr = head;

    for(int i = 1; i < *argc; ++i){
        curr->val = atoi(argv[i]);
        curr->prev = prev;
        curr->next = calloc(1, sizeof(node));
        prev = curr;
        curr = curr->next;
    }

    curr->next = NULL;
    return head;
}

void remove_duplicates(node *curr){
    int count = 1;
    while(curr->next){
        node *new = curr->next;
        while(new->next){
            if(new->val == curr->val){
                node *temp = new->prev;
                new->prev->next = new->next;
                new->next->prev = new->prev;
                free(new);
                new = temp;
                count++;
            }
            new = new->next;
        }
        if(count == 1){
            printf("%d\n", curr->val);
        }
        else{
            curr->val = -1;
        }
        count = 1;
        curr = curr->next;
    }
}