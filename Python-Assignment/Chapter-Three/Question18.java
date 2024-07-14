public class Question18{
   public static void main(String []args){

	for(int outerLoop = 0; outerLoop < 10; outerLoop++){
		for(int innerLoop = 0; innerLoop < outerLoop+1; innerLoop++){
			System.out.print("*");
		}
		for(int spaceLoop = 0; spaceLoop < (10-outerLoop+1); spaceLoop++){
			System.out.print(" ");
}
		System.out.print("   ");


		for(int innerLoop = 0; innerLoop < 10-outerLoop; innerLoop++){
			System.out.print("*");
		}
		for(int spaceLoop = 0; spaceLoop < outerLoop; spaceLoop++){
			System.out.print(" ");
}
		System.out.print("   ");


		for(int spaceLoop = 0; spaceLoop < outerLoop; spaceLoop++){
			System.out.print(" ");
		}
		for(int innerLoop = 0; innerLoop < (10-outerLoop); innerLoop++){
			System.out.print("*");
}
		System.out.print("   ");


		for(int spaceLoop = 0; spaceLoop < (10-outerLoop-1); spaceLoop++){
			System.out.print(" ");
		}
		for(int innerLoop = 0; innerLoop < (outerLoop+1); innerLoop++){
			System.out.print("*");
}
		System.out.print("   ");

	System.out.println();

	}
}

}