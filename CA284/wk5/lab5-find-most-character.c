#include <stdio.h>
#include <string.h>

void get_frequent(char[], char);

int main(int argc, char *argv[]){
    
    int length = strlen(argv[1]);
    char string[length];
    char most_frequent = 'a';
    
    strcpy(string, argv[1]);
    
    get_frequent(string, most_frequent);
    
    return 0;
}

void get_frequent(char string[], char most_frequent){
    
    char *pos = string;
    
    int min = 0;
    int max = 0;
    
    while(*pos != '\0'){
        
        char *pos2 = pos+1;
        
        while(*pos2 != '\0'){
            
            if (*pos2 != ' ' && *pos == *pos2){
                
                min++;
                
            }
            
            pos2++;
        }
        
        if(min > max){
            max = min;
            min = 0;
            most_frequent = *pos;
        }
        
        pos++;
        
    }
    
    printf("%c\n", most_frequent);
    
}