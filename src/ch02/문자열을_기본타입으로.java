package ch02;

public class 문자열을_기본타입으로 {
	public static void main(String[] args) {
	
	/// parse == 구문을 분석하다"
	
	int value1 = Integer.parseInt("100");
	double value2 = Double.parseDouble("23.241");
	boolean value3 = Boolean.parseBoolean("true");
	
	System.out.println("value1: " + value1);
	System.out.println("value2: " + value2);
	System.out.println("value3: " + value3);
	System.out.println();
	
	String str1 = String.valueOf(value1);
	System.out.println("str1: " + str1);
	
	
	
	}
}
