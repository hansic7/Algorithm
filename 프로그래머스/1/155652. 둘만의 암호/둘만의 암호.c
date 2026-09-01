#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s, const char* skip_s, int index) {
    char* skip = skip_s;
    char c_arr[26];
    int skip_len = 0, iter = 0;
    
    while (skip[skip_len] != '\0')
        skip_len++;
    
    for (int j = skip_len-1; 0 < j; j--) {
        for (int i = 0; i < j; i++) {
            if (skip[i] > skip[i+1]) {
                char tmp = skip[i];
                skip[i] = skip[i+1];
                skip[i+1] = tmp;
            }
        }
    }
    
    int c_arr_len = 0;
    for (char c = 'a'; c <= 'z'; c++){
        if (c == skip[iter]) {
            iter++;
            continue;
        }
        c_arr[c_arr_len] = c;
        c_arr_len++;
    }
    
    int answer_len = 0;
    while (s[answer_len] != '\0')
        answer_len++;
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char) * answer_len + 1);
    answer[answer_len] = '\0';
    
    
    for (int i = 0; i < answer_len; i++) {
        // answer[i] = c_arr[(s[i] - 'a' + index) % c_arr_len];
        
        iter = 0;    
        while (c_arr[iter] != s[i])
            iter++;
        
        answer[i] = c_arr[(iter + index) % c_arr_len];
    }
    
    iter = 0;
    while (c_arr[iter] != '\0') {
        printf("%c ", c_arr[iter]);
        iter++;
    }
    
    printf("\n%d", c_arr_len);
    
    return answer;
}