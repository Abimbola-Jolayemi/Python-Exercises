import java.util.Scanner;

public class FeetToMetersConverter {
    public static void main(String[] args) {
   	Scanner input = new Scanner (System.in);

	System.out.print("Enter a value to be converted to meters: ");
        double feet = input.nextDouble();
        double meters = convertFeetToMeters(feet);
        System.out.printf("%.2f feet is equal to %.2f meters.\n", feet, meters);
    }

	public static double convertFeetToMeters(double feet) {
        double meters = feet * 0.305;
        return meters;
    }
}
