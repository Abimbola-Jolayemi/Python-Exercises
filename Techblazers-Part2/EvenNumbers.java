import java.util.ArrayList;

public class EvenNumbers{
   public static void main(String []args){

	ArrayList <Integer> evenNumbers = new ArrayList <>();

	for(int number = 1000; number <= 3000; number++){
		boolean isEven = true;
		int tempNumber = number;
		while(tempNumber != 0){
			int digit = tempNumber % 10;
			tempNumber = tempNumber / 10;

			if(digit % 2 != 0){
				isEven = false;
				break;
			}
		}
		
		if(isEven){
			evenNumbers.add(number);
		}
	}

	System.out.print(evenNumbers);
   }
}