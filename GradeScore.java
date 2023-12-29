public class gradeScore {
    private int grade;

    public gradeScore(int grade) {
        this.grade = grade;
    }
    public String Score(int num) {
        if (this.grade >= 90) {
            return "A";
        }
        else if (this.grade >= 80) {
            return "B";
        }
        else if (this.grade >= 70) {
            return "C";
        }
        else if (this.grade >= 60) {
            return "D";
        }
        else {
            return "F";
        }
    }
}
public class Main {
    public static void main(String[] args) {
        // intialize testing of array
        int[] grades = {90, 50, 84, 35};
        // for loop with size of array
        for (int i = 0; i < grades.length; i++) {
            // Creating a new GradeScore object with the "new" keyword
            gradeScore grade = new gradeScore(grades[i]);
            System.out.println(grade.Score(grades[i]));
        }
    }
}
