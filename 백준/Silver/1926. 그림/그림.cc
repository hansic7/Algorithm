#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;
int arr[500][500];
bool visited[500][500] = {};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m, paint = 0, tmp_size = 0, size = 0;
    deque<pair<int, int>> dq;
    pair<int, int> now;

    cin >> n >> m;

    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> arr[i][j];
        }
    }

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    

    for (int f = 0; f < n; f++) {
        for (int g = 0; g < m; g++) {
            if (!visited[f][g] && arr[f][g] == 1) {
                dq.push_back(make_pair(f,g));
                visited[f][g] = true;
                tmp_size++;
            }
            while (!dq.empty()) {
                now = dq.front();
                dq.pop_front();

                for (int i = 0; i < 4; i++) {
                    int ny = now.first + dy[i];
                    int nx = now.second + dx[i];

                    if (0 <= ny && ny < n && 0 <= nx && nx < m) {
                        if (!visited[ny][nx] && arr[ny][nx] == 1) {
                            visited[ny][nx] = true;
                            dq.push_back(make_pair(ny,nx));
                            tmp_size++;
                        }
                    }
                }
            }
            if (tmp_size) {
                paint++;
                if (size < tmp_size) size = tmp_size;
                tmp_size = 0;
            }
        }
    }

    cout << paint << '\n' << size << '\n';
}
