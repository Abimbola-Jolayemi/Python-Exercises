import java.util.Scanner;

public class Question20{
   public static void main(String []args){

	Scanner input = new Scanner(System.in);

	System.out.print("Enter any binary number: ");
	int binaryNumber = input.nextInt();

	int decimal = 0;
	int count = 1;

	while(binaryNumber > 0){
		int digit = binaryNumber % 10;

		decimal = decimal + digit * count;

		count = count * 2;

		binaryNumber = binaryNumber / 10;
	}

	System.out.print(decimal);
  }
}