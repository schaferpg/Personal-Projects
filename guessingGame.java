import java.util.*;
public class guessingGame {
    private ArrayList<Integer> list = new ArrayList<Integer>();
    private int size; // Value of length of array
    private int randAnswer; // Random answer between the
    Scanner keyboard = new Scanner(System.in);

    public guessingGame() {

    }
    public String greeting() {
        System.out.println("Hello, would you like to play a guessing game? Please respond yes or no.");
        String response = keyboard.nextLine();
        return(response);
    }
    public int displyGameInformation() {
        // Explains the guessing game
        System.out.println("The game asks to pick a number to set the bounds for the game 0 to whatever number you want");
        System.out.println("What number would you like to select?");
        this.size = keyboard.nextInt();
        String temp = keyboard.nextLine();

        return(this.size);
    }
    public void createArrayList() {
        for (int i = 0; i<this.size+1; i++) {
            this.list.add(i);
        }
    }
    public int solver() {
        return(0);
    }
    public int randomNumGen() {

        Random random = new Random(); // Creates instance of Random object
        this.randAnswer = random.nextInt(this.size); // random array between 0 and size
        return(this.randAnswer);
    }
    public String playAgain() {
        System.out.println("Would you like to play again? Please respond yes or no.");
        String answer = keyboard.nextLine();
        return(answer);
    }
}

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Initialize Scanner object
        Scanner keyboard = new Scanner(System.in);
        guessingGame myGame = new guessingGame();
        String response =  myGame.greeting();           // gets user's response as well as greets user
        while (response.equals("yes")) {
            myGame.displyGameInformation();         // displays game information and asks user to pick a number
            myGame.createArrayList(); // Creates array list of numbers between 0 and the num they picked
            int answer = myGame.randomNumGen(); // Picks a random number between 0 and number user inputted
            int guess = -1;

            while (guess != answer) {
                System.out.println("What is your guess?");
                guess = keyboard.nextInt();
                String temp = keyboard.nextLine(); // eats space after nextLine
                if (guess < answer) {
                    System.out.println("Guess higher");
                }
                if (guess > answer) {
                    System.out.println("Guess Lower");
                }
            }
            System.out.println("You got it!");
            response = myGame.playAgain();                     // ask user if they want to play again
        }
    }
}
