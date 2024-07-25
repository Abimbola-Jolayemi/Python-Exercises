public class Question15{
   public static void main (String []args){

	double e = 0.00;

	for (int term = 0; term <= 10; term++){
		int factorial = 1;

		for (int index = 1; index < term; index++){
			factorial *= (term - index);
		}

		e += 1.0 / factorial;
	}

	System.out.print("The estimated value of constant e using 10 terms is: " + e);
   }
}