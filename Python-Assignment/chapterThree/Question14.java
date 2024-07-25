
public class Question14{
   public static void main(String []args){

	double pi = 0;
	int noOfTerms = 0;
	double terms;

	System.out.printf("%-10s%10s%n", "Terms", "Accomodation");

	for(int index = 0; index <= 400; index++){
		if(index % 2 == 0){
			terms = (4.0 * 1) / (2 * index + 1);
		}
		else{
			terms = (4.0 * -1) / (2 * index + 1);
		}

		pi = pi + terms;
		noOfTerms += 1;

		System.out.printf("%-10d%10f%n", noOfTerms,  pi);

	}
   }

}