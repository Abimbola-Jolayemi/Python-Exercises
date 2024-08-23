import java.util.Scanner;

public class LettersAndNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter a sentence: ");
        String userInput = input.next();
        
        int countIntegers = 0;
        int countLetters = 0;
        
        for (char character : userInput.toCharArray()) {
            if (Character.isDigit(character)) {
                countIntegers++;
            } else if (Character.isLetter(character)) {
                countLetters++;
            }
        }
        
        System.out.println("Letters: " + countLetters);
        System.out.println("Numbers: " + countIntegers);
    }
}