#include <iostream>
#include <deque>
#include <algorithm>
#include <queue>

using namespace std;
char arr[100][100];
bool visited[100][100] = {};
int dy[4] = {0,1,0,-1};
int dx[4] = {-1,0,1,0};
int n;

struct triple {
    int y,x,z;
};

void bfs(int a, int b, string str) {
    queue<pair<int,int>> q;
    q.push({a,b});
    visited[a][b] = true;

    while(!q.empty()) {
        int ny, nx;
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            ny = y + dy[i];
            nx = x + dx[i];

            if (0 <= ny && ny < n && 0 <= nx && nx < n && !visited[ny][nx] &&
                (arr[ny][nx] == str[0] || arr[ny][nx] == str[1])) {
                q.push({ny,nx});
                visited[ny][nx] = true;
            }
        }
    }
}


void reset() {
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            visited[i][j] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    int answer = 0;

    cin >> n;

    for (int i = 0; i < n; i++){
        string tmp;
        cin >> tmp;
        
        for (int j = 0; j < n; j++){
            arr[i][j] = tmp[j];
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (visited[i][j] == false) {
                str = arr[i][j];
                str += '\n';
                bfs(i,j,str);
                answer++;
            }
        }
    }
    cout << answer << ' ';

    reset();
    answer = 0;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (visited[i][j] == false) {
                if (arr[i][j] == 'R' || arr[i][j] == 'G')
                    str = "RG";
                else
                    str = "B\n";
                bfs(i,j,str);
                answer++;
            }
        }
    }

    cout << answer;
}