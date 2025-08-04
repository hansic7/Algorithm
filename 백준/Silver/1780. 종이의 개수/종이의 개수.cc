#include <iostream>
using namespace std;

int zero = 0, minus_one = 0, one = 0;

int arr[2188][2188] = {};

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
        dfs(y, x, size/3); // 1번
        dfs(y, x + size/3, size/3); // 2번
        dfs(y , x + (size/3)*2, size/3); // 3번
        dfs(y + size/3 , x, size/3); // 4번
        dfs(y + size/3 , x + size/3, size/3); // 5번
        dfs(y + size/3 , x + (size/3)*2 , size/3); // 6번
        dfs(y + (size/3)*2 , x, size/3); // 7번
        dfs(y + (size/3)*2 , x + size/3, size/3); // 8번
        dfs(y + (size/3)*2 , x + (size/3)*2 , size/3); // 9번
    } else {
        if (arr[y][x] == 0)
            zero++;
        else if (arr[y][x] == -1)
            minus_one++;
        else if (arr[y][x] == 1)
            one++;
        return;
    }
}

int main(){
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    dfs(0,0,n);
    cout << minus_one << '\n' << zero << '\n' << one << '\n';
}