#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* s) {
    int s_len = 0;
    
    while (s[s_len] != 0) {
        s_len++;
    }
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * s_len);
    int arr[26] = {};
    int tmp = 0;
    while (tmp < 26) {
        arr[tmp] = -1;
        tmp++;
    }
    // for (int i = 0; i < 26; i++) {
    //     printf("%d ", arr[i]);
    // }
    
    for (int i = 0; i < s_len; i++) {
        if (arr[s[i] - 'a'] == -1) {
            answer[i] = -1;
        } else {
            answer[i] = i - arr[s[i] - 'a'];
        }
        arr[s[i] - 'a'] = i;
    }
    
//     printf("%d\n", s_len);
    

    
    return answer;
}