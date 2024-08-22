import java.util.Scanner;
import java.util.Random;

public class Lottery {
    public static void main(String[] args) {
        Random random = new Random();
        int lotteryNumber = random.nextInt(900) + 100;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a three-digit number: ");
        int usersInput = scanner.nextInt();

        int lotteryDigit1 = lotteryNumber % 10;
        lotteryNumber /= 10;

        int lotteryDigit2 = lotteryNumber % 10;
        lotteryNumber /= 10;

        int lotteryDigit3 = lotteryNumber;

        int usersDigit1 = usersInput % 10;
        usersInput /= 10;

        int usersDigit2 = usersInput % 10;
        usersInput /= 10;

        int usersDigit3 = usersInput;

        if (usersDigit3 == lotteryDigit3 && usersDigit2 == lotteryDigit2 && usersDigit1 == lotteryDigit1) {
            System.out.println("Your award is $10,000");
        } else if ((usersDigit3 == lotteryDigit3 || usersDigit2 == lotteryDigit2 || usersDigit1 == lotteryDigit1) &&
                   (usersDigit2 == lotteryDigit1 || usersDigit2 == lotteryDigit2 || usersDigit2 == lotteryDigit3) &&
                   (usersDigit3 == lotteryDigit1 || usersDigit3 == lotteryDigit2 || usersDigit3 == lotteryDigit3)) {
            System.out.println("Your award is $3,000");
        } else if ((usersDigit3 == lotteryDigit3 || usersDigit2 == lotteryDigit2 || usersDigit1 == lotteryDigit1) ||
                   (usersDigit2 == lotteryDigit1 || usersDigit2 == lotteryDigit2 || usersDigit2 == lotteryDigit3) ||
                   (usersDigit3 == lotteryDigit1 || usersDigit3 == lotteryDigit2 || usersDigit3 == lotteryDigit3)) {
            System.out.println("Your input matches one digit in the lottery number, your award is $0");
        } else {
            System.out.println("Sorry!!!, your input does not match the lottery number. Try again next time.");
        }
    }
}
