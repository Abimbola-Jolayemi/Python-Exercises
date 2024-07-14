public class Question7{
   public static void main(String []args){

	System.out.printf("%10s%10s%10s%n", "Number", "Square", "Cube");

	for (int index = 0; index <= 5; index++){
		int indexSquared = index * index;
		int indexCubed = index * index * index;

		System.out.printf("%10d%10d%10d%n", index, indexSquared, indexCubed);
	}
   }
}