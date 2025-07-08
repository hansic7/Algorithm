#include <iostream>
#include <queue>

using namespace std;

int main() {

    int n, temp;
    cin >> n;
    queue<int> q;

    for (int i = 1; i <= n; i++) {
        q.push(i);
    }

    while (q.size() != 1) {
        q.pop();
        temp = q.front();
        q.push(temp);
        q.pop();
    }

    cout << q.front();
}