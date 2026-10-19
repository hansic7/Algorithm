#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// food_len은 배열 food의 길이입니다.
char* solution(int food[], size_t food_len) {
    
    int ans_len = 0, half_ans = 0;
    
    int arr[9] = {};
    
    for (int i = 1; i < food_len; i++) {
        half_ans += food[i] / 2;
        arr[i] = food[i] / 2;
    }
    
    ans_len = half_ans * 2 + 2;
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char) * ans_len);
    
    int iter = 0;
    for (int i = 1; i < food_len; i++) {
        for (int j = 0; j < arr[i]; j++) {
            answer[iter] = i + '0';
            iter++;
        }
    }
    
    answer[iter] = '0';
    iter++;
    
    for (int i = food_len - 1; i > 0; i--) {
        for (int j = 0; j < arr[i]; j++) {
            answer[iter] = i + '0';
            iter++;
        }
    }
    
    answer[iter] = 0;
    
    return answer;
}