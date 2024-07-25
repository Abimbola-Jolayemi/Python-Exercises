import java.util.Scanner;

public class Question10{
   public static void main(String []args){

	Scanner input = new Scanner (System.in);

	System.out.print("Enter investment amount: ");
	int investmentAmount = input.nextInt();

	System.out.print("Enter annual return rate: ");
	int annualReturnRate = input.nextInt();

	double percentageAnnualReturn = annualReturnRate / 100.0;

	double percentageAnnualReturnPlusOne = 1 + percentageAnnualReturn;

	for (int noOfYrs = 1; noOfYrs <= 30; noOfYrs++){
		double percentageAnnualReturnRaisedToPowerNoOfYrs = Math.pow(percentageAnnualReturnPlusOne, noOfYrs);

		double result = investmentAmount * percentageAnnualReturnRaisedToPowerNoOfYrs;

		System.out.printf("The investment amount after %d years: %.2f%n", noOfYrs, result);
	}
}

}