package ch07.sec07_자동타입변환;

public class ChildExample {

	public static void main(String[] args) {
	
		Child child = new Child();
		Parent parent = child;
		
		parent.method1();
		parent.method2();
		//타입변환이 해서 child 타고 들어감 +  method2는 child에서 오버라이드 놓음
		
	}

}
