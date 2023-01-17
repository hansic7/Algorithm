package ch07.sec08_다형성;

public class Car {
	
	//여기서는 타이어 선언만 해줌
	Tire tire;

	public void run() {
		tire.roll();
	}
}
