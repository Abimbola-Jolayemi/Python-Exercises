import java.util.Scanner;

public class DivisiblesOf5And6 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        int number = input.nextInt();

        boolean divisibleByBoth = (number % 5 == 0) && (number % 6 == 0);
        System.out.printf("Is %d divisible by 5 and 6? %b\n", number, divisibleByBoth);

        boolean divisibleByEither = (number % 5 == 0) || (number % 6 == 0);
        System.out.printf("Is %d divisible by 5 or 6? %b\n", number, divisibleByEither);

        boolean divisibleByOneNotBoth = (number % 5 == 0 && number % 6 != 0) || (number % 5 != 0 && number % 6 == 0);
        System.out.printf("Is %d divisible by 5 or 6, but not both? %b\n", number, divisibleByOneNotBoth);
    }
}
