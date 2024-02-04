class X {
    int num = 1;
    int getNum() {
        return num;
    }
}
class Y extends X {
    // int num = 1; is inherited from X
    // int getNum() is inherited from X
    @Override
    int getNum(){
        // custom implmentation that overrides X.getnum()
        // to be able to still call X.getNum(), you must call super()
        return super.getNum();
    }
}

public class Notes {
    public static void main(String[] args){

    }
}
