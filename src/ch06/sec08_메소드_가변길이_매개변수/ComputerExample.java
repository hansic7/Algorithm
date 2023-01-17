package ch06.sec08_메소드_가변길이_매개변수;

public class ComputerExample {

	public static void main(String[] args) {
	
	Computer myCom = new Computer();
		
	int result_1 = myCom.sum(1,2,3);
	System.out.println("result_1 : " + result_1);

	int result_2 = myCom.sum(1,2,3,4,5);
	System.out.println("result_1 : " + result_2);

	// int ... value 로 받으면 배열이 '새로' 생성됨
	
	int[] a = {1,2,3,4,5}; 
	int result_3 = myCom.sum(a);
	System.out.println("result_1 : " + result_3);
	
	int result_4 = myCom.sum(new int[] {1,2,3,4,5});
	System.out.println("result_1 : " + result_4);

	}
}
