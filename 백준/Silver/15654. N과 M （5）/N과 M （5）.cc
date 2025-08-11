#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 9

int N, M;
int arr[MAX];         // 선택된 값 저장
bool visited[MAX];    // 인덱스 방문 체크 (0..N-1)
int numbers[MAX];     // 입력 숫자 N개

void dfs(int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++) cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    for (int i = 0; i < N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            arr[depth] = numbers[i];  // 값 사용
            dfs(depth + 1);
            visited[i] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    for (int i = 0; i < N; i++) cin >> numbers[i];

    sort(numbers, numbers + N);  // N개만 정렬 (사전순 출력용)

    dfs(0);
    return 0;
}
