#include <stdio.h>
#include <stdlib.h>

typedef struct Node node;

node *create_list(char*[], int*, int*);
void print_list(node*);

struct Node{
	int val;
	node *next;
};

int main(int argc, char *argv[]){

	node *head = NULL;
	int size = atoi(argv[1]);

	head = create_list(argv, &argc, &size);

	print_list(head);

	return 0;
}

node *create_list(char *argv[], int *argc, int *size){

	node *head, *current;
	head = (node*)calloc(1, sizeof(node));
	current = head;

	for(int i = 0; i < *size; ++i){
		if(i + 1 == *argc){
			current->val = atof(argv[i+2]);
			current->next = NULL;
			current = current->next;
		}
		else{
			current->val = atof(argv[i+2]);
			current->next = (node*)calloc(1, sizeof(node));
			current = current->next;
		}
	}

	return head;

}

void print_list(node *head){

	node *current = head;

	for(; current->next != NULL; current = current->next){
		printf("%d\n", current->val);
	}

}