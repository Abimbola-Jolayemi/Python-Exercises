public class SavingsAccount {

    public static double calculateInitialDeposit(double finalAccountValue, double monthlyInterestRate, int years) {
        double annualInterestRate = (monthlyInterestRate / 100) / 12;
        int noOfMonths = years * 12;
        double initialDepositAmount = finalAccountValue / Math.pow(1 + annualInterestRate, noOfMonths);
        return initialDepositAmount;
    }

    public static void main(String[] args) {
        double finalAccountValue = 10000;
        double monthlyInterestRate = 5;
        int years = 10;

        double initialDepositAmount = calculateInitialDeposit(finalAccountValue, monthlyInterestRate, years);
        System.out.printf("The initial deposit amount is: %.2f%n", initialDepositAmount);
    }
}
