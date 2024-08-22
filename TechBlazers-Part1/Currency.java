import java.util.Scanner;

public class Currency{

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter 0 (USD to naira) or 1 (naira to USD): ");
        int conversionChoice = input.nextInt();

        System.out.print("Enter amount to be converted: ");
        int amount = input.nextInt();

        if (conversionChoice == 0) {
            System.out.printf("Amount in naira: #%d\n", amount * 1500);
        } else if (conversionChoice == 1) {
            System.out.printf("Amount in Dollars: $%d\n", amount / 1500);
        } else {
            System.out.println("Enter a valid input!!!");
        }
    }
}