package ch04.sec03;


public class SwitchExample {

	public static void main(String[] args) {
		char grade = 'b';
		
		switch (grade) {
		case 'a':
		case 'A':
			System.out.println("���ȸ��");
			break;
//		case 'B':
		case 'B':
			System.out.println("�׳�ȸ��");
			break;
		default:
			System.out.println("��");
			break;
		}
		
	}

}
