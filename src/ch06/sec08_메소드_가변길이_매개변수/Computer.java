package ch06.sec08_메소드_가변길이_매개변수;

public class Computer {
	
	//parameter을 int[]로 받으면 '원래' 배열밖에 못 받음 
	//int ... value은 숫자든 배열이든 받아서 배열로 다시 만듬 
	int sum(int ... value) {
		int sum = 0;
		
		
		//value���� �迭ó�� ���
		for (int i : value) {
			sum += i;
		}
		
		
		return sum;
	}	
}
