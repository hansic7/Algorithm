package ch06.sec08_메소드_오버로딩;

public class Calculator {

	double areaREctangle(double with){
		double area = with * with;
		return area;
	};
	
	double areaREctangle(double with,double with_2){
		double area = with * with_2;
		return area;
	};
	
	public static int aaa = 20;
}
