import java.util.Scanner;

public class Question11{
   public static void main (String []args){

	Scanner input = new Scanner (System.in);

	double totalMiles = 0;
	double totalGallons = 0;

	System.out.print("Enter miles driven: ");
	double milesDriven = input.nextDouble();

	while (milesDriven != -1){
		totalMiles += milesDriven;
		
		System.out.print("Enter gallons used: ");
		double gallonsUsed = input.nextDouble();

		totalGallons += gallonsUsed;

		double milesPerGallon = milesDriven / gallonsUsed;

		System.out.println("The miles per gallon for this tank: " + milesPerGallon);

		System.out.print("Enter miles driven: ");
		milesDriven = input.nextDouble();
	}

	double combinedMilesPerGallon = totalMiles / totalGallons;

	System.out.print("The combined miles per gallon: " + combinedMilesPerGallon);
   }

}