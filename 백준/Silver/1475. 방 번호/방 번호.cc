#include<algorithm>
#include<iostream>
using namespace std;
 
int main() {

    int arr[10] = {};
    int n, m, flag = 0, answer = 0;
    

    cin >> n;

    while (n > 0) {
        m = n % 10;
        n /= 10;

        if (arr[m] == 0) {
            if (m == 6) 
                m = 9;
            else if (m == 9)
                m = 6;

            if (arr[m] == 0) {
                for (int i = 0; i < 10; i++) {
                    arr[i] += 1;
                }
                answer += 1;
                arr[m] -= 1;
            }
            else
                arr[m] -= 1;

        }
        else
            arr[m] -= 1;

        // cout << "answer = " << answer << " n = " << n << endl;
    }
/*
    for (int i : arr)
        cout << i;
    cout << endl;
*/        


    cout << answer << endl;

}