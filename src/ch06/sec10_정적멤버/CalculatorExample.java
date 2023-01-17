package ch06.sec10_정적멤버;

public class CalculatorExample {

	public static void main(String[] args) {
		
		
		//따로 만든 객체(인스턴스)를 타고 들어가는 것 X
		//걍 클래스에서 타고 들감
		System.out.println(Calculator.pi);
		System.out.println(Calculator.minus(5, 6));
		System.out.println(Calculator.plus(5, 6));
	}

}
