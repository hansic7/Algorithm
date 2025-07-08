#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m, answer = 0, x, idx;
    deque<int> dq;

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        dq.push_back(i);
    }

    while(m--) {
        cin >> x;

        for (int j = 0; j < dq.size(); j++){
            if (x == dq[j]) {
                idx = j;
                break;
            }
        }
        if (idx <= dq.size()/2){
            while (1) {
                if(dq.front() == x){
                    dq.pop_front();
                    break;
                }
                dq.push_back(dq.front());
                dq.pop_front();
                answer++;
            }
        } else {
            while (1) {
                if(dq.front() == x){
                    dq.pop_front();
                    break;
                }
                dq.push_front(dq.back());
                dq.pop_back();
                answer++;
            }
        }
    }
    cout << answer;
}