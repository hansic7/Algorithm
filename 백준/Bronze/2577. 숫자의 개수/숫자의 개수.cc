#include<algorithm>
#include<iostream>
using namespace std;
 
int main() {

    int a,b,c, mult, i;
    int answer[10] = {};

    cin >> a >> b >> c;

    mult = a * b * c;

    while (mult > 0) {
        i = mult % 10;
        answer[i] += 1;
        mult /= 10;
    }

    for (int j = 0; j < 10; j++) {
        cout << answer[j] << endl;
    }

    return 0;
}
