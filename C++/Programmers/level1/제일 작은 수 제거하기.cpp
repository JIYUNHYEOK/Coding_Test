#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    
    if (arr.size() == 1) {
        arr.clear();
        arr.push_back(-1);
        return arr;
    } 
    
    arr.erase(min_element(arr.begin(), arr.end()));
    
    return arr;
}