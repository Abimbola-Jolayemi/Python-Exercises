public class NumbersInIncreasingOrder {
    public static void main(String[] args) {
        int num1 = 2, num2 = 5, num3 = 1;
        int[] result = numInIncreasingOrder(num1, num2, num3);

        System.out.println("Numbers in increasing order: " + result[0] + ", " + result[1] + ", " + result[2]);
    }

    public static int[] numInIncreasingOrder(int num1, int num2, int num3) {
        if (num1 > num2) {
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }
        if (num1 > num3) {
            int temp = num1;
            num1 = num3;
            num3 = temp;
        }
        if (num2 > num3) {
            int temp = num2;
            num2 = num3;
            num3 = temp;
        }
        return new int[]{num1, num2, num3};
    }
}
