package ch05;

public class Equals_Examples {

	public static void main(String[] args) {
		
		String str_1 = "ȫ�浿";
		String str_2 = "ȫ�浿";
		
		if (str_1 == str_2) {
			System.out.println("�����ϴ�");
		}else {
			System.out.println("�ٸ��ϴ�");
		}
		
		System.out.println();
		
		String str_3 = new String("ȫ�浿");
		String str_4 = new String("ȫ�浿");
		
		if (str_3 == str_4) {
			System.out.println("�����ϴ�");
		}else {
			System.out.println("�ٸ��ϴ�");
		}

	}

}
