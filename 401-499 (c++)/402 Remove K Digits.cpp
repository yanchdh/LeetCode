// URL: https://leetcode.com/problems/remove-k-digits/
// Author: liy
// Desc: A dynamic programming problem, just think about it for a while.
// Date: 2020-03-15

class Solution {
public:
    string removeKdigits(string num, int k) {
        string result;
        int numLen = num.size();
        if (numLen == 0)
            return result;
        int i = 0;
        while (k) {
            while (i < numLen && (result.empty() || result.back() <= num[i])) {
                if (!result.empty() || num[i] != '0')
                    result.push_back(num[i]);
                i++;
            }
            if (!result.empty())
                result.pop_back();
            k--;
        }
        while (i < numLen) {
            if (!result.empty() || num[i] != '0')
                result.push_back(num[i]);
            i++;
        }
        if (result.empty())
            result.push_back('0');
        return result;
    }
};