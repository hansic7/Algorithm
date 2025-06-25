#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
 
int main() {
    int n, answer = 0, x;
    int left, right, tmp;
    
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }
    cin >> x;
    sort(arr, arr + n);

    left = 0;
    right = n - 1;

    while (left < right) {
        tmp = arr[left] + arr[right];
        if (tmp > x)
            right --;
        else if (tmp < x)
            left ++;
        else {
            answer ++;
            left ++;
        }
    }

    cout << answer;
}