public class Table {

    public static void printTable() {
        System.out.printf("%-5s%-5s%s%n", "a", "b", "a**b");

        for (int number = 1; number <= 5; number++) {
            int num = number + 1;
            int exponents = (int) Math.pow(number, num);
            System.out.printf("%-5d%-5d%d%n", number, num, exponents);
        }
    }

    public static void main(String[] args) {
        printTable();
    }
}
