#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, int n) {
    int len = 0;
    
    while (my_string[len] != '\0')
        len++;
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(len * n + 1);
    
    int cn = 0;
    for(int c = 0; c < len; c ++) {        
        for (int z = 0; z < n; z++) {
            answer[cn] = my_string[c];
            cn ++;
        }
    }

    answer[cn] = '\0';
    return answer;
}