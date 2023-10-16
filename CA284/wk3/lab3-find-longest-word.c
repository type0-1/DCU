/*

Program: lab3-find-longest-word.c
Author: Samson Oloruntola
Input:  A string.
Output: The longest word in the string.

*/

// Libraries necessary:

#include <stdio.h>
#include <string.h>

// Function prototypes:

int longest_word_index(char[]);
void print_longest_word(char[], int);

// Main function:

int main(int argc, char *argv[]){

	int size = strlen(argv[1]);
	char sentence[size];

	strcpy(sentence, argv[1]);

	int index = longest_word_index(sentence);
	print_longest_word(sentence, index);
	return 0;
}

// Function that gets the index of the longest word:

int longest_word_index(char sentence[]){
	
	int index = 0; // To return the starting index of longest word
	int min = 0; // Min number that tracks the current count of a word
	int max = 0; // Max number that keeps track of the longest length of a word

	for(int i = 0; i < strlen(sentence); ++i){
		if(sentence[i] == ' '){ // If we see a whitespace
			if(min > max){
				max = min; // Update maximum number
				index = i-max; // Index is the current position minus length of current longest word.
			}
			min = 0; // Reset the minimum to zero.
		}
		else{
			min++; // Increment the current length of word
		}
	}

	if(min > max){
		index = strlen(sentence) - min; // In case last word is longest, update index.
	}

	return index;
}


// Function that prints the longest word.

void print_longest_word(char sentence[], int index){
	while(sentence[index] != ' '){ // While we haven't encountered a whitespace character.
		if(sentence[index] == '\0'){ // Check if longest word is encountered at end
			printf("\n", sentence[index]);
			return;
		}
		printf("%c", sentence[index]);
		index++;
	}
	printf("\n");
}