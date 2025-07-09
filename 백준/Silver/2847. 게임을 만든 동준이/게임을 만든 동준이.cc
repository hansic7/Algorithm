#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, answer = 0, prev = 0, current, j;
    cin >> n;
    int arr[n];

    for (int i=0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = n-1; i >= 1; i--) {
        while(arr[i] <= arr[i-1]) {
            arr[i-1] -= 1;
            answer++;
        }
    }

    cout << answer;
}