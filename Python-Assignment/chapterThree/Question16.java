import java.util.Scanner;

public class Question16{
   public static void main(String []args){

	Scanner input = new Scanner(System.in);

	int largest = 0;
 	int secondLargest = 0;

	System.out.println("Enter a number: ");

	for (int index = 0; index < 10; index++){

		int number = input.nextInt();

		if(number > largest){
			secondLargest = largest;
			largest = number;
		} else if (number > secondLargest && number != largest){
			secondLargest = number;
		}
	}

	System.out.println("The largest number is: " + largest);
	System.out.println("The second largest number is: " + secondLargest);
   }

}