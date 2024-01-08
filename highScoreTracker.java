public class highScoreTracker {
    // Tracks the score for a basketball game
    private int threePointers;
    private int twoPointers;
    // Tracks free throws
    private int freeThrows;
    private int score; // Keeps track of score

    public highScoreTracker() {
    }
    public void threePointers(int amount) {
        score += amount*3;
        this.threePointers = threePointers;
    }
    public void twoPointer(int amount) {
        score += amount*2;
    }
    public void freeThrows(int amount) {
        score += amount;
    }
    public void displayInformation(String name) {
        System.out.println(name + " scored: " + score);
    }
}


import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Initialize Scanner object
        Scanner keyboard = new Scanner(System.in);
        // Get team name
        System.out.println("What is the team name?");
        String name = keyboard.nextLine();
        // Get information of number of three points
        System.out.println("How many three pointers did " + name + " make?");
        int threePointers = keyboard.nextInt();
        // Get number of two pointers made by team
        System.out.println("How many two pointers did " + name + "make?");
        int twoPointers = keyboard.nextInt();
        // Get number of free throws made by team
        System.out.println("How many free throws did " + name + " make?");
        int freeThrows = keyboard.nextInt();
        highScoreTracker tracker = new highScoreTracker();
        tracker.threePointers(threePointers);
        tracker.twoPointer(twoPointers);
        tracker.freeThrows(freeThrows);
        tracker.displayInformation(name);
    }
}
