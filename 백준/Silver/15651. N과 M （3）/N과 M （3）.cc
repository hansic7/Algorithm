#include <iostream>

using namespace std;
#define MAX 9

int N,M;
int arr[MAX];
bool visited[MAX];

void dfs(int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++)
            cout << arr[i] << ' ';
        cout << '\n';
    } else {
        for (int i = 1; i <= N; i++) {
                arr[depth] = i;
                dfs(depth + 1);
        }
    }
}

int main() {
    cin >> N >> M;
    dfs(0);
}