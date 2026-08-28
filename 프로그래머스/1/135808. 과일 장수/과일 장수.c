#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// score_len은 배열 score의 길이입니다.
int solution(int k, int m, int score[], size_t score_len) {
    int answer = 0;
    int arr[10] = {0};
    
    for (int i = 0; i < score_len; i++) {
        arr[score[i]]++;
    }
    
    int in_box = 0, min_p = k;
    for (int i = 9; 0 < i ; i--) {
        while (arr[i]) {
            in_box++;
            if (min_p > i) {
                min_p = i;
            }

            if (in_box == m) {
                in_box = 0;
                answer += (m * min_p);
            }
            arr[i]--;
        }
    }
    
    return answer;
}