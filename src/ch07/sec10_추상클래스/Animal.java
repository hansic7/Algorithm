package ch07.sec10_추상클래스;

public abstract class Animal {
	
	//메소드 선언
	void breathe() {
		
		System.out.println("숨을 쉽니다");
		
	}
	
	
	//추상메소드 선언
	abstract void sound();
	
}
