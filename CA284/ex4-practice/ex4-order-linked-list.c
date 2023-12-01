#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

node *create_list(char*[], int*);
void check_order(node*, int*);

struct Node{
    float val;
    node *next;
    node *prev;
};

int main(int argc, char *argv[]){
    node *head = NULL, *curr = NULL;

    head = create_list(argv, &argc);
    curr = head->next;

    int check = 0;
    check_order(curr, &check);

    if(check){
        printf("%d\n", 0);
        return 0;
    }
    else{
        printf("%d\n", 1);
        return 0;
    }


}

node *create_list(char *argv[], int *argc){

    node *head = calloc(1, sizeof(node)), *prev = NULL;
    node *curr = head;

    for(int i = 1; i < *argc; ++i){
        curr->prev = prev;
        curr->val = atof(*(argv + i));
        
        if(i + 1 == *argc){
            curr->next = NULL;
        }
        else{
            curr->next = calloc(1, sizeof(node));
        }

        prev = curr;
        curr = curr->next;

    }

    return head;

}

void check_order(node *curr, int *check){
    while(curr->next){
        if(curr->prev->val < curr->val){
            *check = 1;
            return;
        }
        curr = curr->next;
    }
}