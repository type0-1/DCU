#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node node;

node *create_list(char*);
void include_quote_sentence(int*, int*, char*);
void shift_index(char*, int*);
void get_shortest(node*, int*);
void get_largest(node*, int*);
void print_output(node*, int*);

struct Node{
    char *sentence;
    node *next;
};

int main(int argc, char *argv[]){

    node *head = NULL, *curr = NULL;
    head = create_list(*(argv + 1));

    int desired_length = 0;
    void (*pFunction)(node*, int*);

    curr = head;

    if(strcmp("shortest", *(argv + 2)) == 0){
        pFunction = get_shortest;
        pFunction(curr, &desired_length);
        
    }
    else if(strcmp("longest", *(argv + 2)) == 0){
        pFunction = get_largest;
        pFunction(curr, &desired_length);
    }
    else{
        printf("Not valid!\n");
        return 0;
    }

    pFunction = print_output;
    pFunction(curr, &desired_length);

    return 0;
}

node *create_list(char *string){
    node *head = calloc(1, sizeof(node));
    node *current = head;

    int length = 1, index = 0, string_index = 0;

    for(int i = 0; i < strlen(string); ++i){
        if(*(string + i) == '\''){
            i++, length++;
            include_quote_sentence(&i, &length, string);
        }
        if(*(string + i) == '.' || *(string + i) == '?'){

            current->sentence = calloc(length+1, sizeof(char)); 

            for(; index <= i; ++index, ++string_index){
                *(current->sentence + string_index) = *(string + index);
            }

            current->next = calloc(1, sizeof(node));
            current = current->next;

            length = 1;
            index += 1;
            string_index = 0;
            
        }
        else{
            length++;
        }
    }

    current->next = NULL;

    return head;
}

void include_quote_sentence(int *i, int *length, char *string){
    while(*(string + *i) != '\''){
        *i += 1, *length += 1;
    }
}

void get_shortest(node *curr, int *shortest){
    *shortest = strlen(curr->sentence);

    while(curr->next){
        if(strlen(curr->sentence) < *shortest){
            *shortest = strlen(curr->sentence);
        }
        curr = curr->next;
    }
}

void get_largest(node *curr, int *largest){
    *largest= strlen(curr->sentence);
    
    while(curr->next){
        if(strlen(curr->sentence) > *largest){
            *largest = strlen(curr->sentence);
        }
        curr = curr->next;
    }
}

void print_output(node *curr, int *desired_length){
    while(curr->next){
        if(strlen(curr->sentence) == *desired_length){
            printf("%d\n%s\n", *desired_length, curr->sentence);
            return;
        }
        curr = curr->next;
    }
}
