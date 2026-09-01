#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int answer = 0;
    char x = *s;
    int x_cnt = 1, y_cnt = 0;

    for(int i = 1; s[i]; i++) {
        if (x != s[i]) {
          y_cnt++;  
        } else if (x == s[i]) {
            x_cnt++;
        }
        if (x_cnt == y_cnt) {
            answer++;
            x_cnt = 0;
            y_cnt = 0;
            x = s[i+1];
        }
    }
    
    if (x_cnt || y_cnt)
        answer++;
    
    return answer;
}