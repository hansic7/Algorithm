package ch05;

public class Equals_Examples {

	public static void main(String[] args) {
		
		String str_1 = "È«±æµ¿";
		String str_2 = "È«±æµ¿";
		
		if (str_1 == str_2) {
			System.out.println("°°½À´Ï´Ù");
		}else {
			System.out.println("´Ù¸¨´Ï´Ù");
		}
		
		System.out.println();
		
		String str_3 = new String("È«±æµ¿");
		String str_4 = new String("È«±æµ¿");
		
		if (str_3 == str_4) {
			System.out.println("°°½À´Ï´Ù");
		}else {
			System.out.println("´Ù¸¨´Ï´Ù");
		}

	}

}
