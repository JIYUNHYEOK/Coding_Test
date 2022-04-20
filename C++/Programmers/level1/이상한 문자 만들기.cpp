#include <string>

using namespace std;

string solution(string s) {
    int idx = 0;
    
    for (int i=0; i<s.size(); i++) {
        
        if (s[i] == ' ') {
            idx = 0;
            continue;
        }
        
        if (idx%2) { // odd
            if (s[i] <= 'Z') {
                s[i] += 32;
            }
        } else {
            if (s[i] >= 'a') {
                s[i] -= 32;
            }
        }
        idx++;
    }
    
    return s;
}