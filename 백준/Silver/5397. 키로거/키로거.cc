#include<iostream>
#include<algorithm>
#include<vector>
#include<list>

using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    list<char>::iterator it;
    list<char> password;

    for (int z = 0; z < n; z++) {
        cin >> s;
        password.clear();
        it = password.begin();

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '<') {
                if (it != password.begin()) it--;
            }

            else if (s[i] == '>') {
                if (it != password.end()) it++;
            }

            else if (s[i] == '-') {
                if (it != password.begin()) {
                    it = password.erase(--it);
                }
            }

            else {
                it = password.insert(it, s[i]);
                it++;
            }
        }

        for (char c : password)
            cout << c;
        cout << endl;
    }
    return 0;
}

