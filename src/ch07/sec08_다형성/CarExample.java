package ch07.sec08_다형성;

public class CarExample {

	public static void main(String[] args) {
		
		Car mycar = new Car();
		//객체 선언을 해줘야 그걸타고 인스턴스필드 변경가능 
		
		mycar.tire = new Tire();
		mycar.run();
		
		
		/* 부모: Tire
		   자식: HankookTire
		 */
		mycar.tire = new HankookTire();
		mycar.run();
		
		mycar.tire = new KumhoTire();
		mycar.run();
		
		/* 다형성을 쓰는 이유 : 바퀴라는 고유한 특성은 남기되,
		 * 새로운 특성으로 수정하고 싶어서임 (타입변환시 특성 추가 불가)
		 * 자동차 바퀴끼우는 곳에 성능이 다른 타이어 끼우는 거ㅇㅇ
		 * 근데 바퀴함수 자체를 바꿔버리면 다른 타이어 끼울때마다 매번 그부분을 찾은다음
		 * 고치고 하면 코드가 길어질시 문제생길수도?
		 * 걍 상속하면 다른 바퀴 빠르게 찍어낼수있음
		 */
		
	}
}
