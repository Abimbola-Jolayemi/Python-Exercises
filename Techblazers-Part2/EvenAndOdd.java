public class EvenAndOdd{
  	
	public static void main(String []args){
		System.out.print(displayNumberState(399));
	}

 public static String displayNumberState(int number){
	if (number % 2 == 0){
		return "It is an even number";
	} else {
		return "It is an odd number";
	}
   }
}