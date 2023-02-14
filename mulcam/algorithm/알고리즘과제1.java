package mulcam.algorithm;

import java.util.Random;

public class 알고리즘과제1{
    public static void main(String[] args) {
    	Random rand = new Random();
        int a[] = new int[6];
        
        for (int i = 0; i < 6; i++) { 
        	a[i] = rand.nextInt(45)+1;
        	
        	for (int j = i-1; 0 <= j; j--) {
        		if (a[i] == a[j]) {
        			i--;
        			break;
        		}
        	}
        }
        
        Sort S = new Sort();
        S.selectionSort(a);
    }
}

class Sort {
    public void selectionSort(int a[]) {
        int i, j;
        for (i = 0; i < a.length - 1; i++) {
            for (j = i + 1; j < a.length; j++) {
                if (a[i] > a[j]) {
                    int temp = a[i];

                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }
        System.out.printf("로또 번호:");
        for (j = 0; j < a.length; j++)
            System.out.printf("%3d", a[j]);
    }
}
