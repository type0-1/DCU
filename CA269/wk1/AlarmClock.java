import java.util.Scanner;

public class AlarmClock{
    public static void main(String[] args){
        
        Scanner input = new Scanner(System.in);
        
        int currentTime = input.nextInt()*60 + input.nextInt();
        int false_alarms = 0;
        
        while(input.nextInt()*60 + input.nextInt() < currentTime){
            false_alarms++;
        }
        
        System.out.println("false alarms: " + false_alarms);

        input.close();
    }
}