import java.util.Scanner;

public class PassScore{
   public static void main(String []args){

	Scanner input = new Scanner(System.in);

	int passes = 0;
	int failures = 0;

	for(int index = 1; index <= 15; index++){
		System.out.print("Enter a score: ");
		int score = input.nextInt();

		if (score >= 45)
			passes++;
		else
			failures++;
	}

	System.out.println(passes + " students passed the examination");
	System.out.println(failures + " students failed the examination");
   }
}