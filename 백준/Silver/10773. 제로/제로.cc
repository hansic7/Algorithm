#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main() {
    int n, m;
    stack<int> s;
    int answer = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> m;
        if (m == 0) {
            answer -= s.top();
            s.pop();
        } else {
            answer += m;
            s.push(m);
        }
    }
    
    cout << answer << endl;

    return 0;
}