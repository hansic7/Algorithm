#include<iostream>
#include<algorithm>
#include<vector>
#include<list>

using namespace std;

int main() {
    list<int>::iterator it;
    list<int> list;

    int n,k;

    cin >> n;
    cin >> k;

    it = list.begin();

    for (int i = 1; i <= n; i++) {
        list.insert(it, i);
    }

    it = list.begin();
    
    cout << "<";
    while (!list.empty()){
        for (int i = 1; i < k; ++i) {
            if (++it == list.end()){
                it = list.begin();
            }
        }

        cout << *it;
        it = list.erase(it);
        if (it == list.end()) it = list.begin();

        if (!list.empty()) cout << ", ";
    }

    cout << ">";
}