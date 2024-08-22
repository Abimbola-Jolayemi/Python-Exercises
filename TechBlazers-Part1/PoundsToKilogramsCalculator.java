public class PoundsToKilogramsCalculator {

    public static double poundsToKilograms(double pounds) {
        double kilograms = pounds * 0.454;
        return kilograms;
    }

    public static void main(String[] args) {
        double pounds = 150;
        double kilograms = poundsToKilograms(pounds);
        System.out.printf("%.2f pounds is %.2f kilograms.%n", pounds, kilograms);
    }
}
