public class SumOfString{
	
	public static void main(String []args){
		String numbers = "123";

		System.out.print(addNumbers(numbers));
	}


	public static String addNumbers(String numbers) {
    		int total = 0;
    
    		for (char character : numbers.toCharArray()) {
            		   total += Character.getNumericValue(character);
    		}

    		return String.valueOf(total);
	}
}