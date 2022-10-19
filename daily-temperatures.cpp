class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<int> s;
        vector<int> result(size(T));
        for(int i = 0; i < size(T); i++) {
            while(size(s) and T[i] > T[s.top()]) {   
                result[s.top()] = i - s.top();         
                s.pop();
            }
            s.push(i);       
        }
        return result;
    }
};
