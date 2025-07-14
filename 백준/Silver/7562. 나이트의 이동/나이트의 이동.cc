#include <iostream>
#include <queue>
using namespace std;

struct triple { int y, x, z; };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cnt;
    cin >> test_cnt;

    int dy[8] = {1,2,2,1,-1,-2,-2,-1};
    int dx[8] = {-2,-1,1,2,-2,-1,1,2};

    while (test_cnt--) {
        int n, sy, sx, ey, ex;
        cin >> n >> sy >> sx >> ey >> ex;

        vector<vector<bool>> visited(n, vector<bool>(n, false));
        queue<triple> q;
        q.push({sy, sx, 0});
        visited[sy][sx] = true;

        int cnt = 0;
        while (!q.empty()) {
            auto [y, x, z] = q.front(); q.pop();
            if (y == ey && x == ex) {
                cnt = z;
                break;
            }
            for (int i = 0; i < 8; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= ny && ny < n && 0 <= nx && nx < n && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    q.push({ny, nx, z + 1});
                }
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}
