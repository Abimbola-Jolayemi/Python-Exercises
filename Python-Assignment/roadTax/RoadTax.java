import java.util.Scanner;

public class RoadTax{
   public static void main (String []args){

	Scanner input = new Scanner (System.in);

	System.out.print("Enter the price of your car: ");
	int priceOfCar = input.nextInt();

	double roadTax = 0;

	if (priceOfCar <= 1000000){
		roadTax = (10.0 / 100) * priceOfCar;
	}
	else if (priceOfCar > 1000000 && priceOfCar <= 3000000){
		roadTax = (15.0 / 100) * priceOfCar;
	}
	else if (priceOfCar > 3000000 && priceOfCar <= 5000000){
		roadTax = (20.0 / 100) * priceOfCar;
	}
	else if (priceOfCar > 5000000){
		roadTax = (25.0 / 100) * priceOfCar;
	}

	System.out.printf("The road tax is: %.2f", roadTax);
   }
}