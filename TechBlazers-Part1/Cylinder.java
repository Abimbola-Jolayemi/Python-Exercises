import java.util.Scanner;

public class Cylinder{

    public static void main(String[] args) {

	Scanner input = new Scanner(System.in);
        
	System.out.println("Enter radius of circle: ");
	double radius = input.nextDouble();

	System.out.println("Enter length of circle: ");
	double length = input.nextDouble();

	CylinderFunction cylinder = new CylinderFunction(radius, length);

	System.out.printf("Area of the cylinder: %.2f\n", cylinder.computeArea());
        System.out.printf("Volume of the cylinder: %.2f\n", cylinder.computeVolume());
    }
}
