import java.util.Scanner;

public class MortgageCalculator{
   public static void main(String []args){

	Scanner input = new Scanner (System.in);

	System.out.print("Enter Principal Amount: ");
	double principal = input.nextDouble();

	System.out.print("Enter number of years: ");
	double noOfYears = input.nextDouble();

	System.out.print("Enter Annual rate: ");
	double annualRate = input.nextDouble();

	double duration = noOfYears * 12;

	double monthlyRate = annualRate / 12;

	double percentageMonthlyRate = monthlyRate / 100;

	double percentageMonthlyRateRaisedToPowerDuration = Math.pow((1+percentageMonthlyRate), duration);

	double numerator = percentageMonthlyRate * percentageMonthlyRateRaisedToPowerDuration;

	double denominator = percentageMonthlyRateRaisedToPowerDuration - 1;

	double monthlyPayment = principal * (numerator / denominator);

	System.out.printf("The Monthly payment is: %.2f", monthlyPayment);
   }
}