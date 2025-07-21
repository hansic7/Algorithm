#include <bits/stdc++.h>
using namespace std;

const int MAX = 100'000 + 1;

/* 전역 배열 (1-based) */
int pick[MAX];          // i번 학생이 고른 학생
bool visited[MAX];      // 현재 DFS 경로에 포함?
bool done[MAX];         // 팀 여부 최종 확정?
int teamCnt;            // 사이클에 속한 학생 수

void dfs(int cur) {
    visited[cur] = true;
    int nxt = pick[cur];

    if (!visited[nxt])
        dfs(nxt);
    else if (!done[nxt]) {            // 사이클 발견
        for (int v = nxt; v != cur; v = pick[v])
            ++teamCnt;
        ++teamCnt;                    // 마지막 cur 포함
    }
    done[cur] = true;                 // 이 노드 처리 완료
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, n;
    cin >> T;
    while (T--) {
        cin >> n;
        for (int i = 1; i <= n; ++i) {
            cin >> pick[i];
            visited[i] = done[i] = false;
        }

        teamCnt = 0;
        for (int i = 1; i <= n; ++i)
            if (!visited[i]) dfs(i);

        cout << n - teamCnt << '\n';  // 팀 못 이룬 학생
    }
    return 0;
}
