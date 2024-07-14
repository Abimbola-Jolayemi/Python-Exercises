import java.util.Scanner;

public class Multiplication{
   public static void main(String []args){

	Scanner input = new Scanner (System.in);

	System.out.print("Enter a number: ");
	int number = input.nextInt();

	for(int index = 1; index <= 12; index++){
		int product = number * index;

		System.out.println(number + " * " + index + " = " + product); 
	}
   }

}