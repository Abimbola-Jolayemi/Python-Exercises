import java.util.Scanner;

public class Question8{
   public static void main(String []args){

	Scanner input = new Scanner(System.in);

	double minNumber = Double.POSITIVE_INFINITY;
	int maxNumber = 0;
	int total = 0;
	int count = 0;

	for (int index = 0; index < 4; index++){
		System.out.print("Enter a number: ");
		int number = input.nextInt();

		if (number < minNumber){
			minNumber = number;
		} 
		if (number > maxNumber){
			maxNumber = number;
		}
		total = total + number;
		count++;

	}

	int average = total / count;

	System.out.println("The sum of all number is: " + total);
	System.out.println("The average is: " + average);
	System.out.println("The minimum number is: " + minNumber);
	System.out.println("The maximum number is: " + maxNumber);
   }
}