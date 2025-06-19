#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
 
int main() {

    int n, v, answer;


    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    cin >> v;

    for (int i = 0; i < n; i++){
        if (arr[i] == v)
            answer ++;
    }

    cout << answer;
    
    return 0;
}