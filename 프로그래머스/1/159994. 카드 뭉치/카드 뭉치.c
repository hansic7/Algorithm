#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

    
bool strcmp(char *a, char* b) {
    while (*a && *b) {
        if (*a != *b) return false;
        a++;
        b++;
    }
    return true;
}

// cards1_len은 배열 cards1의 길이입니다.
// cards2_len은 배열 cards2의 길이입니다.
// goal_len은 배열 goal의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* cards1[], size_t cards1_len, const char* cards2[], size_t cards2_len, const char* goal[], size_t goal_len) {
    int answer_len = 3;
    int iter_1 = 0, iter_2 = 0;

    for (size_t i = 0; i < goal_len; i++) {
        
        if (iter_1 < cards1_len && strcmp(cards1[iter_1], goal[i])) {
            iter_1++;
        } else if (iter_2 < cards2_len && strcmp(cards2[iter_2], goal[i])) {
            iter_2++;
        } else {
            answer_len = 2;
            break;
        }
    }
    
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char) * answer_len + 1);
    
    if (answer_len == 3)
        answer = "Yes";
    else
        answer = "No";
    
    answer[answer_len] = '\0';
    return answer;
}