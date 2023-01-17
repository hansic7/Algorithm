package ch02;

public class OperationpromotionExample_연산식 {
	public static void main(String[] args) {
		
		// byte < short, char < int < long < float < double
		
		byte result1 = 10 + 20;   //컴파일 단계에서 연산
		System.out.println("result1: " + result1);
		
		byte v1 = 10;
		byte v2 = 20;
		int result2 = v1 + v2;     ///실행 단계에서 연산 되기때문에 int로 변환후 연산됨
		System.out.println("result2: " + result2);
	}

}
