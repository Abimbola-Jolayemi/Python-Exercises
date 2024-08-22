import java.util.Scanner;

public class PayrollStatement {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter employee's name: ");
        String name = input.nextLine();

        System.out.print("Enter number of hours worked in a week: ");
        double hrsWorked = input.nextDouble();

        System.out.print("Enter hourly pay rate: ");
        double hourlyPayRate = input.nextDouble();

        System.out.print("Enter federal tax withholding rate: ");
        double federalTax = input.nextDouble();

        System.out.print("Enter state tax withholding rate: ");
        double stateTax = input.nextDouble();

        double grossPay = hrsWorked * hourlyPayRate;
        double federalWithholding = (federalTax / 100) * grossPay;
        double stateWithholding = (stateTax / 100) * grossPay;
        double totalDeduction = federalWithholding + stateWithholding;
        double netPay = grossPay - totalDeduction;

        System.out.println();
        System.out.println(name);
        System.out.printf("Hours worked: %.2f\n", hrsWorked);
        System.out.printf("Pay Rate: %.2f\n", hourlyPayRate);
        System.out.printf("Gross Pay: %.2f\n", grossPay);
        System.out.println("Deductions:");
        System.out.printf("Federal Withholding: $%.2f\n", federalWithholding);
        System.out.printf("State Withholding: $%.2f\n", stateWithholding);
        System.out.printf("Total Deduction: $%.2f\n", totalDeduction);
        System.out.printf("Net Pay: $%.2f\n", netPay);
    }
}
