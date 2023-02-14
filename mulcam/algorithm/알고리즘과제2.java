package mulcam.algorithm;

import java.util.Scanner;
import java.util.StringTokenizer;

public class 알고리즘과제2 {
	
public static void main(String[] args) {
	Scanner in = new Scanner(System.in);

	LinkedStack stackk = new LinkedStack();
	
	String input = in.nextLine();
	StringTokenizer st = new StringTokenizer(input, " ");
	
	while(st.hasMoreTokens()) {
		String nextString = st.nextToken();
	
		if(Num.isNumber(nextString)) {
		stackk.push(nextString);
		} else {
			if(!stackk.isEmpty()) {
				int first = Integer.parseInt(stackk.pop());
                int second = Integer.parseInt(stackk.pop());
                switch (nextString) {
                    case "+":
                        int result = second + first;
                        stackk.push(Integer.toString(result));
                        continue;
                    case "-":
                        result = second - first;
                        stackk.push(Integer.toString(result));
                        continue;
                    case "*":
                        result = second * first;
                        stackk.push(Integer.toString(result));
                        continue;
                    case "/":
                        result = second / first;
                        stackk.push(Integer.toString(result));
                        continue;
                    default:
                    	System.out.println("수식 입력에 오류가 있습니다");
                }
			}
		}
	}
	System.out.println("연산결과 = "+stackk.pop());
}
}

class Num{
	static boolean isNumber(String str) {
		for (int i = 0; i < str.length(); i++) {
			if (!Character.isDigit(str.charAt(i))) {
				return false;
			}
		}
		return true;
	}	
}


class StackNode {
    String data;
    StackNode link;
}

class LinkedStack{
    private StackNode top;

    public boolean isEmpty() {
        return (top == null);
    }

    public void push(String item) {
        StackNode newNode = new StackNode();
        newNode.data = item;
        newNode.link = top;
        top = newNode;
    }

    public String pop() {
        String item = top.data;
        top = top.link;
        return item;
    }
}
