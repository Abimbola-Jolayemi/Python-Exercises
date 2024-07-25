import java.util.Scanner;

public class Question5{
   public static void main (String []args){

	Scanner input = new Scanner (System.in);

	System.out.println("Enter two integers and I will give you the relationships between them");
	System.out.println("Integer 1: ");
	int number1 = input.nextInt();

	System.out.println("Integer 2: ");
	int number2 = input.nextInt();

	if (number1 == number2)
		System.out.println(number1 + " is equal to " + number2);
	else
		System.out.println(number1 + " is not equal to " + number2);

	if (number1 > number2)
		System.out.println(number1 + " is greater than " + number2);
	else
		System.out.println(number1 + " is not not greater than " + number2);

	if (number1 < number2)
		System.out.println(number1 + " is less than " + number2);
	else
		System.out.println(number1 + " is not less than " + number2);
   }
}