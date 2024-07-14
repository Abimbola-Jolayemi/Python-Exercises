import java.util.Scanner;

public class Question1{
   public static void main(String []args){

	Scanner input = new Scanner(System.in);

	int passes = 0;
	int failures = 0;

	for(int students = 1; students <= 10; students++){
		System.out.print("Enter a score (1 = pass and 2 = fail): ");
		int score = input.nextInt();

		if (score == 1)
			passes = passes + 1;
		else if(score == 2)
			failures = failures + 1;
		else
			continue; 
	}

		System.out.println("The number of student that passed: " + passes);
		System.out.println("The number of student that failed: " + failures);

	if (passes >= 8)
		System.out.print("Great Job!!! Bonus to the instructor");
   }

}