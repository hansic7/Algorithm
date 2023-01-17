package ch05;

public class Stirng에서_문자추출 {

	public static void main(String[] args) {
		String ssn = new String("950124435");
		
		char sex = ssn.charAt(6);
		switch(sex) {
		case '1':
		case '3':
			System.out.println("남자입니다");
			break;
		case '2':
		case '4':
			System.out.println("여자입니다");
//			break;
		
		}
		

	}

}
