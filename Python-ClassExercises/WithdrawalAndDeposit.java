import java.util.Scanner;

public class WithdrawalAndDeposit{
   public static void main (String []args){

	Scanner input = new Scanner(System.in);

	int accountBalance = 0;

	System.out.println("Welcome to Comfort to Comfort Bank!!!");
	System.out.println("Enter name :");
	String name = input.next().toUpperCase();
	System.out.println("Hi " + name + "!!!");

	while(true){
		System.out.printf("%s%n%s%n%s%n", "1. Deposit", "2. Withdrawal", "0. Exit");
	System.out.print("Enter an option to proceed: ");
	int decision = input.nextInt();
		if(decision == 0){
		   break;
		}

		else if (decision == 1){
			System.out.print("Enter amount to be deposited: ");
			int deposit = input.nextInt();

			accountBalance += deposit;
			System.out.println(accountBalance);
		}

		else if (decision == 2){
			System.out.print("Enter amount to be withdrawn: ");
			int withdrawal = input.nextInt();

			if (withdrawal <= accountBalance){
				accountBalance -= withdrawal;
				System.out.println(accountBalance);
			}
			else{
				System.out.println("Insufficient fund!!!");
			}		
		}

		else{

			System.out.println("Invalid input!!!. Kinldy select 1 to deposit, 2 to withdrawal or 0 to exit");
		}

	}


	System.out.print(name + "!!!. Your account balance is: " + accountBalance);
	
   }
}