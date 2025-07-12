#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    deque<pair<int, int>> dq;

    int n, l;
    cin >> n >> l;
    

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        while (!dq.empty() && dq.front().first <= i - l) {
            dq.pop_front();
        }

        while (!dq.empty() && dq.back().second > num) {
            dq.pop_back();
        }
        
        
        dq.push_back(make_pair(i, num));
        cout << dq.front().second << " ";

    }
}

