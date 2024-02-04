import java.time.LocalDate;
import java.time.Period;

enum State{
    TODO, BEGN, HALT, WAIT, DONE;
}

public class Task{

    private String title;
    private String description;

    private LocalDate scheduled;
    private LocalDate deadline;

    State state;

    
    public Task(String title, State state){
        this.title = title;
        this.state = state;
    }

    public Task(String title, String description, LocalDate scheduled, LocalDate deadline, State state){
        this.title = title;
        this.description = description;
        this.scheduled = scheduled;
        this.deadline = deadline;
        this.state = state;
    }

    // Getters

    public String getTitle(){
        return this.title;
    }

    public String getDescription(){
        return this.description;
    }

    public LocalDate getScheduled(){
        return this.scheduled;
    }

    public LocalDate getDeadline(){
        return this.deadline;
    }

    public State getState(){
        return this.state;
    }

    // Setters

    public void setDescription(String new_description){
        this.description = new_description;
    }

    public void setScheduled(LocalDate new_schedule){
        this.scheduled = new_schedule;
    }

    public void setState(State new_state){
        this.state = new_state;
    }

    public String toString() {
        String message = this.title + " (" + this.state + ")";
        if (scheduled != null) {
            message += " scheduled: " + scheduled;
        }
        if (deadline != null) {
            message += " deadline: " + deadline;
        }
        return message;
    }
    // Main function:
    public static void main(String[] args){
        // Check Chores work correctly on DONE -> repeat
        // note s1 is Task but object is type Chore
        Task s1 = new Chore("Test", State.TODO, LocalDate.now(), LocalDate.now().plus(Period.ofDays(7)));
        System.out.println(s1);
        s1.setState(State.DONE);
        System.out.println(s1);
        // verify the scheduled date has moved by +7 days
        Task s2 = new RepeatedTask("Task S1", State.WAIT);
        System.out.println(s2);
    }
}

class RepeatedTask extends Task{
    RepeatedTask(String title, State state){
        super(title, state);
    }

    // Check if the state is done, if so change to "TO-DO"
    public void setState(State state){
        if(state == State.DONE){
            this.state = State.TODO;
        }
        else{
            this.state = state;
        }
    }
}

class Chore extends RepeatedTask{

    private LocalDate repeat;

    Chore(String title, State state, LocalDate scheduled, LocalDate repeat){
        super(title, state);
        setScheduled(scheduled);
        setRepeat(repeat);
    }

    public void setRepeat(LocalDate repeat){
        this.repeat = repeat;
    }

    LocalDate getRepeat(){
        return this.repeat;
    }

    public void setState(State state) {
        // Invoke setState @ RepeatedTask class.
        super.setState(state);
        if (state == State.DONE) {
            LocalDate repeat_new = repeat.plus(Period.ofDays(7));
            setScheduled(repeat);
            setRepeat(repeat_new);
    }
}
}

class SharedTask extends Task{

    SharedTask(String title, String name){
        super(title, State.WAIT);
        setName(name);
    }

    private String name;

    public void setName(String name){
        this.name = name;
    }

    public String toString(){
        System.out.print(super.getTitle() + " (" + this.state + ")");
        return " shared with: " + this.name;
    }

}

class Dependency extends Task{

    Task t1;

    Dependency(String title, State state, Task t1){
        super(title, state);
        setTask(t1);
        setState(state);
    }
     
    public void setTask(Task t1){
        this.t1 = t1;
    }
    
    // Check if the dependency has a done state.
    public void setState(State state){
        if(t1.getState() != State.DONE){
            this.state = State.HALT;
        }
        else{
            this.state = State.DONE;
        }
    }

    public String toString(){
        System.out.print(super.getTitle() + " (" + this.state + ")" + " dependent on: ");
        return t1.getTitle() + " (" + t1.getState() + ")";
    }

}