#include <string>

using namespace std;

int solution(int num) {
    int cnt = 0;
    long long temp = num;
    
    while (temp != 1) {
        
        if (temp % 2 == 0) {
            temp /= 2;
        } else {
            temp = temp*3 + 1;
        }
        
        cnt++;
        
        if (cnt>=500) {
            return -1;
        }
    }
    
    return cnt;
}