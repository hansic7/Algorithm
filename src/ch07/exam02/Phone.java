package ch07.exam02;

public class Phone {
	
	String model;
	String color;
	
	Phone(String model, String color){
		this.model = model;
		this.color = color;
		System.out.println("Phone() 생성자 실행");
	}
}
