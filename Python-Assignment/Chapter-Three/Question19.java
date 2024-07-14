public class Question19{
   public static void main (String []args){

	int maxNumber = 20;

	for(int side1 = 1; side1 <= maxNumber; side1++){
		for(int side2 = side1; side2 <= maxNumber; side2++){
			for(int side3 = side2; side3 <= maxNumber; side3++){
				if(Math.pow(side1, 2) + Math.pow(side2, 2) == Math.pow(side3, 2))
				System.out.printf("%d%s%d%s%d%n", side1, ", ", side2, ", ", side3);
				
			}
		}
	}
   }
}