#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int n) {
    int answer = 0;
    int tmp = 0;
    
    while (n > 0) {
        if (tmp) {
            n += tmp;
            tmp = 0;
        }
        
        if (n % a != 0) {
            tmp += n % a;
            n -= tmp;
        }
        
        answer += (n / a) * b;
        
        n = (n / a) * b;
    }
    
    
    
    return answer;
}