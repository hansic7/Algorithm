package ch05;

public class 다차원배열 {

	public static void main(String[] args) {
		//2李⑥�� 諛곗�� ����
		int [][] score = {
				{80, 90 , 96},
				{76, 88}
		};
		
		//諛곗�댁�� 湲몄��
		System.out.println("泥ル�吏� 諛� ���� �� : " + score[0].length);
		System.out.println("��踰�吏� 諛� ���� �� : " + score[1].length);
		System.out.println();
		
		//��洹� 援ы��湲�
		int sum = 0;
		for (int i : score[0]) {
			sum += i;
		}
		double avarage = (double)sum / score[0].length;
		System.out.println("�닿� 1諛� ��洹�: " + avarage);
		
		
		//��泥� 諛� ��
		System.out.println(score.length);
	}

}
