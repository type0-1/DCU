public class Point implements Comparable{
    private double x, y;

    public Point(double newX, double newY) {
        this.x = newX;
        this.y = newY;
    }

    public double getX(){
        return this.x;
    }

    public double getY(){
        return this.y;
    }

    public void setX(double newX){
        this.x = newX;
    }

    public void setY(double newY){
        this.y = newY;
    }

    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }

    @Override 
    public boolean lessThan(Order other){
        Point newer = (Point) other;
        if(this.x < newer.getX() || this.y < newer.getY()){
            return true;
        }
        if(this.equals(newer)){
            return false;
        }
        return false;
    }

    public int compareTo(Object arg){
        Point newer = (Point) arg;
        if(this.x < newer.getX() || this.y < newer.getY()){
            return -1;
        }
        else if (this.equals(newer)){
            return 0;
        }
        return 1;
    }

    public static void main(String[] args){
    }
}