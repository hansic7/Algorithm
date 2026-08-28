#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = false;
    int tmp = x, sum_x = 0;
    
    while (tmp) {
        sum_x += tmp % 10;
        tmp /= 10;
    }
    
    if (x % sum_x == 0)
        answer = true;
    
    return answer;
}