package ch07.sec10_추상클래스;

public class AbstractMethodExample {

	public static void main(String[] args) {
		
		Cat cat = new Cat();
		Dog dog = new Dog();
		
		cat.breathe();
		cat.sound();
		dog.breathe();
		dog.sound();
		
		/*
		animalSound(new Dog());  --예제에서 이거뭔지 모르겠음
		*/

	}

}
