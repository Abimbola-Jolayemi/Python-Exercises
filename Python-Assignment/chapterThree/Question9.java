import java.util.Scanner;

public class Question9{
   public static void main(String []args){

	Scanner input = new Scanner(System.in);

	System.out.print("Enter a five-digit integer: ");
	int number = input.nextInt();

	for(int index = 0; index < 5; index++){
		int digit = number % 10;
		number = number / 10;

		System.out.print(digit + " ");
	}
   }
}