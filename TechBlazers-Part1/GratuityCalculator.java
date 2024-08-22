public class GratuityCalculator {
    public static double[] calculateGratuityAndTotal(double subtotal, double gratuityRate) {
        double gratuity = (gratuityRate / 100) * subtotal;
        double total = gratuity + subtotal;
        return new double[]{gratuity, total};
    }

    public static void main(String[] args) {
        double subtotal = 10.0;
        double gratuityRate = 15.0;
        double[] results = calculateGratuityAndTotal(subtotal, gratuityRate);
        System.out.printf("Gratuity: %.2f\nTotal: %.2f\n", results[0], results[1]);
    }
}