#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int sum = 0;
    int tmp = x;
    
    while (x>0) {
        sum += x%10;
        x /= 10;
    }
    
    if (tmp%sum) {
        answer = false;
    }
    
    return answer;
}