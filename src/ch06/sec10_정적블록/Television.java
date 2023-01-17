package ch06.sec10_정적블록;

public class Television {
	
	static String Company;
	static String model;
	
//	static String info = Company + '-' +  model;
	//위쪽은 info 만드는게 쉬울때, 아래는 어려울때  

	static String info; 
	static {  // static 블록은 메모리에 로딩되면 자동으로 실행됨
		System.out.println("1");
		info = "정보 : "  + Company;
		info += "-" + model; 
	}
	
	static {
		System.out.println("2");
	}
}
