#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x;
    queue<int> q;
    string op;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> op;

        if (op == "push") {
            cin >> x;
            q.push(x);
        } 
        else if (op == "pop") {
            if (q.empty()) cout << -1 << endl;
            else {
                cout << q.front() << endl;
                q.pop();
            }
        }
        else if (op == "size") cout << q.size() << endl;
        else if (op == "empty") {
            if (q.empty()) cout << 1 << endl;
            else cout << 0 << endl;
        }
        else if (op == "front") {
            if (q.empty()) cout << -1 << endl;
            else cout << q.front() << endl;
        }
        else {
            if (q.empty()) cout << -1 << endl;
            else cout << q.back() << endl;
        }
    }
}