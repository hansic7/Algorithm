#include <iostream>
using namespace std;

string answer;

int arr[65][65] = {};

void dfs(int y, int x, int size) {
    
    bool same = true;
    
    for (int i = y; i < y+size; i++) {
        for (int j = x; j < x+size; j++) {
            if (arr[y][x] != arr[i][j]) {
                same = false;
                break;
            };
        }
    }

    if (!same) {
        answer += '(';
        dfs(y, x, size/2); // 1번
        dfs(y, x + size/2, size/2); // 2번
        dfs(y + size/2, x, size/2); // 3번
        dfs(y + size/2, x + size/2, size/2); // 4번
        answer += ')';
    } else {
        if (arr[y][x] == 0)
            answer += '0';
        else if (arr[y][x] == 1)
            answer += '1';
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < n; j++) {
            arr[i][j] = tmp[j] - '0';
        }
    }
    dfs(0,0,n);
    cout << answer << '\n';
}