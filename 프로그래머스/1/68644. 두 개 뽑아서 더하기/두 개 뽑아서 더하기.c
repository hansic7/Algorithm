#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int* solution(int numbers[], size_t numbers_len) {
    
    int* sum_num = (int*)malloc(sizeof(int) * (numbers_len * (numbers_len - 1)));
    int iter = 0, sum_num_len = 0;
    
    for (int i = 0; i < numbers_len; i++) {
        for (int j = i + 1; j < numbers_len; j++) {
            sum_num[iter] = numbers[i] + numbers[j];
            iter++;
        }
    }
    sum_num_len = iter;
    
    // free 해줘야됨
    
    // bubble sort
    for (int j = sum_num_len - 1; 0 < j; j--) {        
        for (int i = 0; i < j; i++) {
            if (sum_num[i] > sum_num[i+1]) {
                int tmp = sum_num[i];
                sum_num[i] = sum_num[i+1];
                sum_num[i+1] = tmp;
            }
        }
    }
    
    // 출력
    for (int i = 0; i < sum_num_len; i++) {
        printf("%d ", sum_num[i]);
    }
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * sum_num_len);
    
    answer[0] = sum_num[0];
    iter = 1;
    for (int i = 1; i < sum_num_len; i++) {
        if (sum_num[i] != sum_num[i-1]) {
            answer[iter] = sum_num[i];
            iter++;
        }
    }
    
    return answer;
}