#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    long long answer = 0;
    stack<int> s;

    cin >> n;

    for (int i=0; i < n; i++) {
        cin >> m;

        if (s.empty()){
            s.push(m);
            continue;
        }

        while (!s.empty() && s.top() <= m) {
            s.pop();
        }

        answer += s.size();
        s.push(m);
    }

    cout << answer;
}
