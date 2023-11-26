#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct Node node;

int validate_args(char*[], int*);
void calculate_decimal(int*, int*, node*);
node *create_list(int*, char*[]);


struct Node{
    int val;
    node *next;
};

int main(int argc, char *argv[]){

    node *head = NULL;
    if(validate_args(argv, &argc)){
        return 0;
    };

    head = create_list(&argc, argv);

    node *curr = head;

    int degree = (argc-2), total = 0;

    calculate_decimal(&degree, &total, curr);

    printf("%d\n", total);

    return 0;
}

int validate_args(char *argv[], int *argc){
    if((*argc - 1) > 8){
        printf("Too many binary digits entered.\n");
        return 1;
    }
    else{
        for(int i = 1; i < *argc; ++i){
            if(!((*(argv)[i]) == '1' || *(argv)[i] == '0')){
                printf("Only digits 1 and 0 are permitted.\n");
                return 1;
            }
        }
    }
    return 0;
}

node *create_list(int *size, char *argv[]){
    node *head = (node*)calloc(1, sizeof(node)), *current = NULL;

    current = head;
    for(int i = 1; i < *size; ++i){
        current->val = atoi(argv[i]);
        if(i + 1 == *size){
            current->next = NULL;
        }
        else{
            current->next = (node*)calloc(1, sizeof(node));
        }
        current = current->next;
    }
    return head;
}

void calculate_decimal(int *highest_degree, int *total, node *curr){
    while(curr){
        *total += ((2 * curr->val) * pow(2, *highest_degree - 1));
        *highest_degree -= 1;
        curr = curr->next;
    }
}