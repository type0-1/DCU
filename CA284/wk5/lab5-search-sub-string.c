#include <stdio.h>
#include <string.h>

void assign_strings(char[], char[], char *argv[]);
void search_sub_string(char[], char[], int*, int*);

int main(int argc, char *argv[]){
    
    char sentence[strlen(argv[1])];
    char word[strlen(argv[2])];
    
    assign_strings(sentence, word, argv);
    
    int first = 0, last = 0;
    
    search_sub_string(sentence, word, &first, &last);
    
    printf("%d %d\n", first, last);
    
    return 0;
    
}

void assign_strings(char sentence[], char word[], char *argv[]){
    
    strcpy(sentence, argv[1]);
    strcpy(word, argv[2]);
    
};

void search_sub_string(char sentence[], char word[], int* first, int* last){
    
    char *pStart = sentence;
    int index = 0;
    int keep_count = 1;
    
    for(; *pStart != '\0'; pStart++){
        
        if(*pStart == word[0]){
            
            char *pStart2 = word;
            *first = index;
            
            while(*pStart == *pStart2 && *pStart2 != '\0'){
                pStart++;
                pStart2++;
                keep_count++;
                
            }
        }
        
        if(keep_count == strlen(word)){
            *last = *first+keep_count-1;
            break;
        }
        
        keep_count = 0;
        index++;
    }
    
}