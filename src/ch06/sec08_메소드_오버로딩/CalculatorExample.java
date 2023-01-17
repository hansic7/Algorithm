package ch06.sec08_메소드_오버로딩;

public class CalculatorExample {

	public static void main(String[] args) {
		
		Calculator myCalc = new Calculator();

		System.out.println(myCalc.areaREctangle(10));
		System.out.println(myCalc.areaREctangle(10,20));

		
		System.out.println(Calculator.aaa);
	}

}
