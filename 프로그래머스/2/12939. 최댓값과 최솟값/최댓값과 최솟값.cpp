#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

string solution(string s) {
    vector<int> v;
    stringstream ss(s);
    int num;

    // 문자열을 공백 기준으로 분리해서 숫자 벡터에 저장
    while (ss >> num) {
        v.push_back(num);
    }

    // 최소값, 최대값 찾기
    int min_val = *min_element(v.begin(), v.end());
    int max_val = *max_element(v.begin(), v.end());

    // 문자열로 변환하여 반환
    return to_string(min_val) + " " + to_string(max_val);
}
