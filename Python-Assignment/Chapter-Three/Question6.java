import java.util.Scanner;

public class Question6{
   public static void main(String []args){

	Scanner input = new Scanner (System.in);

	System.out.println("What is your problem?: ");
	String problem = input.nextLine();

	System.out.println("Have you had this problem before? (Yes or No): ");
	String response = input.nextLine();

	switch (response){
		case "Yes":
			System.out.print("Well, you have it again!!!");
		break;
		case "No":
			System.out.print("Well, you have it now!!!");
		break;
		default:
			System.out.print("Kindly select a valid option next time");
	}
   }
}