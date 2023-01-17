package ch07.sec08_다형성;

public class KumhoTire extends Tire {

@Override
//타이어 기능 일부만 대체 느낌
void roll() {
	
	System.out.println("금호타이가 회전합니다");
}
}

/*인터페이스에서는 오버라이드가 필수임
하지만 상속에서는 ㄴㄴ
*/