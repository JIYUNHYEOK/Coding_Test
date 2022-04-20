#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    
    string str = to_string(n); // to_string(): number to string
    
    sort(str.begin(), str.end(), greater<char>());
    answer = stoll(str); // stoll(): string to long long
    return answer;
}