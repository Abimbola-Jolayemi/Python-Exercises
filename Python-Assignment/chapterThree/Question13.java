import java.util.Scanner;

public class Question13{
   public static void main(String []args){

	Scanner input = new Scanner (System.in);

	int factorial = 1;

	System.out.print("Enter any number: ");
	int number = input.nextInt();

	for(int index = 0; index < number; index++){
		factorial = factorial * (number - index);
	}

	System.out.print("The factorial is: " + factorial);
   }
}