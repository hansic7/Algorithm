#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = -1;
    
    int standard_sum = 1+2+3+4+5+6+7+8+9;
    
    int tmp = 0;
    
    for (int i = 0; i < numbers_len; i++) {
        tmp += numbers[i];
    }
    
    answer = standard_sum - tmp;
    
    return answer;
}