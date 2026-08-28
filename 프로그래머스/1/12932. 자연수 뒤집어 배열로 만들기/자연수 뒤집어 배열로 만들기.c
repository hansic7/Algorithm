#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(long long n) {
    int len = 0, tmp = n;
    
    while (tmp) {
        tmp /= 10;
        len++;
    }
    
    // 리턴할 값은 메모리를 동적 할당해주세요.
    int* answer = (int*)malloc(sizeof(int) * len);
    
    int i = 0;
    while (n) {
        answer[i] = n % 10;
        i++;
        n /= 10;
    }
    
    return answer;
}