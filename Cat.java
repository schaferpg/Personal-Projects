public class Cat {
    // Private instance variables, encapsulating the state of the Cat Object
    private String name;
    private int age;
    private String color;
    private String mood;

    public void purr() {
        System.out.println("Cat purrs");
    }
    /*
    public Cat(String color, String mood) {
        // The "this keyword refers to the current instance of the class
        this.color = color;
        this.mood = mood;
    }
     */

    // Public method to access the private color field
    public String getColor() {
        return color;
    }
    // Public method ot access the private mood field
    public String getMood() {
        return mood;
    }
    // Private method, only accessible within this class
    private void changeMood(String newMood) {
        mood = newMood;
    }
    // Public method to interact with the private changeMood
    public void makeHappy() {
        changeMood("happy");
        purr(); // The cat purrs when made happy
    }
    public Cat(String name, int age) {
        this.name = name;
        this.age = age;
    }
    // Public getter for the name, allowing read access ot the private variable
    public String getName() {
        return this.name;
    }
    //Public setter for the name allowing write access to the private variable
    public void setName(String name) {
        this.name = name;
    }
    // Public getter for the age, allowing read access to the private variable
    public int getAge() {
        return this.age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void dispalyInfo() {
        System.out.println(this.name + " is " + this.age + " year(s) old.");
    }

}
public class Main {
    public static void main(String[] args) {
        // Creating a new Cat object with the "new" keyword
        Cat myCat = new Cat("Zeta", 7);

        // accessing the public methods of the Cat class
        myCat.dispalyInfo();
        myCat.setAge(12);
        myCat.setName("Pippa");
        myCat.dispalyInfo();
    }
}
