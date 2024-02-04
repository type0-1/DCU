import java.util.Scanner;

public class VowelAge{
    
    public static void main(String[] args){
        
        Scanner input = new Scanner(System.in);
        
        String name = input.nextLine();
        char[] vowels = "aeiouAEIOU".toCharArray();
        
        int vowel = 0;
        
        for(int i = 0; i < name.toCharArray().length; ++i){
            for(int j = 0; j < vowels.length; ++j){
                if((name.toCharArray())[i] == vowels[j]){
                    vowel++;
                }
            }
        }
        
        int age = input.nextInt();
        
        if(check_age(age)){
            System.out.println("Hello " + name + ", you have " + vowel + " vowels, and are a minor");
        }
        else{
            System.out.println("Hello " + name + ", you have " + vowel + " vowels, and are an adult");
        }

        input.close();
        
    }
    
    public static boolean check_age(int age){
        if(age > 18){
            return false;
        }
        return true;
    }
}