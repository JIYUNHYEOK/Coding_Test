#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b) {
    int tmp = 0;
    
    while (b!=0) {
        tmp = a%b;
        a = b;
        b = tmp;
    }
    
    return a;
}

vector<int> solution(int n, int m) {
    vector<int> answer;
    
    int gcd_num = gcd(max(n,m), min(n,m));
    
    answer.push_back(gcd_num);
    answer.push_back((n*m)/gcd_num);
    
    return answer;
}