#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

node *create_list(char*[], int*);

void insert_node(node*, int, int);
void print_list(node*);

struct Node{
    int val;
    node *next;
};

int main(int argc, char *argv[]){

    node *head = NULL;
    int list_of_nums[10] = {8, 7, 3, 4, 5, 6, 9, 2, 14, 12};

    head = create_list(argv, list_of_nums);

    insert_node(head, atoi(argv[1]), atoi(argv[2]));

    print_list(head);

    return 0;
}

node *create_list(char *argv[], int *list_of_nums){

    node *head, *current;
    head = (node*)calloc(1, sizeof(node));
    current = head;

    for(int i = 0; i < 10; ++i){
        current->val = *(list_of_nums + i);
        if(i + 1 == 10){
            current->next = NULL;
        }
        else{
            current->next = (node*)calloc(1, sizeof(node));
        }
        current = current->next;
    }

    return head;

}

void insert_node(node *head, int position, int value){
    node *temp_node = head;
    node *temp_node2 = NULL;

    node *new_node = (node*)calloc(1, sizeof(node));
    new_node->val = value;

    for(; temp_node != NULL; temp_node = temp_node->next){

        if(!temp_node->next){
            temp_node->next = new_node;
            new_node->next = NULL;
            return;
        }
        else if(!position){
            temp_node2->next = new_node;
            new_node->next = temp_node;
            return;
        }
        position--;
        temp_node2 = temp_node;
    }


}

void print_list(node *head){
    node *print_node = head;

    for(; print_node != NULL; print_node = print_node->next){
       printf("%d\n", print_node->val);
    }
}