#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    
    int n, m;
    string command, strn;
    
    cin >> n;
    
    while (n--) {
        deque<int> dq;
        bool reversed = false, print_error = false;
        string temp;

        cin >> command;
        cin >> m;
        cin >> strn;

        for (int i = 1; i < strn.size(); i++) //string to deque
		{
			if (strn[i] == ',' || strn[i] == ']')
			{
				if (temp != "")
				{
					dq.push_back(stoi(temp));
					temp = "";
				}
			}
			else
			{
				temp += strn[i];
			}
		}

        for (char c : command) {
            if (c == 'R') reversed = !reversed;
            else if (c == 'D') {
                if (dq.empty()) {
                    print_error = true;
                    break;
                }
                if (!reversed) {
                    dq.pop_front();
                } else {
                    dq.pop_back();
                }
            }
            
        }

        if (print_error) {
            cout << "error" << '\n';
            continue;
        }
        
        cout << '[';
        if (!reversed) {
            while (!dq.empty()) {
                cout << dq.front();
                dq.pop_front();
                if (dq.size()) cout << ',';
            }
        } else {
            while (!dq.empty()) {
                cout << dq.back();
                dq.pop_back();
                if (dq.size()) cout << ',';
            }
        }
        cout << ']' << '\n';
    }
}