public class ReversedPattern{
   public static void main(String []args){

	for (int outerLoop = 5; outerLoop > 0; outerLoop--){
		for(int innerLoop = outerLoop; innerLoop > 0; innerLoop--){
			System.out.print(innerLoop + " ");
		}
		System.out.println();
	}
   }
}