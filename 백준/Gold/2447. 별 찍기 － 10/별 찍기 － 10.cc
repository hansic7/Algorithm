#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int x = i, y = j;
            bool blank = false;

            // 반복적으로 좌표를 3으로 나누며 중심 영역(1,1)에 있는지 검사
            while (x > 0 || y > 0) {
                if (x % 3 == 1 && y % 3 == 1) {
                    blank = true;
                    break;
                }
                x /= 3;
                y /= 3;
            }

            cout << (blank ? ' ' : '*');
        }
        cout << '\n';
    }

    return 0;
}