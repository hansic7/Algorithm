package ch04.sec03;


public class SwitchExample {

	public static void main(String[] args) {
		char grade = 'b';
		
		switch (grade) {
		case 'a':
		case 'A':
			System.out.println("우수회원");
			break;
//		case 'B':
		case 'B':
			System.out.println("그냥회원");
			break;
		default:
			System.out.println("ㅇ");
			break;
		}
		
	}

}
