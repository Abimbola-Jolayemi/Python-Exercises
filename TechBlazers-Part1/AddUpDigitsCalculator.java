public class AddUpDigits {

    public static void main(String[] args) {
        int number = 932;
        System.out.println(addUpDigits(number));
    }

    public static int addUpDigits(int number) {
        int total = 0;
        while (number > 0) {
            int digit = number % 10;
            total += digit;
            number = number / 10;
        }
        return total;
    }
}
