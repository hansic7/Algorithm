#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// food_len은 배열 food의 길이입니다.
char* solution(int food[], size_t food_len) {
    
    int food_cnt[10] = {0};
    int count = 0;
    
    for (int i = 1; i < food_len; i++) {
        food_cnt[i] = food[i] / 2;
        count += food_cnt[i];
        printf("%d ", food_cnt[i]);
    }    
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char) * (count * 2 + 2));
    
    int iter = 0;
    for (int i = 1; i < food_len; i++) {
        for (int j = 0; j < food_cnt[i]; j++) {
            answer[iter] = i + '0';
            answer[(count * 2) - iter] = i + '0';
            iter++;
        }
    }
    
    answer[iter] = '0';
    answer[count * 2 + 1] = '\0';
    
    return answer;
}