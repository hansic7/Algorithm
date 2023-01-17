package ch06.sec07_생성자_오버로딩;

public class Car {
	
	String model;
	String color;
	int maxSpeed;
	
	public Car(String model, String color, int maxSpeed){
		this.model = model;
		this.color = color;
		this.maxSpeed = maxSpeed;
		System.out.println("1번으로 돌아옵니다");
	};
	
	public Car(String model, String color){
		this(model, color, 300);
		System.out.println("2번으로 돌아옵니다");
	};
	
	public Car(String model){
		this(model, "?곗??", 300);
		System.out.println("3번으로 돌아옵니다");
	};
	
	public Car() {
		this("洹몃????", "?곗??", 300);
		System.out.println("4번으로 돌아옵니다");
	}

	

	
	
	
	
}
