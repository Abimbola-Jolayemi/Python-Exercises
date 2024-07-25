import java.util.Scanner;

public class Question12{
   public static void main (String []args){

	Scanner input = new Scanner (System.in);


	System.out.print("Enter any five-digits number: ");
	int number = input.nextInt();

	int digit1 = number % 10;
	number = number / 10;

	int digit2 = number % 10;
	number = number / 10;
	
	int digit3 = number % 10;
	number = number / 10;

	int digit4 = number % 10;
	number = number / 10;

	int digit5 = number % 10;

	if (digit1 == digit5 && digit2 == digit4)
		System.out.print("Number is a palindrome");
	else
		System.out.print("Number is not a palindrome");
   }

}